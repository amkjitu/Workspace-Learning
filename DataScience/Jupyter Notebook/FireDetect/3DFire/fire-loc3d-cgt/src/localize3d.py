# import cv2, time, yaml, numpy as np, os
# from .detector import FireSmokeDetector
# from .anchor_model import AnchorNet, size_norm, apply_anchor_heuristic
# from .associate import simple_nearest, fundamental_from_KRT, epipolar_pairs
# from .geometry import ray_from_pixel, intersect_plane, triangulate
# from .utils import load_calib, load_planes

# CLASSES = {0: "fire", 1: "smoke"}  # adjust to match your model


# def get_anchors(frame, dets, model=None, device="cpu"):
#     anchors = []
#     if model is None:
#         for cls, box, conf in dets:
#             anchors.append((*apply_anchor_heuristic(CLASSES.get(cls, str(cls)), box),))
#         return anchors
#     # (Optional) crop ROIs and run AnchorNet for (du,dv,q) then convert to pixels
#     raise NotImplementedError("Plug in your AnchorNet inference if trained.")


# def localize_pair(cfg):
#     # # OpenCV capture (lowest latency)
#     # capL = cv2.VideoCapture(cfg["left"]["rtsp"], cv2.CAP_FFMPEG)
#     # capR = cv2.VideoCapture(cfg["right"]["rtsp"], cv2.CAP_FFMPEG)
#     # K_L, R_L, T_L, P_L = load_calib(cfg["left"]["calib_file"])
#     # K_R, R_R, T_R, P_R = load_calib(cfg["right"]["calib_file"])
#     # planes = load_planes("configs/planes.json")
#     # det = FireSmokeDetector(cfg["model"]["yolov10_weights"])

#     # --- Normalize and validate critical paths ---
#     for side in ("left", "right"):
#         cfg[side]["calib_file"] = os.path.normpath(cfg[side]["calib_file"])
#         if not os.path.isfile(cfg[side]["calib_file"]):
#             raise FileNotFoundError(
#                 f"Calibration file missing: {cfg[side]['calib_file']}"
#             )
#     planes_path = os.path.normpath("configs/planes.json")
#     if not os.path.isfile(planes_path):
#         raise FileNotFoundError(f"Plane config missing: {planes_path}")
#     weights_path = os.path.normpath(cfg["model"]["yolov10_weights"])

#     # OpenCV capture (lowest latency)
#     capL = cv2.VideoCapture(cfg["left"]["rtsp"], cv2.CAP_FFMPEG)
#     capL.set(cv2.CAP_PROP_BUFFERSIZE, 100)  # Set buffer size to 50

#     capR = cv2.VideoCapture(cfg["right"]["rtsp"], cv2.CAP_FFMPEG)
#     capR.set(cv2.CAP_PROP_BUFFERSIZE, 100)  # Set buffer size to 50

#     if not capL.isOpened():
#         raise RuntimeError(f"Could not open Left RTSP: {cfg['left']['rtsp']}")
#     if not capR.isOpened():
#         raise RuntimeError(f"Could not open Right RTSP: {cfg['right']['rtsp']}")

#     K_L, R_L, T_L, P_L = load_calib(cfg["left"]["calib_file"])
#     K_R, R_R, T_R, P_R = load_calib(cfg["right"]["calib_file"])
#     planes = load_planes(planes_path)
#     det = FireSmokeDetector(weights_path)

#     anchor_model = None  # load if weights provided

#     # Fundamental matrix for epipolar matching
#     F = (
#         fundamental_from_KRT(K_L, R_L, T_L, K_R, R_R, T_R)
#         if cfg["runtime"]["assoc_mode"] == "epipolar"
#         else None
#     )

#     # csv = open(cfg["runtime"]["save_csv"], "w") if cfg["runtime"]["save_csv"] else None

#     csv = None
#     if cfg["runtime"]["save_csv"]:
#         save_csv = os.path.normpath(cfg["runtime"]["save_csv"])
#         os.makedirs(os.path.dirname(save_csv), exist_ok=True)
#         csv = open(save_csv, "w", newline="")

#     if csv:
#         csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap\n")

#     while True:
#         t0 = time.time()
#         okL, frameL = capL.read()
#         okR, frameR = capR.read()
#         if not (okL and okR):
#             break

#         detsL = det.infer(frameL)
#         detsR = det.infer(frameR)
#         anchorsL = get_anchors(frameL, detsL, model=anchor_model)
#         anchorsR = get_anchors(frameR, detsR, model=anchor_model)

#         # associate
#         pairs = (
#             epipolar_pairs(detsL, detsR, F)
#             if F is not None
#             else simple_nearest(detsL, detsR)
#         )
#         seenR = set([j for _, j in pairs])

#         # Compute 3D for pairs (triangulate), others (single-view plane)
#         for i, (clsL, boxL, confL) in enumerate(detsL):
#             uL, vL, _ = anchorsL[i]
#             Cw = None
#             mode = "plane"
#             gap = np.nan
#             CL, dL = ray_from_pixel(uL, vL, K_L, R_L, T_L)
#             # If paired -> triangulate
#             pr = [p for p in pairs if p[0] == i]
#             if pr:
#                 j = pr[0][1]
#                 uR, vR, _ = anchorsR[j]
#                 CR, dR = ray_from_pixel(uR, vR, K_R, R_R, T_R)
#                 Pw, gap = triangulate(CL, dL, CR, dR)
#                 if Pw is not None:
#                     Cw = Pw
#                     mode = "stereo"
#             # Fallback single-view plane (floor)
#             if Cw is None:
#                 n = planes["floor"]["n"]
#                 b = planes["floor"]["b"]
#                 hit = intersect_plane(CL, dL, n, b)
#                 Cw = hit if hit is not None else CL + 2.0 * dL
#             x, y, z = Cw.tolist()
#             if csv:
#                 uR = vR = np.nan
#                 csv.write(
#                     f"{t0:.3f},{CLASSES.get(clsL,clsL)},{confL:.2f},{uL:.1f},{vL:.1f},{uR},{vR},{x:.3f},{y:.3f},{z:.3f},{mode},{gap}\n"
#                 )

#         # draw
#         if cfg["runtime"]["draw"]:
#             from .visualize import draw_det

#             visL = draw_det(
#                 frameL.copy(), detsL, [(a[0], a[1], a[2]) for a in anchorsL]
#             )
#             cv2.imshow("Left", visL)
#             cv2.imshow(
#                 "Right",
#                 draw_det(frameR.copy(), detsR, [(a[0], a[1], a[2]) for a in anchorsR]),
#             )
#             if cv2.waitKey(1) & 0xFF == 27:
#                 break

#     if csv:
#         csv.close()
#     capL.release()
#     capR.release()
#     cv2.destroyAllWindows()


# import cv2, time, yaml, numpy as np, os
# from collections import deque

# from .detector import FireSmokeDetector
# from .anchor_model import AnchorNet, size_norm, apply_anchor_heuristic
# from .associate import simple_nearest, fundamental_from_KRT, epipolar_pairs
# from .geometry import ray_from_pixel, intersect_plane, triangulate
# from .utils import load_calib, load_planes

# CLASSES = {0: "fire", 1: "smoke"}  # adjust to match your model


# def get_anchors(frame, dets, model=None, device="cpu"):
#     """Return per-detection (u_anchor, v_anchor, q). Uses heuristic if no model."""
#     anchors = []
#     if model is None:
#         for cls, box, conf in dets:
#             anchors.append((*apply_anchor_heuristic(CLASSES.get(cls, str(cls)), box),))
#         return anchors
#     # (Optional) crop ROIs and run AnchorNet for (du,dv,q) then convert to pixels
#     raise NotImplementedError("Plug in your AnchorNet inference if trained.")


# def _open_rtsp_low_latency(url: str):
#     """
#     Open an RTSP stream with low-latency flags where possible.
#     Returns a cv2.VideoCapture.
#     """
#     # Try FFMPEG with low-latency flags embedded in URL.
#     # (Some cameras ignore query params; it's still harmless.)
#     low = f"{url}" f"?tcp&fflags=nobuffer&flags=low_delay&max_delay=1"
#     cap = cv2.VideoCapture(low, cv2.CAP_FFMPEG)
#     # Keep buffer tiny so we always read the freshest frames
#     try:
#         cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
#     except Exception:
#         pass
#     return cap

### 2nd version after edits ###
# def localize_pair(cfg):
#     # --- Normalize and validate critical paths ---
#     for side in ("left", "right"):
#         cfg[side]["calib_file"] = os.path.normpath(cfg[side]["calib_file"])
#         if not os.path.isfile(cfg[side]["calib_file"]):
#             raise FileNotFoundError(
#                 f"Calibration file missing: {cfg[side]['calib_file']}"
#             )
#     planes_path = os.path.normpath("configs/planes.json")
#     if not os.path.isfile(planes_path):
#         raise FileNotFoundError(f"Plane config missing: {planes_path}")
#     weights_path = os.path.normpath(cfg["model"]["yolov10_weights"])

#     # --- Open RTSP with low-latency settings ---
#     capL = _open_rtsp_low_latency(cfg["left"]["rtsp"])
#     capR = _open_rtsp_low_latency(cfg["right"]["rtsp"])
#     if not capL.isOpened():
#         raise RuntimeError(f"Could not open Left RTSP: {cfg['left']['rtsp']}")
#     if not capR.isOpened():
#         raise RuntimeError(f"Could not open Right RTSP: {cfg['right']['rtsp']}")

#     # --- Load calibration and planes ---
#     K_L, R_L, T_L, P_L = load_calib(cfg["left"]["calib_file"])
#     K_R, R_R, T_R, P_R = load_calib(cfg["right"]["calib_file"])
#     planes = load_planes(planes_path)

#     # --- Detector ---
#     det = FireSmokeDetector(weights_path)
#     anchor_model = None  # load if you later train it

#     # --- Association geometry ---
#     F = (
#         fundamental_from_KRT(K_L, R_L, T_L, K_R, R_R, T_R)
#         if cfg["runtime"]["assoc_mode"] == "epipolar"
#         else None
#     )

#     # --- CSV logging (ensure folder exists) ---
#     csv = None
#     if cfg["runtime"]["save_csv"]:
#         save_csv = os.path.normpath(cfg["runtime"]["save_csv"])
#         os.makedirs(os.path.dirname(save_csv), exist_ok=True)
#         csv = open(save_csv, "w", newline="")
#         csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap\n")

#     # --- Time pairing buffers ---
#     max_pair_dt = float(cfg["runtime"].get("max_pair_dt_ms", 60)) / 1000.0
#     bufL, bufR = deque(maxlen=60), deque(maxlen=60)  # (t, frame)

#     # --- Main loop ---
#     while True:
#         # Grab newest frames into small buffers
#         t_now = time.time()
#         okL, fL = capL.read()
#         okR, fR = capR.read()
#         if not okL and not okR:
#             break
#         if okL:
#             bufL.append((t_now, fL))
#         if okR:
#             bufR.append((t_now, fR))
#         if not bufL or not bufR:
#             continue

#         # Pair by closest timestamp
#         tL, frameL = bufL[-1]
#         tR, frameR = min(bufR, key=lambda p: abs(p[0] - tL))
#         if abs(tR - tL) > max_pair_dt:
#             # too far apart in time, wait for a closer pair
#             continue
#         t0 = (tL + tR) / 2.0

#         # --- Run detectors on paired frames ---
#         detsL = det.infer(frameL)
#         detsR = det.infer(frameR)
#         anchorsL = get_anchors(frameL, detsL, model=anchor_model)
#         anchorsR = get_anchors(frameR, detsR, model=anchor_model)

#         # --- Associate detections across views ---
#         if F is not None:
#             pairs = epipolar_pairs(detsL, detsR, F)
#         else:
#             pairs = simple_nearest(detsL, detsR)

#         # --- For each left detection, compute 3D ---
#         for i, (clsL, boxL, confL) in enumerate(detsL):
#             uL, vL, _ = anchorsL[i]
#             Cw = None
#             mode = "plane"
#             gap = np.nan
#             uR_log = np.nan
#             vR_log = np.nan

#             CL, dL = ray_from_pixel(uL, vL, K_L, R_L, T_L)

#             # If paired -> triangulate
#             pr = [p for p in pairs if p[0] == i]
#             if pr:
#                 j = pr[0][1]
#                 uR, vR, _ = anchorsR[j]
#                 CR, dR = ray_from_pixel(uR, vR, K_R, R_R, T_R)
#                 Pw, gap = triangulate(CL, dL, CR, dR)
#                 if Pw is not None:
#                     Cw = Pw
#                     mode = "stereo"
#                     uR_log, vR_log = uR, vR

#             # Fallback: single-view ray -> floor plane
#             if Cw is None:
#                 n = planes["floor"]["n"]
#                 b = planes["floor"]["b"]
#                 hit = intersect_plane(CL, dL, n, b)
#                 Cw = hit if hit is not None else CL + 2.0 * dL

#             x, y, z = Cw.tolist()

#             if csv:
#                 csv.write(
#                     f"{t0:.3f},{CLASSES.get(clsL,clsL)},{confL:.2f},"
#                     f"{uL:.1f},{vL:.1f},{uR_log if mode=='stereo' else np.nan},"
#                     f"{vR_log if mode=='stereo' else np.nan},"
#                     f"{x:.3f},{y:.3f},{z:.3f},{mode},{gap}\n"
#                 )

#         # --- Quick visual debug ---
#         if cfg["runtime"]["draw"]:
#             from .visualize import draw_det

#             visL = draw_det(
#                 frameL.copy(), detsL, [(a[0], a[1], a[2]) for a in anchorsL]
#             )
#             visR = draw_det(
#                 frameR.copy(), detsR, [(a[0], a[1], a[2]) for a in anchorsR]
#             )
#             cv2.imshow("Left", visL)
#             cv2.imshow("Right", visR)
#             if cv2.waitKey(1) & 0xFF == 27:
#                 break

#     if csv:
#         csv.close()
#     capL.release()
#     capR.release()
#     cv2.destroyAllWindows()


# ### 3rd version after edits ###
# import cv2, time, yaml, numpy as np, os
# from collections import deque

# from .detector import FireSmokeDetector
# from .anchor_model import AnchorNet, size_norm, apply_anchor_heuristic
# from .associate import simple_nearest, fundamental_from_KRT, epipolar_pairs
# from .geometry import ray_from_pixel, intersect_plane, triangulate
# from .utils import load_calib, load_planes

# CLASSES = {0: "fire", 1: "smoke"}  # adjust to match your model


# def get_anchors(frame, dets, model=None, device="cpu"):
#     """Return per-detection (u_anchor, v_anchor, q). Uses heuristic if no model."""
#     anchors = []
#     if model is None:
#         for cls, box, conf in dets:
#             anchors.append((*apply_anchor_heuristic(CLASSES.get(cls, str(cls)), box),))
#         return anchors
#     # (Optional) crop ROIs and run AnchorNet for (du,dv,q) then convert to pixels
#     raise NotImplementedError("Plug in your AnchorNet inference if trained.")


# def _open_rtsp_low_latency(url: str):
#     """Open an RTSP stream with low-latency flags where possible."""
#     low = f"{url}?tcp&fflags=nobuffer&flags=low_delay&max_delay=1"
#     cap = cv2.VideoCapture(low, cv2.CAP_FFMPEG)
#     try:
#         cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
#     except Exception:
#         pass
#     return cap


# def height_from_plane(Pw, n, b):
#     """Signed distance from point Pw to plane n^T X + b = 0 (n needn't be unit)."""
#     n = np.asarray(n, dtype=float)
#     return (n @ Pw + b) / (np.linalg.norm(n) + 1e-12)


# def _epipolar_error(F, pL, pR):
#     """Distance of right-point to right epipolar line from left-point."""
#     # p* are homogeneous [u,v,1]
#     lR = F @ pL
#     return abs(lR @ pR) / (np.sqrt(lR[0] ** 2 + lR[1] ** 2) + 1e-12)


# def localize_pair(cfg):
#     # --- Normalize and validate critical paths ---
#     for side in ("left", "right"):
#         cfg[side]["calib_file"] = os.path.normpath(cfg[side]["calib_file"])
#         if not os.path.isfile(cfg[side]["calib_file"]):
#             raise FileNotFoundError(
#                 f"Calibration file missing: {cfg[side]['calib_file']}"
#             )
#     planes_path = os.path.normpath("configs/planes.json")
#     if not os.path.isfile(planes_path):
#         raise FileNotFoundError(f"Plane config missing: {planes_path}")
#     weights_path = os.path.normpath(cfg["model"]["yolov10_weights"])

#     # --- Open RTSP with low latency ---
#     capL = _open_rtsp_low_latency(cfg["left"]["rtsp"])
#     capR = _open_rtsp_low_latency(cfg["right"]["rtsp"])
#     if not capL.isOpened():
#         raise RuntimeError(f"Could not open Left RTSP: {cfg['left']['rtsp']}")
#     if not capR.isOpened():
#         raise RuntimeError(f"Could not open Right RTSP: {cfg['right']['rtsp']}")

#     # --- Calibration & planes ---
#     K_L, R_L, T_L, P_L = load_calib(cfg["left"]["calib_file"])
#     K_R, R_R, T_R, P_R = load_calib(cfg["right"]["calib_file"])
#     planes = load_planes(planes_path)

#     # --- Detector ---
#     det = FireSmokeDetector(weights_path, conf=float(cfg["model"].get("conf", 0.15)))
#     anchor_model = None  # load if trained later

#     # --- Association geometry/tuning ---
#     assoc_mode = cfg["runtime"].get("assoc_mode", "simple").lower()
#     F = (
#         fundamental_from_KRT(K_L, R_L, T_L, K_R, R_R, T_R)
#         if assoc_mode == "epipolar"
#         else None
#     )
#     epi_tol = float(cfg["runtime"].get("epipolar_tol_px", 2.0))
#     min_box_area = float(cfg["runtime"].get("min_box_area_px", 0))  # filter tiny boxes

#     # --- CSV ---
#     csv = None
#     if cfg["runtime"]["save_csv"]:
#         save_csv = os.path.normpath(cfg["runtime"]["save_csv"])
#         os.makedirs(os.path.dirname(save_csv), exist_ok=True)
#         csv = open(save_csv, "w", newline="")
#         # csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap,epi_err\n")
#         csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap,epi_err,height\n")

#     # --- Time pairing buffers ---
#     max_pair_dt = float(cfg["runtime"].get("max_pair_dt_ms", 60)) / 1000.0
#     bufL, bufR = deque(maxlen=60), deque(maxlen=60)  # (t, frame)

#     # --- Main loop ---
#     while True:
#         t_now = time.time()
#         okL, fL = capL.read()
#         okR, fR = capR.read()
#         if not okL and not okR:
#             break
#         if okL:
#             bufL.append((t_now, fL))
#         if okR:
#             bufR.append((t_now, fR))
#         if not bufL or not bufR:
#             continue

#         # Pair by closest timestamps
#         tL, frameL = bufL[-1]
#         tR, frameR = min(bufR, key=lambda p: abs(p[0] - tL))
#         if abs(tR - tL) > max_pair_dt:
#             continue
#         t0 = (tL + tR) / 2.0

#         # --- Detections ---
#         detsL = det.infer(frameL)
#         detsR = det.infer(frameR)

#         # optional tiny-box filter
#         if min_box_area > 0:
#             detsL = [
#                 (c, b, s)
#                 for (c, b, s) in detsL
#                 if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
#             ]
#             detsR = [
#                 (c, b, s)
#                 for (c, b, s) in detsR
#                 if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
#             ]

#         anchorsL = get_anchors(frameL, detsL, model=anchor_model)
#         anchorsR = get_anchors(frameR, detsR, model=anchor_model)

#         # --- Associate ---
#         if assoc_mode == "epipolar":
#             pairs = epipolar_pairs(detsL, detsR, F, tol=epi_tol)
#             if not pairs and detsL and detsR:
#                 print(
#                     f"Epipolar [assoc] no pairs: L={len(detsL)} R={len(detsR)} "
#                     f"(try increasing runtime.simple_max_dv or max_pair_dt_ms)"
#                 )
#         else:
#             # pairs = simple_nearest(detsL, detsR, max_dv=300)
#             simple_max = int(cfg["runtime"].get("simple_max_dv", 120))
#             pairs = simple_nearest(detsL, detsR, max_dv=simple_max)
#             if not pairs and detsL and detsR:
#                 print(
#                     f"Simple [assoc] no pairs: L={len(detsL)} R={len(detsR)} "
#                     f"(try increasing runtime.simple_max_dv or max_pair_dt_ms)"
#                 )

#         # --- For each left detection, compute 3D ---
#         for i, (clsL, boxL, confL) in enumerate(detsL):
#             uL, vL, _ = anchorsL[i]
#             CL, dL = ray_from_pixel(uL, vL, K_L, R_L, T_L)

#             Cw, mode, gap = None, "plane", np.nan
#             uR_log, vR_log, epi_err = np.nan, np.nan, np.nan

#             # Try stereo
#             pr = [p for p in pairs if p[0] == i]
#             if pr:
#                 j = pr[0][1]
#                 uR, vR, _ = anchorsR[j]
#                 CR, dR = ray_from_pixel(uR, vR, K_R, R_R, T_R)
#                 Pw, gap = triangulate(CL, dL, CR, dR)
#                 if Pw is not None:
#                     Cw = Pw
#                     mode = "stereo"
#                     uR_log, vR_log = uR, vR
#                     if F is not None:
#                         epi_err = _epipolar_error(
#                             F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0])
#                         )

#             # Fallback: single-view ray -> floor
#             n = planes["floor"]["n"]
#             b = planes["floor"]["b"]
#             if Cw is None:
#                 hit = intersect_plane(CL, dL, n, b)
#                 Cw = hit if hit is not None else CL + 2.0 * dL

#             # x, y, z = Cw.tolist()
#             # height = float(height_from_plane(Cw, n, b))  # <-- TRUE height above the floor plane
#             scale = float(cfg["runtime"].get("unit_scale_m_per_world_unit", 1.0))
#             x, y, z = (Cw * scale).tolist()
#             height = float(height_from_plane(Cw, n, b)) * scale  # plane computed in world units too
#             gap_to_log = gap * scale if not np.isnan(gap) else gap

#             if csv:
#                 csv.write(
#                     f"{t0:.3f},{CLASSES.get(clsL,clsL)},{confL:.2f},"
#                     f"{uL:.1f},{vL:.1f},{uR_log if mode=='stereo' else np.nan},"
#                     f"{vR_log if mode=='stereo' else np.nan},"
#                     f"{x:.3f},{y:.3f},{z:.3f},{mode},{gap_to_log},{epi_err},{height:.3f}\n"
#                 )

#         # --- OSD ---
#         if cfg["runtime"]["draw"]:
#             from .visualize import draw_det

#             visL = draw_det(
#                 frameL.copy(), detsL, [(a[0], a[1], a[2]) for a in anchorsL]
#             )
#             visR = draw_det(
#                 frameR.copy(), detsR, [(a[0], a[1], a[2]) for a in anchorsR]
#             )
#             # show quick height text from the last computed result if stereo existed
#             cv2.putText(visL, f"assoc={assoc_mode}", (10, 24), 0, 0.7, (0, 255, 255), 2)
#             cv2.putText(
#                 visR, f"conf>={det.conf:.2f}", (10, 24), 0, 0.7, (0, 255, 255), 2
#             )
#             # optional: show last computed height on the left view
#             cv2.putText(visL, "height: plane Z", (10, 48), 0, 0.6, (0, 255, 0), 2)

#             cv2.imshow("Left", visL)
#             cv2.imshow("Right", visR)
#             if cv2.waitKey(1) & 0xFF == 27:
#                 break

#     if csv:
#         csv.close()
#     capL.release()
#     capR.release()
#     cv2.destroyAllWindows()


# ### 4th version after edits debugging purpose working better more than 3,2,1 ###
# import cv2, time, yaml, numpy as np, os
# from collections import deque

# from .detector import FireSmokeDetector
# from .anchor_model import AnchorNet, size_norm, apply_anchor_heuristic
# from .associate import simple_nearest, fundamental_from_KRT, epipolar_pairs
# from .geometry import ray_from_pixel, intersect_plane, triangulate
# from .utils import load_calib, load_planes

# CLASSES = {0: "fire", 1: "smoke"}  # adjust to match your model


# def _box_center_xyxy(box):
#     x1, y1, x2, y2 = box
#     return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)


# def _pair_diagnostics(detsL, detsR, ignore_class=False):
#     """Return (min_dv, min_dist, i_min, j_min, i_dv, j_dv) for debug."""
#     if not detsL or not detsR:
#         return None
#     mins = {"dv": (1e9, None, None), "dist": (1e9, None, None)}
#     for i, (cL, bL, _) in enumerate(detsL):
#         cxL, cyL = _box_center_xyxy(bL)
#         for j, (cR, bR, _) in enumerate(detsR):
#             if (not ignore_class) and (cL != cR):
#                 continue
#             cxR, cyR = _box_center_xyxy(bR)
#             dv = abs(cyR - cyL)
#             d2 = (cxR - cxL) ** 2 + (cyR - cyL) ** 2
#             if dv < mins["dv"][0]:
#                 mins["dv"] = (dv, i, j)
#             if d2 < mins["dist"][0]:
#                 mins["dist"] = (d2, i, j)
#     if mins["dist"][1] is None:
#         return None
#     min_dv, i_dv, j_dv = mins["dv"]
#     min_dist = np.sqrt(mins["dist"][0])
#     i_min, j_min = mins["dist"][1], mins["dist"][2]
#     return (min_dv, min_dist, i_min, j_min, i_dv, j_dv)


# def get_anchors(frame, dets, model=None, device="cpu"):
#     """Return per-detection (u_anchor, v_anchor, q). Uses heuristic if no model."""
#     anchors = []
#     if model is None:
#         for cls, box, conf in dets:
#             anchors.append((*apply_anchor_heuristic(CLASSES.get(cls, str(cls)), box),))
#         return anchors
#     # (Optional) crop ROIs and run AnchorNet for (du,dv,q) then convert to pixels
#     raise NotImplementedError("Plug in your AnchorNet inference if trained.")


# def _open_rtsp_low_latency(url: str):
#     """Open an RTSP stream with low-latency flags where possible."""
#     low = f"{url}?tcp&fflags=nobuffer&flags=low_delay&max_delay=1"
#     cap = cv2.VideoCapture(low, cv2.CAP_FFMPEG)
#     try:
#         cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
#     except Exception:
#         pass
#     return cap


# def height_from_plane(Pw, n, b):
#     """Signed distance from point Pw to plane n^T X + b = 0 (n needn't be unit)."""
#     n = np.asarray(n, dtype=float)
#     return (n @ Pw + b) / (np.linalg.norm(n) + 1e-12)


# def _epipolar_error(F, pL, pR):
#     """Distance of right-point to right epipolar line from left-point."""
#     # p* are homogeneous [u,v,1]
#     lR = F @ pL
#     return abs(lR @ pR) / (np.sqrt(lR[0] ** 2 + lR[1] ** 2) + 1e-12)


# def localize_pair(cfg):
#     # --- Normalize and validate critical paths ---
#     for side in ("left", "right"):
#         cfg[side]["calib_file"] = os.path.normpath(cfg[side]["calib_file"])
#         if not os.path.isfile(cfg[side]["calib_file"]):
#             raise FileNotFoundError(
#                 f"Calibration file missing: {cfg[side]['calib_file']}"
#             )
#     planes_path = os.path.normpath("configs/planes.json")
#     if not os.path.isfile(planes_path):
#         raise FileNotFoundError(f"Plane config missing: {planes_path}")
#     weights_path = os.path.normpath(cfg["model"]["yolov10_weights"])

#     # --- Open RTSP with low latency ---
#     capL = _open_rtsp_low_latency(cfg["left"]["rtsp"])
#     capR = _open_rtsp_low_latency(cfg["right"]["rtsp"])
#     if not capL.isOpened():
#         raise RuntimeError(f"Could not open Left RTSP: {cfg['left']['rtsp']}")
#     if not capR.isOpened():
#         raise RuntimeError(f"Could not open Right RTSP: {cfg['right']['rtsp']}")

#     # --- Calibration & planes ---
#     K_L, R_L, T_L, P_L = load_calib(cfg["left"]["calib_file"])
#     K_R, R_R, T_R, P_R = load_calib(cfg["right"]["calib_file"])
#     planes = load_planes(planes_path)

#     # --- Detector ---
#     det = FireSmokeDetector(weights_path, conf=float(cfg["model"].get("conf", 0.15)))
#     anchor_model = None  # load if trained later

#     # --- Association geometry/tuning ---
#     assoc_mode = cfg["runtime"].get("assoc_mode", "simple").lower()
#     F = (
#         fundamental_from_KRT(K_L, R_L, T_L, K_R, R_R, T_R)
#         if assoc_mode == "epipolar"
#         else None
#     )

#     ignore_class = bool(cfg["runtime"].get("ignore_class", False))
#     simple_metric = cfg["runtime"].get("simple_metric", "v")  # "v" or "euclidean"
#     simple_max_dv = int(cfg["runtime"].get("simple_max_dv", 160))
#     simple_max_dist = float(cfg["runtime"].get("simple_max_dist", 260.0))
#     force_pair = cfg["runtime"].get("assoc_mode", "simple").lower() == "force"
#     show_indices = bool(cfg["runtime"].get("show_indices", True))

#     epi_tol = float(cfg["runtime"].get("epipolar_tol_px", 2.0))
#     min_box_area = float(cfg["runtime"].get("min_box_area_px", 0))  # filter tiny boxes

#     # D1 = np.load("calib/cam_left.npz")
#     D1 = np.load("calib/cam_left_shared.npz")
#     # D2 = np.load("calib/cam_right.npz")
#     D2 = np.load("calib/cam_right_shared.npz")
#     R1, R2 = D1["R"], D2["R"]
#     T1, T2 = D1["T"], D2["T"]
#     C1 = (-R1.T @ T1).ravel()
#     C2 = (-R2.T @ T2).ravel()
#     print("Camera centers (world units):", C1, C2, "baseline:", np.linalg.norm(C2 - C1))

#     # --- CSV ---
#     csv = None
#     if cfg["runtime"]["save_csv"]:
#         save_csv = os.path.normpath(cfg["runtime"]["save_csv"])
#         os.makedirs(os.path.dirname(save_csv), exist_ok=True)
#         csv = open(save_csv, "w", newline="")
#         # csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap,epi_err\n")
#         csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap,epi_err,height\n")

#     # --- Time pairing buffers ---
#     max_pair_dt = float(cfg["runtime"].get("max_pair_dt_ms", 60)) / 1000.0
#     bufL, bufR = deque(maxlen=60), deque(maxlen=60)  # (t, frame)

#     # --- Main loop ---
#     while True:
#         t_now = time.time()
#         okL, fL = capL.read()
#         okR, fR = capR.read()
#         if not okL and not okR:
#             break
#         if okL:
#             bufL.append((t_now, fL))
#         if okR:
#             bufR.append((t_now, fR))
#         if not bufL or not bufR:
#             continue

#         # Pair by closest timestamps
#         tL, frameL = bufL[-1]
#         tR, frameR = min(bufR, key=lambda p: abs(p[0] - tL))
#         if abs(tR - tL) > max_pair_dt:
#             continue
#         t0 = (tL + tR) / 2.0

#         # --- Detections ---
#         detsL = det.infer(frameL)
#         detsR = det.infer(frameR)

#         # optional tiny-box filter
#         if min_box_area > 0:
#             detsL = [
#                 (c, b, s)
#                 for (c, b, s) in detsL
#                 if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
#             ]
#             detsR = [
#                 (c, b, s)
#                 for (c, b, s) in detsR
#                 if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
#             ]

#         anchorsL = get_anchors(frameL, detsL, model=anchor_model)
#         anchorsR = get_anchors(frameR, detsR, model=anchor_model)

#         # --- Associate ---
#         pairs = []
#         nL, nR = len(detsL), len(detsR)
#         if assoc_mode == "epipolar":
#             # pairs = epipolar_pairs(detsL, detsR, F, tol=epi_tol)
#             # candidate matches from epipolar geometry
#             cand = epipolar_pairs(detsL, detsR, F, tol=epi_tol)  # returns list[(i,j)]
#             best = {}
#             for i, j in cand:
#                 uL, vL, _ = anchorsL[i]
#                 uR, vR, _ = anchorsR[j]
#                 e = _epipolar_error(F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0]))
#                 if e <= epi_tol:
#                     if (i not in best) or (e < best[i][1]):
#                         best[i] = ((i, j), e)
#             pairs = [p for (p, e) in best.values()]

#             # --- Fallback to simple nearest if epipolar found nothing ---
#             if not pairs:
#                 diag = _pair_diagnostics(detsL, detsR, ignore_class=ignore_class)
#                 if diag:
#                     min_dv, min_dist, i_min, j_min, i_dv, j_dv = diag
#                     if simple_metric == "euclidean":
#                         if min_dist <= simple_max_dist:
#                             pairs = [(i_min, j_min)]
#                     else:
#                         if min_dv <= simple_max_dv:
#                             pairs = [(i_dv, j_dv)]
#                 print(f"[assoc] epi:0  simple:{pairs if pairs else None} L={nL} R={nR}")
#             else:
#                 print(f"[assoc] epi:{pairs} L={nL} R={nR}")
#         else:
#             # diagnostics on current detections
#             diag = _pair_diagnostics(detsL, detsR, ignore_class=ignore_class)
#             if diag is None:
#                 pairs = []
#             else:
#                 min_dv, min_dist, i_min, j_min, i_dv, j_dv = diag
#                 # choose gating metric
#                 if simple_metric == "euclidean":
#                     # gate by full 2D distance
#                     if min_dist <= simple_max_dist:
#                         pairs = [(i_min, j_min)]
#                     else:
#                         pairs = []
#                 else:
#                     # gate by vertical diff
#                     if min_dv <= simple_max_dv:
#                         pairs = [(i_dv, j_dv)]
#                     else:
#                         pairs = []

#                 # force pairing path for debugging
#                 if force_pair and detsL and detsR:
#                     pairs = [(i_min, j_min)]  # ignore gates & class

#             # optional console diagnostics
#             if detsL and detsR:
#                 print(
#                     f"[assoc] L={len(detsL)} R={len(detsR)} "
#                     f"min_dv={min_dv if diag else 'NA':>6} px "
#                     f"min_euc={min_dist if diag else 'NA':>6} px "
#                     f"chosen={pairs[0] if pairs else None}"
#                 )

#         # --- For each left detection, compute 3D ---
#         for i, (clsL, boxL, confL) in enumerate(detsL):
#             uL, vL, _ = anchorsL[i]
#             CL, dL = ray_from_pixel(uL, vL, K_L, R_L, T_L)

#             Cw, mode, gap = None, "plane", np.nan
#             uR_log, vR_log, epi_err = np.nan, np.nan, np.nan

#             # Try stereo
#             pr = [p for p in pairs if p[0] == i]
#             if pr:
#                 j = pr[0][1]
#                 uR, vR, _ = anchorsR[j]
#                 CR, dR = ray_from_pixel(uR, vR, K_R, R_R, T_R)

#                 # Pw, gap = triangulate(CL, dL, CR, dR)
#                 # if Pw is not None:
#                 #     Cw = Pw
#                 #     mode = "stereo"
#                 #     uR_log, vR_log = uR, vR
#                 #     if F is not None:
#                 #         epi_err = _epipolar_error(
#                 #             F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0])
#                 #         )

#                 scale = float(cfg["runtime"].get("unit_scale_m_per_world_unit", 1.0))
#                 Pw, gap = triangulate(CL, dL, CR, dR)
#                 gap = gap * scale  # scale gap to meters

#                 if Pw is not None and gap < float(
#                     cfg["runtime"].get("max_triangulation_gap_m", 0.30)
#                 ):
#                     Cw = Pw
#                     mode = "stereo"
#                     uR_log, vR_log = uR, vR
#                     if F is not None:
#                         epi_err = _epipolar_error(
#                             F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0])
#                         )

#             # Fallback: single-view ray -> floor
#             n = planes["floor"]["n"]
#             b = planes["floor"]["b"]
#             if Cw is None:
#                 hit = intersect_plane(CL, dL, n, b)
#                 Cw = hit if hit is not None else CL + 2.0 * dL

#             # x, y, z = Cw.tolist()
#             # height = float(
#             #     height_from_plane(Cw, n, b)
#             # )  # <-- TRUE height above the floor plane

#             # if csv:
#             #     csv.write(
#             #         f"{t0:.3f},{CLASSES.get(clsL,clsL)},{confL:.2f},"
#             #         f"{uL:.1f},{vL:.1f},{uR_log if mode=='stereo' else np.nan},"
#             #         f"{vR_log if mode=='stereo' else np.nan},"
#             #         f"{x:.3f},{y:.3f},{z:.3f},{mode},{gap},{epi_err},{height:.3f}\n"
#             #     )
#             scale = float(cfg["runtime"].get("unit_scale_m_per_world_unit", 1.0))
#             x, y, z = (Cw * scale).tolist()
#             height = (
#                 float(height_from_plane(Cw, n, b)) * scale
#             )  # plane computed in world units too

#             if csv:
#                 csv.write(
#                     f"{t0:.3f},{CLASSES.get(clsL,clsL)},{confL:.2f},"
#                     f"{uL:.1f},{vL:.1f},{uR_log if mode=='stereo' else np.nan},"
#                     f"{vR_log if mode=='stereo' else np.nan},"
#                     f"{x:.3f},{y:.3f},{z:.3f},{mode},{gap},{epi_err},{height:.3f}\n"
#                 )

#         # --- OSD ---
#         if cfg["runtime"]["draw"]:
#             from .visualize import draw_det

#             visL = draw_det(
#                 frameL.copy(), detsL, [(a[0], a[1], a[2]) for a in anchorsL]
#             )
#             visR = draw_det(
#                 frameR.copy(), detsR, [(a[0], a[1], a[2]) for a in anchorsR]
#             )
#             # show quick height text from the last computed result if stereo existed
#             cv2.putText(visL, f"assoc={assoc_mode}", (10, 24), 0, 0.7, (0, 255, 255), 2)
#             cv2.putText(
#                 visR, f"conf>={det.conf:.2f}", (10, 24), 0, 0.7, (0, 255, 255), 2
#             )
#             # optional: show last computed height on the left view
#             cv2.putText(visL, "height: plane Z", (10, 48), 0, 0.6, (0, 255, 0), 2)

#             if show_indices:
#                 # label left detections
#                 for idx, (_, b, _) in enumerate(detsL):
#                     cx, cy = map(int, _box_center_xyxy(b))
#                     cv2.putText(visL, f"L{idx}", (cx, cy), 0, 0.6, (0, 255, 255), 2)
#                 # label right detections
#                 for idx, (_, b, _) in enumerate(detsR):
#                     cx, cy = map(int, _box_center_xyxy(b))
#                     cv2.putText(visR, f"R{idx}", (cx, cy), 0, 0.6, (0, 255, 255), 2)

#             # If we had at least one pair this frame, draw the chosen one
#             if "pairs" in locals() and pairs:
#                 j0 = pairs[0][1]
#                 # mark chosen centers
#                 for idx, (_, b, _) in enumerate(detsL):
#                     cx, cy = map(int, ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2))
#                     col = (0, 255, 0) if idx == pairs[0][0] else (0, 200, 200)
#                     cv2.circle(visL, (cx, cy), 4, col, -1)
#                 for idx, (_, b, _) in enumerate(detsR):
#                     cx, cy = map(int, ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2))
#                     col = (0, 255, 0) if idx == j0 else (0, 200, 200)
#                     cv2.circle(visR, (cx, cy), 4, col, -1)

#             cv2.imshow("Left", visL)
#             cv2.imshow("Right", visR)
#             if cv2.waitKey(1) & 0xFF == 27:
#                 break

#     if csv:
#         csv.close()
#     capL.release()
#     capR.release()
#     cv2.destroyAllWindows()


## 5th version after edits debugging purpose with split and 3d axes ###
# src/localize3d.py
import cv2, time, yaml, numpy as np, os
from collections import deque

from .detector import FireSmokeDetector
from .anchor_model import apply_anchor_heuristic  # (kept for future use)
from .associate import simple_nearest, fundamental_from_KRT, epipolar_pairs
from .geometry import ray_from_pixel, intersect_plane, triangulate
from .utils import load_calib, load_planes

CLASSES = {0: "fire", 1: "smoke"}  # adjust to match your model


# ---------------------- Small helpers ----------------------
def _box_center_xyxy(box):
    x1, y1, x2, y2 = box
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)


def _open_rtsp_low_latency(url: str):
    low = f"{url}?tcp&fflags=nobuffer&flags=low_delay&max_delay=1"
    cap = cv2.VideoCapture(low, cv2.CAP_FFMPEG)
    try:
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    except Exception:
        pass
    return cap


def height_from_plane(Pw, n, b):
    n = np.asarray(n, dtype=float)
    return (n @ Pw + b) / (np.linalg.norm(n) + 1e-12)


def _epipolar_error(F, pL, pR):
    lR = F @ pL  # epipolar line in right image
    return abs(lR @ pR) / (np.sqrt(lR[0] ** 2 + lR[1] ** 2) + 1e-12)


def _pair_diagnostics(detsL, detsR, ignore_class=False):
    """Return (min_dv, min_dist, i_min, j_min, i_dv, j_dv) for debug."""
    if not detsL or not detsR:
        return None
    mins = {"dv": (1e9, None, None), "dist": (1e9, None, None)}
    for i, (cL, bL, _) in enumerate(detsL):
        cxL, cyL = _box_center_xyxy(bL)
        for j, (cR, bR, _) in enumerate(detsR):
            if (not ignore_class) and (cL != cR):
                continue
            cxR, cyR = _box_center_xyxy(bR)
            dv = abs(cyR - cyL)
            d2 = (cxR - cxL) ** 2 + (cyR - cyL) ** 2
            if dv < mins["dv"][0]:
                mins["dv"] = (dv, i, j)
            if d2 < mins["dist"][0]:
                mins["dist"] = (d2, i, j)
    if mins["dist"][1] is None:
        return None
    min_dv, i_dv, j_dv = mins["dv"]
    min_dist = np.sqrt(mins["dist"][0])
    i_min, j_min = mins["dist"][1], mins["dist"][2]
    return (min_dv, min_dist, i_min, j_min, i_dv, j_dv)


def _split_canvas(imL, imR, scale=0.8, sep_px=4):
    """Create one window with LEFT | RIGHT."""
    hL, wL = imL.shape[:2]
    hR, wR = imR.shape[:2]
    H = min(hL, hR)
    if hL != H:
        imL = cv2.resize(imL, (int(wL * H / hL), H), interpolation=cv2.INTER_AREA)
    if hR != H:
        imR = cv2.resize(imR, (int(wR * H / hR), H), interpolation=cv2.INTER_AREA)
    sep = np.full((H, sep_px, 3), (40, 40, 40), np.uint8)
    canvas = np.hstack([imL, sep, imR])
    if scale != 1.0:
        canvas = cv2.resize(
            canvas, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA
        )
    return canvas


def _project_points_world(Pw, K, R, T):
    """Project 3D world points (N,3) into image using K,[R|T] (world->cam)."""
    Pw = np.asarray(Pw, dtype=float).reshape(-1, 3)  # (N,3)
    Xc = (R @ Pw.T) + T  # (3,N)
    x = (K @ Xc).T  # (N,3)
    uv = x[:, :2] / np.clip(x[:, 2:3], 1e-9, None)
    return uv


def _draw_axes_at_world_point(img, K, R, T, origin_w, axis_len_world=150.0):
    """
    Draw XYZ axes at a world point in the image.
    origin_w, axis_len_world in *world units* (mm for your ChArUco world).
    """
    O = np.asarray(origin_w, dtype=float).ravel()
    X = O + np.array([axis_len_world, 0, 0], dtype=float)
    Y = O + np.array([0, axis_len_world, 0], dtype=float)
    Z = O + np.array([0, 0, axis_len_world], dtype=float)
    pts = np.vstack([O, X, Y, Z])  # (4,3)
    uv = _project_points_world(pts, K, R, T)
    o = tuple(np.int32(uv[0]))
    # x=red, y=green, z=blue
    cv2.line(img, o, tuple(np.int32(uv[1])), (0, 0, 255), 2)
    cv2.line(img, o, tuple(np.int32(uv[2])), (0, 255, 0), 2)
    cv2.line(img, o, tuple(np.int32(uv[3])), (255, 0, 0), 2)
    cv2.circle(img, o, 3, (255, 255, 255), -1)
    return img


# ---------------------- Anchors ----------------------
def get_anchors(frame, dets, model=None, device="cpu"):
    """
    Return per-detection (u_anchor, v_anchor, q).
    Fire: bottom-center of bbox (floor contact); Smoke: top-center (origin-ish).
    """
    H, W = frame.shape[:2]
    anchors = []
    if model is None:
        for cls, box, conf in dets:
            x1, y1, x2, y2 = box
            cx = 0.5 * (x1 + x2)
            c = CLASSES.get(cls, str(cls))
            if c == "fire":
                cy = y2 - 2.0  # bottom center; keep inside frame
            else:
                cy = y1 + 2.0  # smoke heuristic
            u = float(np.clip(cx, 0, W - 1))
            v = float(np.clip(cy, 0, H - 1))
            anchors.append((u, v, float(conf)))
        return anchors
    # If you later train an AnchorNet, plug inference here.
    raise NotImplementedError("Plug in your AnchorNet inference if trained.")


# ---------------------- Main ----------------------
def localize_pair(cfg):
    # Validate paths
    for side in ("left", "right"):
        cfg[side]["calib_file"] = os.path.normpath(cfg[side]["calib_file"])
        if not os.path.isfile(cfg[side]["calib_file"]):
            raise FileNotFoundError(
                f"Calibration file missing: {cfg[side]['calib_file']}"
            )
    planes_path = os.path.normpath("configs/planes.json")
    if not os.path.isfile(planes_path):
        raise FileNotFoundError(f"Plane config missing: {planes_path}")
    weights_path = os.path.normpath(cfg["model"]["yolov10_weights"])

    # Open RTSP
    capL = _open_rtsp_low_latency(cfg["left"]["rtsp"])
    capR = _open_rtsp_low_latency(cfg["right"]["rtsp"])
    if not capL.isOpened():
        raise RuntimeError(f"Could not open Left RTSP: {cfg['left']['rtsp']}")
    if not capR.isOpened():
        raise RuntimeError(f"Could not open Right RTSP: {cfg['right']['rtsp']}")

    # Calibration & planes
    K_L, R_L, T_L, P_L = load_calib(cfg["left"]["calib_file"])
    K_R, R_R, T_R, P_R = load_calib(cfg["right"]["calib_file"])
    planes = load_planes(planes_path)

    # Detector
    det = FireSmokeDetector(weights_path, conf=float(cfg["model"].get("conf", 0.15)))
    anchor_model = None

    # Association
    assoc_mode = cfg["runtime"].get("assoc_mode", "simple").lower()
    F = (
        fundamental_from_KRT(K_L, R_L, T_L, K_R, R_R, T_R)
        if assoc_mode == "epipolar"
        else None
    )
    epi_tol = float(cfg["runtime"].get("epipolar_tol_px", 3.5))
    ignore_class = bool(cfg["runtime"].get("ignore_class", True))
    simple_metric = cfg["runtime"].get("simple_metric", "euclidean")  # or "v"
    simple_max_dv = int(cfg["runtime"].get("simple_max_dv", 160))
    simple_max_dist = float(cfg["runtime"].get("simple_max_dist", 260.0))
    force_pair = assoc_mode == "force"
    min_box_area = float(cfg["runtime"].get("min_box_area_px", 80))

    # Draw options
    draw = bool(cfg["runtime"].get("draw", True))
    draw_axes = bool(cfg["runtime"].get("draw_axes", True))
    axis_len_world = float(cfg["runtime"].get("axis_len_world", 150.0))  # mm
    split_scale = float(cfg["runtime"].get("split_scale", 0.8))
    show_indices = bool(cfg["runtime"].get("show_indices", True))
    draw_world_axes = bool(cfg["runtime"].get("draw_world_axes", True))
    world_axes_every_n = int(
        cfg["runtime"].get("world_axes_every_n", 20)
    )  # draw occasionally

    # Unit scale (mm->m for CSV logging)
    scale_m = float(cfg["runtime"].get("unit_scale_m_per_world_unit", 1.0))
    max_pair_dt = float(cfg["runtime"].get("max_pair_dt_ms", 150)) / 1000.0
    max_tr_gap_m = float(cfg["runtime"].get("max_triangulation_gap_m", 0.30))

    # Camera centers (debug)
    C1 = (-R_L.T @ T_L).ravel()
    C2 = (-R_R.T @ T_R).ravel()
    print("Camera centers (world units):", C1, C2, "baseline:", np.linalg.norm(C2 - C1))

    # CSV
    csv = None
    if cfg["runtime"]["save_csv"]:
        save_csv = os.path.normpath(cfg["runtime"]["save_csv"])
        os.makedirs(os.path.dirname(save_csv), exist_ok=True)
        csv = open(save_csv, "w", newline="")
        csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap,epi_err,height,pair_src\n")

    # Time pairing buffers
    bufL, bufR = deque(maxlen=60), deque(maxlen=60)

    frame_count = 0
    last_world_point = None  # for drawing axes even if only one detection this frame

    while True:
        t_now = time.time()
        okL, fL = capL.read()
        okR, fR = capR.read()
        if not okL and not okR:
            break
        if okL:
            bufL.append((t_now, fL))
        if okR:
            bufR.append((t_now, fR))
        if not bufL or not bufR:
            continue

        # Pair by closest timestamps
        tL, frameL = bufL[-1]
        tR, frameR = min(bufR, key=lambda p: abs(p[0] - tL))
        if abs(tR - tL) > max_pair_dt:
            continue
        t0 = 0.5 * (tL + tR)

        # Detections
        detsL = det.infer(frameL)
        detsR = det.infer(frameR)
        if min_box_area > 0:
            detsL = [
                (c, b, s)
                for (c, b, s) in detsL
                if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
            ]
            detsR = [
                (c, b, s)
                for (c, b, s) in detsR
                if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
            ]

        anchorsL = get_anchors(frameL, detsL, model=anchor_model)
        anchorsR = get_anchors(frameR, detsR, model=anchor_model)

        # Associate (with fallback)
        pairs = []
        pair_src = "none"
        nL, nR = len(detsL), len(detsR)
        if nL and nR:
            if assoc_mode == "epipolar":
                cand = epipolar_pairs(detsL, detsR, F, tol=epi_tol)  # [(i,j)]
                best = {}
                for i, j in cand:
                    uL, vL, _ = anchorsL[i]
                    uR, vR, _ = anchorsR[j]
                    e = _epipolar_error(
                        F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0])
                    )
                    if e <= epi_tol:
                        if (i not in best) or (e < best[i][1]):
                            best[i] = ((i, j), e)
                pairs = [p for (p, e) in best.values()]
                if pairs:
                    pair_src = "epi"
                    print(f"[assoc] epi:{pairs} L={nL} R={nR}")
                else:
                    # fallback
                    diag = _pair_diagnostics(detsL, detsR, ignore_class=ignore_class)
                    if diag:
                        min_dv, min_dist, i_min, j_min, i_dv, j_dv = diag
                        if simple_metric == "euclidean":
                            if min_dist <= simple_max_dist:
                                pairs = [(i_min, j_min)]
                        else:
                            if min_dv <= simple_max_dv:
                                pairs = [(i_dv, j_dv)]
                    pair_src = "simple" if pairs else "none"
                    print(
                        f"[assoc] epi:0  simple:{pairs if pairs else None} L={nL} R={nR}"
                    )
            else:
                # simple/force
                diag = _pair_diagnostics(detsL, detsR, ignore_class=ignore_class)
                if diag:
                    min_dv, min_dist, i_min, j_min, i_dv, j_dv = diag
                    if simple_metric == "euclidean":
                        if min_dist <= simple_max_dist:
                            pairs = [(i_min, j_min)]
                    else:
                        if min_dv <= simple_max_dv:
                            pairs = [(i_dv, j_dv)]
                    if force_pair:
                        pairs = [(i_min, j_min)]
                pair_src = "simple" if pairs else "none"
                if detsL and detsR:
                    print(f"[assoc] simple:{pairs if pairs else None} L={nL} R={nR}")

        # For each left detection, compute 3D
        # (We’ll draw axes for the first computed 3D point this frame)
        world_point_drawn = False
        for i, (clsL, boxL, confL) in enumerate(detsL):
            uL, vL, _ = anchorsL[i]
            CL, dL = ray_from_pixel(uL, vL, K_L, R_L, T_L)

            Cw, mode, gap_m = None, "plane", np.nan
            uR_log = np.nan
            vR_log = np.nan
            epi_err = np.nan

            # stereo if paired
            pr = [p for p in pairs if p[0] == i]
            if pr:
                j = pr[0][1]
                uR, vR, _ = anchorsR[j]
                CR, dR = ray_from_pixel(uR, vR, K_R, R_R, T_R)

                Pw, gap_world = triangulate(CL, dL, CR, dR)  # gap in world units (mm)
                gap_m = gap_world * scale_m  # compare/log in meters
                if Pw is not None and gap_m < max_tr_gap_m:
                    Cw = Pw
                    mode = "stereo"
                    uR_log, vR_log = uR, vR
                    if pair_src == "epi":
                        epi_err = _epipolar_error(
                            F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0])
                        )

            # Fallback: ray->floor plane
            n = planes["floor"]["n"]
            b = planes["floor"]["b"]
            if Cw is None:
                hit = intersect_plane(CL, dL, n, b)
                Cw = hit if hit is not None else CL + 2.0 * dL

            # Save unscaled world point for drawing (mm)
            Cw_world = Cw.copy()
            last_world_point = Cw_world

            # Log in meters
            x, y, z = (Cw * scale_m).tolist()
            height = float(height_from_plane(Cw, n, b)) * scale_m

            if csv:
                csv.write(
                    f"{t0:.3f},{CLASSES.get(clsL,clsL)},{confL:.2f},"
                    f"{uL:.1f},{vL:.1f},{uR_log if mode=='stereo' else np.nan},"
                    f"{vR_log if mode=='stereo' else np.nan},"
                    f"{x:.3f},{y:.3f},{z:.3f},{mode},{gap_m},{epi_err},{height:.3f},{pair_src}\n"
                )

            # Draw: we’ll place the 3D axis once per frame (at the first 3D point)
            if draw and not world_point_drawn and draw_axes:
                try:
                    # Draw gizmo at the 3D point in both views
                    _draw_axes_at_world_point(
                        frameL, K_L, R_L, T_L, Cw_world, axis_len_world=axis_len_world
                    )
                    _draw_axes_at_world_point(
                        frameR, K_R, R_R, T_R, Cw_world, axis_len_world=axis_len_world
                    )
                    world_point_drawn = True
                except Exception:
                    pass

        # Compose and display
        if draw:
            from .visualize import draw_det

            visL = draw_det(
                frameL.copy(), detsL, [(a[0], a[1], a[2]) for a in anchorsL]
            )
            visR = draw_det(
                frameR.copy(), detsR, [(a[0], a[1], a[2]) for a in anchorsR]
            )

            # Add status text
            cv2.putText(visL, f"assoc={assoc_mode}", (10, 24), 0, 0.7, (0, 255, 255), 2)
            cv2.putText(
                visR, f"conf>={det.conf:.2f}", (10, 24), 0, 0.7, (0, 255, 255), 2
            )

            # If we logged something this frame, show last height/gap
            if last_world_point is not None:
                # compute height again for OSD (cheap)
                n = planes["floor"]["n"]
                b = planes["floor"]["b"]
                h_osd = float(height_from_plane(last_world_point, n, b)) * scale_m
                cv2.putText(
                    visL, f"height={h_osd:.3f} m", (10, 48), 0, 0.7, (0, 255, 0), 2
                )

            # Index overlays + pair highlights
            if show_indices:
                for idx, (_, b, _) in enumerate(detsL):
                    cx, cy = map(int, _box_center_xyxy(b))
                    cv2.putText(visL, f"L{idx}", (cx, cy), 0, 0.6, (0, 255, 255), 2)
                for idx, (_, b, _) in enumerate(detsR):
                    cx, cy = map(int, _box_center_xyxy(b))
                    cv2.putText(visR, f"R{idx}", (cx, cy), 0, 0.6, (0, 255, 255), 2)
            if "pairs" in locals() and pairs:
                i0, j0 = pairs[0]
                for idx, (_, b, _) in enumerate(detsL):
                    cx, cy = map(int, _box_center_xyxy(b))
                    col = (0, 255, 0) if idx == i0 else (0, 200, 200)
                    cv2.circle(visL, (cx, cy), 4, col, -1)
                for idx, (_, b, _) in enumerate(detsR):
                    cx, cy = map(int, _box_center_xyxy(b))
                    col = (0, 255, 0) if idx == j0 else (0, 200, 200)
                    cv2.circle(visR, (cx, cy), 4, col, -1)

            # Draw world origin axes occasionally (to verify world frame)
            # World origin is the ChArUco board origin from your shared-pose calibration.
            if draw_world_axes and (frame_count % world_axes_every_n == 0):
                try:
                    origin = np.array(
                        [0.0, 0.0, 0.0], dtype=float
                    )  # world (board) origin
                    _draw_axes_at_world_point(
                        visL, K_L, R_L, T_L, origin, axis_len_world=axis_len_world
                    )
                    _draw_axes_at_world_point(
                        visR, K_R, R_R, T_R, origin, axis_len_world=axis_len_world
                    )
                except Exception:
                    pass

            # Single split window
            canvas = _split_canvas(visL, visR, scale=split_scale, sep_px=4)
            cv2.imshow("PyroLoc3D (Left | Right)", canvas)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        frame_count += 1

    if csv:
        csv.close()
    capL.release()
    capR.release()
    cv2.destroyAllWindows()


# ### 6th version after edits debugging purpose with split and 3d axes v1 ###
# # src/localize3d.py
# import cv2, time, yaml, numpy as np, os
# from collections import deque

# from .detector import FireSmokeDetector
# from .associate import simple_nearest, fundamental_from_KRT, epipolar_pairs
# from .geometry import ray_from_pixel, intersect_plane, triangulate
# from .utils import load_calib, load_planes

# CLASSES = {0: "fire", 1: "smoke"}  # adjust to match your model


# # ---------- helpers ----------
# def _box_center_xyxy(box):
#     x1, y1, x2, y2 = box
#     return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)


# def _open_rtsp_low_latency(url: str):
#     low = f"{url}?tcp&fflags=nobuffer&flags=low_delay&max_delay=1"
#     cap = cv2.VideoCapture(low, cv2.CAP_FFMPEG)
#     try:
#         cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
#     except Exception:
#         pass
#     return cap


# def height_from_plane(Pw, n, b):
#     n = np.asarray(n, dtype=float)
#     return (n @ Pw + b) / (np.linalg.norm(n) + 1e-12)


# def _epipolar_error(F, pL, pR):
#     lR = F @ pL
#     return abs(lR @ pR) / (np.sqrt(lR[0] ** 2 + lR[1] ** 2) + 1e-12)


# def _split_canvas(imL, imR, scale=0.8, sep_px=4):
#     hL, wL = imL.shape[:2]
#     hR, wR = imR.shape[:2]
#     H = min(hL, hR)
#     if hL != H:
#         imL = cv2.resize(imL, (int(wL * H / hL), H), interpolation=cv2.INTER_AREA)
#     if hR != H:
#         imR = cv2.resize(imR, (int(wR * H / hR), H), interpolation=cv2.INTER_AREA)
#     sep = np.full((H, sep_px, 3), (40, 40, 40), np.uint8)
#     canvas = np.hstack([imL, sep, imR])
#     if scale != 1.0:
#         canvas = cv2.resize(
#             canvas, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA
#         )
#     return canvas


# def _project_points_world(Pw, K, R, T):
#     Pw = np.asarray(Pw, dtype=float).reshape(-1, 3)  # (N,3)
#     Xc = (R @ Pw.T) + T  # (3,N)
#     x = (K @ Xc).T  # (N,3)
#     uv = x[:, :2] / np.clip(x[:, 2:3], 1e-9, None)
#     return uv


# def _draw_axes_at_world_point(img, K, R, T, origin_w, axis_len_world=150.0, label=""):
#     """
#     Draw XYZ axes at a world point in the image. origin_w, axis length in world units.
#     """
#     O = np.asarray(origin_w, dtype=float).ravel()
#     X = O + np.array([axis_len_world, 0, 0], dtype=float)
#     Y = O + np.array([0, axis_len_world, 0], dtype=float)
#     Z = O + np.array([0, 0, axis_len_world], dtype=float)

#     pts = np.vstack([O, X, Y, Z])  # (4,3)
#     uv = _project_points_world(pts, K, R, T)
#     o = tuple(np.int32(uv[0]))

#     # lines
#     cv2.line(img, o, tuple(np.int32(uv[1])), (0, 0, 255), 3)  # X red
#     cv2.line(img, o, tuple(np.int32(uv[2])), (0, 255, 0), 3)  # Y green
#     cv2.line(img, o, tuple(np.int32(uv[3])), (255, 0, 0), 3)  # Z blue
#     cv2.circle(img, o, 4, (255, 255, 255), -1)

#     # labels
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(
#         img, "X", tuple(np.int32(uv[1]) + 2), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA
#     )
#     cv2.putText(
#         img, "Y", tuple(np.int32(uv[2]) + 2), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA
#     )
#     cv2.putText(
#         img, "Z", tuple(np.int32(uv[3]) + 2), font, 0.6, (255, 0, 0), 2, cv2.LINE_AA
#     )
#     if label:
#         cv2.putText(
#             img, label, (o[0] + 8, o[1] - 6), font, 0.6, (220, 220, 220), 2, cv2.LINE_AA
#         )
#     return img


# # ---------- anchors (bottom/top center) ----------
# def get_anchors(frame, dets):
#     """Return per-detection (u_anchor, v_anchor, q). Fire=bottom-center, Smoke=top-center."""
#     H, W = frame.shape[:2]
#     anchors = []
#     for cls, box, conf in dets:
#         x1, y1, x2, y2 = box
#         cx = 0.5 * (x1 + x2)
#         c = CLASSES.get(cls, str(cls))
#         cy = (y2 - 2.0) if c == "fire" else (y1 + 2.0)
#         u = float(np.clip(cx, 0, W - 1))
#         v = float(np.clip(cy, 0, H - 1))
#         anchors.append((u, v, float(conf)))
#     return anchors


# # ---------- main ----------
# def localize_pair(cfg):
#     # validate paths
#     for side in ("left", "right"):
#         cfg[side]["calib_file"] = os.path.normpath(cfg[side]["calib_file"])
#         if not os.path.isfile(cfg[side]["calib_file"]):
#             raise FileNotFoundError(
#                 f"Calibration file missing: {cfg[side]['calib_file']}"
#             )
#     planes_path = os.path.normpath("configs/planes.json")
#     if not os.path.isfile(planes_path):
#         raise FileNotFoundError(f"Plane config missing: {planes_path}")
#     weights_path = os.path.normpath(cfg["model"]["yolov10_weights"])

#     # open RTSP
#     capL = _open_rtsp_low_latency(cfg["left"]["rtsp"])
#     capR = _open_rtsp_low_latency(cfg["right"]["rtsp"])
#     if not capL.isOpened():
#         raise RuntimeError(f"Could not open Left RTSP: {cfg['left']['rtsp']}")
#     if not capR.isOpened():
#         raise RuntimeError(f"Could not open Right RTSP: {cfg['right']['rtsp']}")

#     # calib & planes
#     K_L, R_L, T_L, _ = load_calib(cfg["left"]["calib_file"])
#     K_R, R_R, T_R, _ = load_calib(cfg["right"]["calib_file"])
#     planes = load_planes(planes_path)

#     # detector
#     det = FireSmokeDetector(weights_path, conf=float(cfg["model"].get("conf", 0.15)))

#     # association
#     assoc_mode = cfg["runtime"].get("assoc_mode", "epipolar").lower()
#     F = (
#         fundamental_from_KRT(K_L, R_L, T_L, K_R, R_R, T_R)
#         if assoc_mode == "epipolar"
#         else None
#     )
#     epi_tol = float(cfg["runtime"].get("epipolar_tol_px", 3.5))
#     ignore_class = bool(cfg["runtime"].get("ignore_class", True))
#     simple_metric = cfg["runtime"].get("simple_metric", "euclidean")
#     simple_max_dv = int(cfg["runtime"].get("simple_max_dv", 160))
#     simple_max_dist = float(cfg["runtime"].get("simple_max_dist", 260.0))
#     force_pair = assoc_mode == "force"
#     min_box_area = float(cfg["runtime"].get("min_box_area_px", 80))

#     # draw options
#     draw = bool(cfg["runtime"].get("draw", True))
#     draw_axes = bool(cfg["runtime"].get("draw_axes", True))
#     axis_len_world = float(cfg["runtime"].get("axis_len_world", 200.0))  # mm
#     split_scale = float(cfg["runtime"].get("split_scale", 0.8))
#     show_indices = bool(cfg["runtime"].get("show_indices", True))
#     draw_world_axes = bool(cfg["runtime"].get("draw_world_axes", True))
#     world_axes_every_n = int(cfg["runtime"].get("world_axes_every_n", 1))  # always
#     world_origin_world = np.array(
#         cfg["runtime"].get("world_origin_world", [0.0, 0.0, 0.0]), dtype=float
#     )

#     # units & timing
#     scale_m = float(cfg["runtime"].get("unit_scale_m_per_world_unit", 1.0))
#     max_pair_dt = float(cfg["runtime"].get("max_pair_dt_ms", 150)) / 1000.0
#     max_tr_gap_m = float(cfg["runtime"].get("max_triangulation_gap_m", 0.30))

#     # debug baseline
#     C1 = (-R_L.T @ T_L).ravel()
#     C2 = (-R_R.T @ T_R).ravel()
#     print("Camera centers (world units):", C1, C2, "baseline:", np.linalg.norm(C2 - C1))

#     # csv
#     csv = None
#     if cfg["runtime"]["save_csv"]:
#         save_csv = os.path.normpath(cfg["runtime"]["save_csv"])
#         os.makedirs(os.path.dirname(save_csv), exist_ok=True)
#         csv = open(save_csv, "w", newline="")
#         csv.write("t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap,epi_err,height,pair_src\n")

#     # buffers
#     bufL, bufR = deque(maxlen=60), deque(maxlen=60)
#     frame_count = 0
#     last_world_point = None

#     while True:
#         t_now = time.time()
#         okL, fL = capL.read()
#         okR, fR = capR.read()
#         if not okL and not okR:
#             break
#         if okL:
#             bufL.append((t_now, fL))
#         if okR:
#             bufR.append((t_now, fR))
#         if not bufL or not bufR:
#             continue

#         # pair newest frames
#         tL, frameL = bufL[-1]
#         tR, frameR = min(bufR, key=lambda p: abs(p[0] - tL))
#         if abs(tR - tL) > max_pair_dt:
#             continue
#         t0 = 0.5 * (tL + tR)

#         # detections
#         detsL = det.infer(frameL)
#         detsR = det.infer(frameR)
#         if min_box_area > 0:
#             detsL = [
#                 (c, b, s)
#                 for (c, b, s) in detsL
#                 if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
#             ]
#             detsR = [
#                 (c, b, s)
#                 for (c, b, s) in detsR
#                 if (b[2] - b[0]) * (b[3] - b[1]) >= min_box_area
#             ]
#         anchorsL = get_anchors(frameL, detsL)
#         anchorsR = get_anchors(frameR, detsR)

#         # associate
#         pairs = []
#         pair_src = "none"
#         nL, nR = len(detsL), len(detsR)
#         if nL and nR:
#             if assoc_mode == "epipolar":
#                 cand = epipolar_pairs(detsL, detsR, F, tol=epi_tol)
#                 best = {}
#                 for i, j in cand:
#                     uL, vL, _ = anchorsL[i]
#                     uR, vR, _ = anchorsR[j]
#                     e = _epipolar_error(
#                         F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0])
#                     )
#                     if e <= epi_tol:
#                         if (i not in best) or (e < best[i][1]):
#                             best[i] = ((i, j), e)
#                 pairs = [p for (p, e) in best.values()]
#                 if not pairs:
#                     # fallback
#                     diag = _pair_diagnostics(detsL, detsR, ignore_class=ignore_class)
#                     if diag:
#                         min_dv, min_dist, i_min, j_min, i_dv, j_dv = diag
#                         if simple_metric == "euclidean":
#                             if min_dist <= simple_max_dist:
#                                 pairs = [(i_min, j_min)]
#                         else:
#                             if min_dv <= simple_max_dv:
#                                 pairs = [(i_dv, j_dv)]
#                     pair_src = "simple" if pairs else "none"
#                     print(
#                         f"[assoc] epi:0  simple:{pairs if pairs else None} L={nL} R={nR}"
#                     )
#                 else:
#                     pair_src = "epipolar"
#                     print(f"[assoc] epi:{pairs} L={nL} R={nR}")
#             else:
#                 diag = _pair_diagnostics(detsL, detsR, ignore_class=ignore_class)
#                 if diag:
#                     min_dv, min_dist, i_min, j_min, i_dv, j_dv = diag
#                     if simple_metric == "euclidean":
#                         if min_dist <= simple_max_dist:
#                             pairs = [(i_min, j_min)]
#                     else:
#                         if min_dv <= simple_max_dv:
#                             pairs = [(i_dv, j_dv)]
#                     if force_pair:
#                         pairs = [(i_min, j_min)]
#                 pair_src = "simple" if pairs else "none"

#         # 3D for each left detection
#         world_point_drawn = False
#         for i, (clsL, boxL, confL) in enumerate(detsL):
#             uL, vL, _ = anchorsL[i]
#             CL, dL = ray_from_pixel(uL, vL, K_L, R_L, T_L)

#             Cw, mode, gap_m = None, "plane", np.nan
#             uR_log = vR_log = np.nan
#             epi_err = np.nan

#             pr = [p for p in pairs if p[0] == i]
#             if pr:
#                 j = pr[0][1]
#                 uR, vR, _ = anchorsR[j]
#                 CR, dR = ray_from_pixel(uR, vR, K_R, R_R, T_R)
#                 Pw, gap_world = triangulate(CL, dL, CR, dR)
#                 gap_m = gap_world * scale_m
#                 if Pw is not None and gap_m < max_tr_gap_m:
#                     Cw = Pw
#                     mode = "stereo"
#                     uR_log, vR_log = uR, vR
#                     if pair_src == "epipolar":
#                         epi_err = _epipolar_error(
#                             F, np.array([uL, vL, 1.0]), np.array([uR, vR, 1.0])
#                         )

#             n = planes["floor"]["n"]
#             b = planes["floor"]["b"]
#             if Cw is None:
#                 hit = intersect_plane(CL, dL, n, b)
#                 Cw = hit if hit is not None else CL + 2.0 * dL

#             # keep for drawing in world units (mm)
#             last_world_point = Cw.copy()

#             # log in meters
#             x, y, z = (Cw * scale_m).tolist()
#             height = float(height_from_plane(Cw, n, b)) * scale_m
#             if csv:
#                 csv.write(
#                     f"{t0:.3f},{CLASSES.get(clsL,clsL)},{confL:.2f},"
#                     f"{uL:.1f},{vL:.1f},{uR_log if mode=='stereo' else np.nan},"
#                     f"{vR_log if mode=='stereo' else np.nan},"
#                     f"{x:.3f},{y:.3f},{z:.3f},{mode},{gap_m},{epi_err},{height:.3f},{pair_src}\n"
#                 )

#             # draw local axes at detection point (both views)
#             if draw and not world_point_drawn and draw_axes:
#                 try:
#                     _draw_axes_at_world_point(
#                         frameL, K_L, R_L, T_L, Cw, axis_len_world=axis_len_world
#                     )
#                     _draw_axes_at_world_point(
#                         frameR, K_R, R_R, T_R, Cw, axis_len_world=axis_len_world
#                     )
#                     world_point_drawn = True
#                 except Exception:
#                     pass

#         # compose display
#         if draw:
#             # add status & height readout
#             if last_world_point is not None:
#                 n = planes["floor"]["n"]
#                 b = planes["floor"]["b"]
#                 h_osd = float(height_from_plane(last_world_point, n, b)) * scale_m
#                 cv2.putText(
#                     frameL, f"assoc={assoc_mode}", (10, 24), 0, 0.7, (0, 255, 255), 2
#                 )
#                 cv2.putText(
#                     frameL, f"height={h_osd:+.3f} m", (10, 48), 0, 0.7, (0, 255, 0), 2
#                 )
#                 cv2.putText(
#                     frameR, f"conf>={det.conf:.2f}", (10, 24), 0, 0.7, (0, 255, 255), 2
#                 )

#             # draw world origin axes ALWAYS (0,0,0 by default)
#             if draw_world_axes and (frame_count % world_axes_every_n == 0):
#                 try:
#                     _draw_axes_at_world_point(
#                         frameL,
#                         K_L,
#                         R_L,
#                         T_L,
#                         world_origin_world,
#                         axis_len_world=axis_len_world,
#                         label="World origin",
#                     )
#                     _draw_axes_at_world_point(
#                         frameR,
#                         K_R,
#                         R_R,
#                         T_R,
#                         world_origin_world,
#                         axis_len_world=axis_len_world,
#                         label="World origin",
#                     )
#                 except Exception:
#                     pass

#             # single split window
#             canvas = _split_canvas(frameL, frameR, scale=split_scale, sep_px=4)
#             cv2.imshow("PyroLoc3D (Left | Right)", canvas)
#             if cv2.waitKey(1) & 0xFF == 27:
#                 break

#         frame_count += 1

#     if csv:
#         csv.close()
#     capL.release()
#     capR.release()
#     cv2.destroyAllWindows()


# # ---------- simple pairing diagnostics ----------
# def _pair_diagnostics(detsL, detsR, ignore_class=False):
#     if not detsL or not detsR:
#         return None
#     mins = {"dv": (1e9, None, None), "dist": (1e9, None, None)}
#     for i, (cL, bL, _) in enumerate(detsL):
#         cxL, cyL = _box_center_xyxy(bL)
#         for j, (cR, bR, _) in enumerate(detsR):
#             if (not ignore_class) and (cL != cR):
#                 continue
#             cxR, cyR = _box_center_xyxy(bR)
#             dv = abs(cyR - cyL)
#             d2 = (cxR - cxL) ** 2 + (cyR - cyL) ** 2
#             if dv < mins["dv"][0]:
#                 mins["dv"] = (dv, i, j)
#             if d2 < mins["dist"][0]:
#                 mins["dist"] = (d2, i, j)
#     if mins["dist"][1] is None:
#         return None
#     min_dv, i_dv, j_dv = mins["dv"]
#     min_dist = np.sqrt(mins["dist"][0])
#     i_min, j_min = mins["dist"][1], mins["dist"][2]
#     return (min_dv, min_dist, i_min, j_min, i_dv, j_dv)
