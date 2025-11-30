### Script to generate figures and tables for Chapter 6 assets

# ######################### Section 6.1 - 6.4: Figures #########################
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from matplotlib.patches import Rectangle, FancyBboxPatch
# from zipfile import ZipFile, ZIP_DEFLATED
# import os


# def save(fig, stem):
#     png = f"{stem}.png"
#     svg = f"{stem}.svg"
#     fig.savefig(png, dpi=240, bbox_inches="tight")
#     fig.savefig(svg, bbox_inches="tight")
#     plt.close(fig)
#     return png, svg


# # ---------- Figure 6.1: System overview ----------
# fig, ax = plt.subplots(figsize=(10, 3))
# ax.axis("off")


# def rbox(ax, xy, w, h, text):
#     box = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02", linewidth=1)
#     ax.add_patch(box)
#     ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center")


# x0, y0, w, h, dx = 0.02, 0.2, 0.18, 0.6, 0.195
# labels = [
#     "Acquisition\n(RTSP)",
#     "YOLOv10\nDetections",
#     "AnchorNet\n(Δu,Δv,q)",
#     "Association\n(Epipolar)",
#     "3D Geometry\n(Triangulation\n+ Floor)",
#     "Stability &\nVisualization\n+ CSV Log",
# ]
# for i, lab in enumerate(labels):
#     rbox(ax, (x0 + i * dx, y0), w, h, lab)
#     if i > 0:
#         ax.annotate(
#             "",
#             xy=(x0 + i * dx - 0.01, 0.5),
#             xytext=(x0 + (i - 1) * dx + w + 0.01, 0.5),
#             arrowprops=dict(arrowstyle="->", lw=1),
#         )
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# f61 = save(fig, "fig6_1_system_overview")

# # ---------- Figure 6.2: World frame + baseline + origin axes ----------
# fig, ax = plt.subplots(figsize=(8, 5))
# ax.set_aspect("equal")
# ax.axis("off")

# # Floor rectangle (Z=0 in the model; we illustrate it in 2D top view)
# ax.add_patch(Rectangle((0, 0), 6, 4, fill=False, linewidth=1))
# ax.text(0.1, 3.8, "Floor plane (Z=0)")

# # World origin and axes (schematic)
# origin = np.array([1, 1])
# ax.plot([origin[0], origin[0] + 1.2], [origin[1], origin[1]], lw=2)  # X
# ax.plot([origin[0], origin[0]], [origin[1], origin[1] + 1.2], lw=2)  # Y
# ax.plot([origin[0], origin[0] + 0.8], [origin[1], origin[1] + 0.8], lw=2)  # Z (diag)
# ax.text(origin[0] + 1.25, origin[1] - 0.1, "X")
# ax.text(origin[0] - 0.1, origin[1] + 1.25, "Y")
# ax.text(origin[0] + 0.85, origin[1] + 0.85, "Z")


# def camera(ax, center, look_at, label):
#     c = np.array(center)
#     l = np.array(look_at)
#     d = l - c
#     d = d / (np.linalg.norm(d) + 1e-9)
#     left = np.array([-d[1], d[0]])
#     p1 = c + 0.2 * left
#     p2 = c - 0.2 * left
#     p3 = c + 0.6 * d
#     ax.plot([p1[0], p2[0], p3[0], p1[0]], [p1[1], p2[1], p3[1], p1[1]], lw=1)
#     ax.text(c[0] - 0.15, c[1] - 0.25, label)


# C_L = np.array([1.2, 0.6])
# C_R = np.array([4.8, 0.9])
# camera(ax, C_L, np.array([3.0, 2.0]), "Left cam")
# camera(ax, C_R, np.array([3.0, 2.0]), "Right cam")
# ax.plot([C_L[0], C_R[0]], [C_L[1], C_R[1]], lw=1)
# ax.text(3.0, 0.9, "baseline")

# X = np.array([3.0, 2.0])  # example fire base
# ax.plot([C_L[0], X[0]], [C_L[1], X[1]], lw=1, linestyle="--")
# ax.plot([C_R[0], X[0]], [C_R[1], X[1]], lw=1, linestyle="--")
# ax.scatter([X[0]], [X[1]], s=20)
# ax.text(X[0] + 0.05, X[1] + 0.05, "fire base")

# ax.set_xlim(-0.1, 6.2)
# ax.set_ylim(-0.1, 4.3)
# f62 = save(fig, "fig6_2_world_frame_baseline")

# # ---------- Figure 6.3: Latency-aware pairing timeline ----------
# fig, ax = plt.subplots(figsize=(10, 2.8))
# ax.axis("off")
# ax.hlines(0.8, 0, 10, lw=1)
# ax.hlines(0.3, 0, 10, lw=1)
# ax.text(-0.2, 0.8, "Left", va="center")
# ax.text(-0.2, 0.3, "Right", va="center")

# left_times = [1, 2, 3, 4, 5, 6, 7]
# right_times = [0.9, 2.15, 3.1, 4.6, 5.05, 6.9]


# def frame_box(y, t, txt):
#     ax.add_patch(Rectangle((t - 0.15, y - 0.1), 0.3, 0.2, fill=False, lw=1))
#     ax.text(t, y, txt, ha="center", va="center", fontsize=8)


# for i, t in enumerate(left_times):
#     frame_box(0.8, t, f"L{i}")
# for j, t in enumerate(right_times):
#     frame_box(0.3, t, f"R{j}")

# tau = 0.2
# for i, tL in enumerate(left_times):
#     j = int(np.argmin([abs(tR - tL) for tR in right_times]))
#     tR = right_times[j]
#     if abs(tR - tL) <= tau:
#         ax.annotate(
#             "", xy=(tR, 0.42), xytext=(tL, 0.68), arrowprops=dict(arrowstyle="->", lw=1)
#         )
#         ax.text((tL + tR) / 2, 0.55, "|Δt|≤τ", ha="center", fontsize=8)
#     else:
#         ax.annotate(
#             "",
#             xy=(tR, 0.42),
#             xytext=(tL, 0.68),
#             arrowprops=dict(arrowstyle="->", lw=1, linestyle="--"),
#         )
#         ax.text((tL + tR) / 2, 0.9, "rejected", ha="center", fontsize=8)
# ax.text(6.5, 1.0, "Gate τₜ = 0.2 s", fontsize=9)
# f63 = save(fig, "fig6_3_latency_pairing")

# # ---------- Figure 6.4: Triangulation & ray-gap ----------
# fig, ax = plt.subplots(figsize=(6, 4))
# ax.set_aspect("equal")
# ax.axis("off")
# CL = np.array([0.5, 0.3])
# CR = np.array([5.5, 0.5])
# ax.scatter([CL[0], CR[0]], [CL[1], CR[1]])
# ax.text(CL[0] - 0.2, CL[1] - 0.2, "C_L")
# ax.text(CR[0] + 0.05, CR[1] - 0.2, "C_R")
# X1 = np.array([3.1, 2.4])
# X2 = np.array([3.3, 2.0])
# ax.plot([CL[0], X1[0]], [CL[1], X1[1]], linestyle="--")
# ax.plot([CR[0], X2[0]], [CR[1], X2[1]], linestyle="--")
# M = (X1 + X2) / 2
# ax.scatter([M[0]], [M[1]])
# ax.text(M[0] + 0.05, M[1] + 0.05, "midpoint")
# ax.plot([X1[0], X2[0]], [X1[1], X2[1]], lw=1)
# ax.text(2.2, 2.3, "ray-gap", fontsize=9)
# ax.set_xlim(0, 6)
# ax.set_ylim(0, 3.5)
# f64 = save(fig, "fig6_4_triangulation_gap")

# # ---------- Tables ----------
# notation = pd.DataFrame(
#     [
#         ["K", "3×3 camera intrinsic matrix"],
#         ["R, T", "Rotation and translation (world→camera)"],
#         ["C", "Camera center = -RᵀT (world units)"],
#         ["F", "Fundamental matrix between the two views"],
#         ["(u,v)", "Pixel coordinates (column, row)"],
#         ["Δu, Δv", "AnchorNet 2D offset within the detection box"],
#         ["q", "AnchorNet confidence for the predicted anchor"],
#         ["p_out", "Probability anchor lies outside the box"],
#         ["d", "Unit ray direction in world coordinates"],
#         ["gap", "Shortest distance between the two rays (meters)"],
#         ["h", "Height above the calibrated floor plane (meters)"],
#     ],
#     columns=["Symbol", "Meaning"],
# )
# notation_csv = "table6_1_notation.csv"
# notation.to_csv(notation_csv, index=False)

# hardware = pd.DataFrame(
#     [
#         ["Cameras", "2× Dahua indoor Wi-Fi (3MP)"],
#         ["Lens", "Fixed focus (factory)"],
#         [
#             "Calibration target",
#             "ChArUco 7×5; 30 mm squares; 15 mm markers; DICT_5X5_100",
#         ],
#         ["Compute host", "Laptop/Workstation (CPU; optional GPU)"],
#         ["Network", "Single LAN/Wi-Fi (RTSP/H.264)"],
#     ],
#     columns=["Component", "Specification"],
# )
# hardware_csv = "table6_2_hardware.csv"
# hardware.to_csv(hardware_csv, index=False)

# params = pd.DataFrame(
#     [
#         ["assoc_mode", "epipolar", "Association mode: epipolar | simple | force"],
#         ["epipolar_tol_px", "2", "Max distance to epipolar line (px)"],
#         ["max_triangulation_gap_m", "0.30", "Ray-gap acceptance threshold (m)"],
#         ["unit_scale_m_per_world_unit", "0.001", "World→meters scale (mm board)"],
#         ["max_pair_dt_ms", "60", "Max time skew for pairing (ms)"],
#         ["min_box_area_px", "200", "Min detection area to enter pipeline"],
#         ["q_min", "0.3", "AnchorNet quality threshold"],
#         ["p_out_th", "0.5", "Out-of-box probability threshold"],
#     ],
#     columns=["Parameter", "Default", "Description"],
# )
# params_csv = "table6_3_params.csv"
# params.to_csv(params_csv, index=False)

# # ---------- Zip everything ----------
# zip_path = "ch6_figs_tables.zip"
# with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as z:
#     for p in [*f61, *f62, *f63, *f64, notation_csv, hardware_csv, params_csv]:
#         z.write(p, arcname=os.path.basename(p))

# print(
#     "Done. Wrote:",
#     *f61,
#     *f62,
#     *f63,
#     *f64,
#     notation_csv,
#     hardware_csv,
#     params_csv,
#     zip_path,
#     sep="\n",
# )


## ######################### Section 6.5 #########################
# # make_ch6_perception_figs.py
# # Generates all Perception Stack figures (Matplotlib only, single-axes per figure).

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle, Polygon


# def save_fig(path):
#     plt.savefig(path, dpi=240, bbox_inches="tight")
#     plt.close()


# # ---------- Fig 6.5.1: Perception pipeline ----------
# fig = plt.figure(figsize=(9, 3.8))
# ax = plt.gca()
# ax.axis("off")


# def box(ax, x, y, w, h, label, fontsize=9):
#     ax.add_patch(Rectangle((x, y), w, h, fill=False, linewidth=1.5))
#     ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=fontsize)


# def arrow(ax, x1, y1, x2, y2):
#     ax.annotate(
#         "", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", lw=1.3)
#     )


# y0 = 0.55
# h = 0.2
# w = 0.22
# pad = 0.04
# x0 = 0.04
# box(ax, x0, y0, w, h, "RTSP Frame\n(low-latency)")
# arrow(ax, x0 + w, y0 + h / 2, x0 + w + pad, y0 + h / 2)
# box(ax, x0 + w + pad, y0, w, h, "YOLOv10 Detector\n(bboxes, scores)")
# arrow(ax, x0 + 2 * w + pad, y0 + h / 2, x0 + 2 * w + 2 * pad, y0 + h / 2)
# box(ax, x0 + 2 * w + 2 * pad, y0, w, h, "ROI Builder\n(padded crops)")
# arrow(ax, x0 + 3 * w + 2 * pad, y0 + h / 2, x0 + 3 * w + 3 * pad, y0 + h / 2)
# box(
#     ax,
#     x0 + 3 * w + 3 * pad,
#     y0,
#     w,
#     h,
#     "AnchorNet\n($\\hat{\\Delta u},\\hat{\\Delta v},q,p_{out}$)",
# )
# # Heuristic branch
# y1 = 0.15
# box(ax, x0 + 2 * w + 2 * pad, y1, w, h, "Heuristic Anchor\n(class-aware)")
# gate_x = x0 + 3 * w + 2.5 * pad
# gate_y = 0.36
# gd = 0.05
# ax.add_patch(
#     Polygon(
#         [
#             [gate_x, gate_y + gd],
#             [gate_x + gd, gate_y],
#             [gate_x, gate_y - gd],
#             [gate_x - gd, gate_y],
#         ],
#         closed=True,
#         fill=False,
#         linewidth=1.5,
#     )
# )
# ax.text(gate_x, gate_y, "Gate", ha="center", va="center", fontsize=9)
# arrow(ax, x0 + 3 * w + 3 * pad + w / 2, y0, gate_x, gate_y + gd)
# arrow(ax, x0 + 2 * w + 2 * pad + w / 2, y1 + h, gate_x, gate_y - gd)
# box(ax, x0 + 4 * w + 3.8 * pad, y0, w, h, "Fused Anchor\n+ reliability")
# arrow(ax, gate_x + gd, gate_y, x0 + 4 * w + 3.8 * pad, y0 + h / 2)
# box(ax, x0 + 5 * w + 4.8 * pad, y0, w, h, "Association\n(Epipolar + fallback)")
# arrow(
#     ax,
#     x0 + 5 * w + 4.8 * pad + w,
#     y0 + h / 2,
#     x0 + 5 * w + 5.8 * pad + 0.02,
#     y0 + h / 2,
# )
# box(
#     ax,
#     x0 + 6 * w + 5.8 * pad,
#     y0,
#     w,
#     h,
#     "Geometry\n(Rays, Triangulation,\nPlane Intersection)",
# )
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# save_fig("fig_perception_pipeline.png")

# # ---------- Fig 6.5.2: Anchor semantics ----------
# fig = plt.figure(figsize=(8, 4.2))
# ax = plt.gca()
# ax.axis("off")
# ax.text(0.18, 0.92, "Fire anchor = flame base", ha="center", va="center", fontsize=10)
# ax.add_patch(Rectangle((0.06, 0.28), 0.24, 0.5, fill=False, linewidth=1.5))
# ax.plot([0.18], [0.30], "o")
# ax.text(0.18, 0.24, "anchor", ha="center", va="center", fontsize=9)
# ax.plot([0.05, 0.31], [0.25, 0.25], lw=1.2)
# ax.text(0.06, 0.22, "floor plane", fontsize=8)
# ax.text(
#     0.72, 0.92, "Smoke anchor = emission origin", ha="center", va="center", fontsize=10
# )
# ax.add_patch(Rectangle((0.58, 0.28), 0.24, 0.5, fill=False, linewidth=1.5))
# ax.plot([0.70], [0.44], "o")
# ax.text(0.70, 0.40, "anchor", ha="center", va="center", fontsize=9)
# ax.text(
#     0.18,
#     0.12,
#     "Within bbox, near bottom edge\n(vertical snap by local gradients)",
#     ha="center",
#     va="center",
#     fontsize=9,
# )
# ax.text(
#     0.70,
#     0.12,
#     "Lower half/third; whiteness emergence\n(H,S,V heuristic)",
#     ha="center",
#     va="center",
#     fontsize=9,
# )
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# save_fig("fig_anchor_semantics.png")

# # ---------- Fig 6.5.3: AnchorNet architecture ----------
# fig = plt.figure(figsize=(7.5, 4.5))
# ax = plt.gca()
# ax.axis("off")
# ax.text(0.08, 0.5, "128×128 ROI", fontsize=10, ha="center", va="center")
# x = 0.16
# y = 0.35
# w = 0.12
# h = 0.30
# dx = 0.14
# for i, lbl in enumerate(["Conv×5\n(strided, BN, ReLU)\n→ 8×8×128", "GAP", "FC 128"]):
#     ax.add_patch(Rectangle((x + i * dx, y), w, h, fill=False, linewidth=1.5))
#     ax.text(x + i * dx + w / 2, y + h / 2, lbl, ha="center", va="center", fontsize=9)
#     if i > 0:
#         ax.annotate(
#             "",
#             xy=(x + i * dx, y + h / 2),
#             xytext=(x + (i - 1) * dx + w, y + h / 2),
#             arrowprops=dict(arrowstyle="->", lw=1.3),
#         )
# hx = x + 3 * dx + 0.02
# hw = 0.14
# hh = 0.18
# hy = [0.62, 0.41, 0.20]
# for yi, lbl in zip(
#     hy,
#     [
#         "Offsets (du,dv)\n(tanh→[-0.5,0.5])",
#         "Quality q\n(sigmoid)",
#         "Out-of-box p_out\n(sigmoid)",
#     ],
# ):
#     ax.add_patch(Rectangle((hx, yi - hh / 2), hw, hh, fill=False, linewidth=1.5))
#     ax.text(hx + hw / 2, yi, lbl, ha="center", va="center", fontsize=9)
#     ax.annotate(
#         "",
#         xy=(hx, yi),
#         xytext=(x + 2 * dx + w, y + h / 2),
#         arrowprops=dict(arrowstyle="->", lw=1.3),
#     )
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# save_fig("fig_anchornet_arch.png")

# # ---------- Fig 6.5.4: Fire pseudo-label ----------
# fig = plt.figure(figsize=(6.5, 4.0))
# ax = plt.gca()
# ax.axis("off")
# bx = 0.18
# by = 0.20
# bw = 0.45
# bh = 0.60
# ax.add_patch(Rectangle((bx, by), bw, bh, fill=False, linewidth=1.5))
# ax.text(0.08, 0.88, "Fire pseudo-label", fontsize=10)
# cx = bx + bw / 2
# ys = np.linspace(by + 0.05, by + 0.25, 18)
# ax.plot([cx] * len(ys), ys, ".", ms=4)
# ax.plot([cx], [by + 0.22], "o", ms=6)
# ax.text(cx, by + 0.16, "max gradient/brightness", ha="center", fontsize=9)
# ax.text(
#     0.50,
#     0.05,
#     "Start at bottom-center → scan vertical band → pick max score",
#     ha="center",
#     fontsize=9,
# )
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# save_fig("fig_pseudolabel_fire.png")

# # ---------- Fig 6.5.5: Smoke pseudo-label ----------
# fig = plt.figure(figsize=(6.5, 4.0))
# ax = plt.gca()
# ax.axis("off")
# bx = 0.18
# by = 0.20
# bw = 0.45
# bh = 0.60
# ax.add_patch(Rectangle((bx, by), bw, bh, fill=False, linewidth=1.5))
# ax.text(0.08, 0.88, "Smoke pseudo-label", fontsize=10)
# nx, ny = 80, 120
# X, Y = np.meshgrid(np.linspace(0, 1, nx), np.linspace(0, 1, ny))
# Z = np.exp(-((Y - 0.6) ** 2) / 0.03) * np.exp(-((X - 0.5) ** 2) / 0.12)
# pts_u = bx + bw * X.flatten()
# pts_v = by + bh * Y.flatten()
# idx = slice(0, pts_u.size, 20)
# ax.scatter(pts_u[idx], pts_v[idx], s=(Z.flatten()[idx] * 25 + 1))
# ax.plot([bx + bw * 0.5], [by + bh * 0.55], "o", ms=6)
# ax.text(
#     bx + bw * 0.5,
#     by + bh * 0.49,
#     "whitest/low-S high-V\n(lower half)",
#     ha="center",
#     fontsize=9,
# )
# ax.text(
#     0.50,
#     0.05,
#     "Search lower half/third → whiteness proxy → pick emission origin",
#     ha="center",
#     fontsize=9,
# )
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# save_fig("fig_pseudolabel_smoke.png")

# # ---------- Fig 6.5.6: Gating & fusion ----------
# fig = plt.figure(figsize=(8.2, 4.6))
# ax = plt.gca()
# ax.axis("off")


# def rbox(ax, x, y, w, h, text):
#     ax.add_patch(Rectangle((x, y), w, h, fill=False, linewidth=1.5))
#     ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9)


# def diamond(ax, xc, yc, w, h, text):
#     ax.add_patch(
#         Polygon(
#             [[xc, yc + h / 2], [xc + w / 2, yc], [xc, yc - h / 2], [xc - w / 2, yc]],
#             closed=True,
#             fill=False,
#             linewidth=1.5,
#         )
#     )
#     ax.text(xc, yc, text, ha="center", va="center", fontsize=9)


# rbox(ax, 0.05, 0.42, 0.18, 0.16, "YOLO box + ROI\nper detection")
# ax.annotate(
#     "", xy=(0.26, 0.50), xytext=(0.23, 0.50), arrowprops=dict(arrowstyle="->", lw=1.3)
# )
# rbox(ax, 0.26, 0.42, 0.22, 0.16, "AnchorNet\n(du,dv,q,p_out)")
# ax.annotate(
#     "", xy=(0.53, 0.50), xytext=(0.48, 0.50), arrowprops=dict(arrowstyle="->", lw=1.3)
# )
# diamond(ax, 0.56, 0.50, 0.12, 0.18, "p_out<th\nand\nanchor in box?")
# ax.annotate(
#     "", xy=(0.68, 0.62), xytext=(0.62, 0.53), arrowprops=dict(arrowstyle="->", lw=1.3)
# )
# rbox(ax, 0.68, 0.54, 0.22, 0.16, "Use AnchorNet anchor\nΣ from q")
# ax.annotate(
#     "", xy=(0.68, 0.34), xytext=(0.62, 0.47), arrowprops=dict(arrowstyle="->", lw=1.3)
# )
# rbox(ax, 0.68, 0.26, 0.22, 0.16, "Heuristic anchor\n(class-aware)")
# ax.annotate(
#     "", xy=(0.93, 0.50), xytext=(0.90, 0.58), arrowprops=dict(arrowstyle="->", lw=1.3)
# )
# ax.annotate(
#     "", xy=(0.93, 0.50), xytext=(0.90, 0.34), arrowprops=dict(arrowstyle="->", lw=1.3)
# )
# rbox(ax, 0.93, 0.42, 0.22, 0.16, "Fused anchor →\nAssociation & Geometry")
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# save_fig("fig_anchor_gating_flow.png")

# # ---------- Fig 6.5.7: Temporal smoothing ----------
# np.random.seed(7)
# t = np.arange(0, 4 * np.pi, 0.15)
# y = np.sin(t) + 0.25 * np.random.randn(len(t))
# alpha = 0.3
# ys = []
# s = y[0]
# for v in y:
#     s = alpha * v + (1 - alpha) * s
#     ys.append(s)
# ys = np.array(ys)
# fig = plt.figure(figsize=(6.8, 3.4))
# ax = plt.gca()
# ax.plot(t, y, label="raw anchor v(t)")
# ax.plot(t, ys, label="EMA-smoothed v(t)")
# ax.set_xlabel("time (frames)")
# ax.set_ylabel("pixel coordinate")
# ax.legend()
# save_fig("fig_temporal_smoothing.png")

# print("DONE: generated figs in current folder.")

######################### Section 6.6 #########################
# make_ch6_assets.py
# Generates figures (PNG + SVG) and CSV tables for Section 6.6: Cross-View Association.
# Matplotlib only (one plot per figure). No seaborn. No custom colors.

# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

# ASSETS_DIR = os.path.join(".", "assets", "ch6")
# os.makedirs(ASSETS_DIR, exist_ok=True)


# # ---------------- Figure 6.6.1: Epipolar geometry schematic ----------------
# def fig_6_6_1():
#     fig = plt.figure(figsize=(10, 4))
#     ax = plt.gca()
#     ax.set_xlim(0, 10)
#     ax.set_ylim(0, 4)
#     ax.axis("off")

#     # Left / Right image planes
#     ax.add_patch(Rectangle((0.5, 0.5), 4, 3, fill=False, linewidth=2))
#     ax.add_patch(Rectangle((5.5, 0.5), 4, 3, fill=False, linewidth=2))

#     # Left anchor (pixel)
#     pL = (2.5, 2.2)
#     ax.add_patch(Circle(pL, 0.06))
#     # Fixed: Changed \tilde{u} to \~{u} to avoid \t conflict
#     ax.text(pL[0] + 0.1, pL[1] + 0.1, r"$\~{u}_L$", fontsize=10)

#     # Epipolar line (right image)
#     x_line = np.linspace(5.5, 9.5, 100)
#     m, c = -0.4, 5.0
#     ax.plot(x_line, m * x_line + c, linewidth=2)

#     # Two right candidates
#     cand1 = (7.1, m * 7.1 + c)  # on/near line
#     cand2 = (8.5, m * 8.5 + c + 0.4)  # slightly off

#     # Fixed: Changed \tilde{u} to \~{u} to avoid \t conflict
#     for (x, y), label in [
#         (cand1, r"$\~{u}_{R,1}$"),
#         (cand2, r"$\~{u}_{R,2}$"),
#     ]:
#         ax.add_patch(Circle((x, y), 0.06))
#         ax.text(x + 0.1, y + 0.1, label, fontsize=10)

#     # Arrow hinting “pixel → line correspondence”
#     ax.add_patch(
#         FancyArrowPatch(
#             (4.5, 2.2), (5.5, m * 5.5 + c), arrowstyle="->", mutation_scale=12
#         )
#     )

#     ax.set_title(
#         "Epipolar geometry: left pixel induces an epipolar line on the right image"
#     )
#     for ext in ("png", "svg"):
#         plt.savefig(
#             os.path.join(ASSETS_DIR, f"fig_6_6_1_epipolar_geometry.{ext}"),
#             dpi=200,
#             bbox_inches="tight",
#         )
#     plt.close()


# # -------- Figure 6.6.2: Pixel–line distance tolerance (epi residual) -------
# def fig_6_6_2():
#     fig = plt.figure(figsize=(5, 4))
#     ax = plt.gca()
#     ax.set_xlim(0, 4)
#     ax.set_ylim(0, 3)
#     ax.axis("off")
#     # Fixed: Changed \le to \leq to avoid \l conflict
#     ax.set_title(r"Pixel–line distance tolerance ($d_{epi} \leq \tau_{epi}$)")

#     # Right image box
#     ax.add_patch(Rectangle((0.2, 0.2), 3.6, 2.6, fill=False, linewidth=2))

#     # Epipolar line
#     x = np.linspace(0.2, 3.8, 100)
#     m, c = -0.7, 2.6
#     y = m * x + c
#     ax.plot(x, y, linewidth=2)

#     def perp_proj(px, py, m, c):
#         # line y = m x + c -> Ax + By + C = 0 with A=m, B=-1, C=c
#         A, B, C = m, -1.0, c
#         denom = A * A + B * B
#         x0 = (B * (B * px - A * py) - A * C) / denom
#         y0 = (A * (-B * px + A * py) - B * C) / denom
#         return x0, y0

#     candA = (1.1, m * 1.1 + c + 0.05)  # inside tolerance
#     candB = (2.8, m * 2.8 + c + 0.35)  # outside tolerance

#     for (px, py), label in [(candA, "in"), (candB, "out")]:
#         ax.add_patch(Circle((px, py), 0.06))
#         qx, qy = perp_proj(px, py, m, c)
#         ax.plot([px, qx], [py, qy], linestyle="--")
#         ax.text(px + 0.08, py + 0.08, label, fontsize=10)

#     # Visual tolerance band (parallel lines)
#     offset = 0.2
#     band_c = offset * np.sqrt(1 + m * m)
#     ax.plot(x, m * x + (c + band_c), linestyle=":")
#     ax.plot(x, m * x + (c - band_c), linestyle=":")

#     for ext in ("png", "svg"):
#         plt.savefig(
#             os.path.join(ASSETS_DIR, f"fig_6_6_2_epi_tolerance.{ext}"),
#             dpi=200,
#             bbox_inches="tight",
#         )
#     plt.close()


# # ---------------- Figure 6.6.3: Association pipeline flowchart -------------
# def fig_6_6_3():
#     fig = plt.figure(figsize=(10, 4))
#     ax = plt.gca()
#     ax.axis("off")
#     ax.set_xlim(0, 10)
#     ax.set_ylim(0, 4)

#     def box(x, y, w, h, text):
#         ax.add_patch(Rectangle((x, y), w, h, fill=False, linewidth=2))
#         ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=10)

#     def arrow(x1, y1, x2, y2):
#         ax.add_patch(
#             FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="->", mutation_scale=12)
#         )

#     box(0.4, 2.3, 2.2, 1.0, "Detections\n(Left/Right)")
#     arrow(2.6, 2.8, 3.3, 2.8)
#     # Fixed: Changed to raw string r"..." and \le to \leq
#     box(3.3, 2.3, 2.2, 1.0, r"Epipolar gating\n($d_{epi} \leq \tau_{epi}$)")
#     arrow(5.5, 2.8, 6.2, 2.8)
#     box(6.2, 2.3, 2.2, 1.0, "Tie-break\n(q, conf, area, history)")
#     arrow(8.4, 2.8, 9.2, 2.8)
#     ax.text(9.2, 2.8, "Pairs", va="center", fontsize=10)

#     arrow(4.4, 2.3, 4.4, 1.3)
#     box(3.3, 0.3, 2.2, 1.0, "Fallback: simple nearest\n(dv / d2, gates)")
#     arrow(5.5, 0.8, 6.2, 0.8)
#     box(6.2, 0.3, 2.2, 1.0, "Tie-break\n(q, conf, area, history)")
#     arrow(8.4, 0.8, 9.2, 0.8)
#     ax.text(9.2, 0.8, "Pairs", va="center", fontsize=10)

#     ax.set_title("Cross-view association pipeline")

#     for ext in ("png", "svg"):
#         plt.savefig(
#             os.path.join(ASSETS_DIR, f"fig_6_6_3_association_flow.{ext}"),
#             dpi=200,
#             bbox_inches="tight",
#         )
#     plt.close()


# # ----------- Figure 6.6.4: Epipolar residuals (time series) ---------------
# def fig_6_6_4():
#     np.random.seed(1)
#     frames = np.arange(1, 121)
#     residuals = 1.2 + 0.3 * np.sin(frames / 8.0) + 0.25 * np.random.randn(len(frames))
#     residuals[::17] += 1.6
#     tau_epi = 2.0

#     plt.figure(figsize=(10, 3.5))
#     plt.plot(frames, residuals, linewidth=2)
#     plt.axhline(tau_epi, linestyle="--")
#     plt.xlabel("Frame")
#     plt.ylabel("Symmetric epipolar distance (px)")
#     plt.title("Epipolar residuals with tolerance line")

#     for ext in ("png", "svg"):
#         plt.savefig(
#             os.path.join(ASSETS_DIR, f"fig_6_6_4_epi_residuals_timeseries.{ext}"),
#             dpi=200,
#             bbox_inches="tight",
#         )
#     plt.close()


# # --------------- Figure 6.6.5: Tie-break demo (bar chart) -----------------
# def fig_6_6_5():
#     cands = ["j=2", "j=5", "j=7"]
#     epi = np.array([0.6, 0.9, 1.4])  # px
#     dv = np.array([40, 22, 18])  # px
#     d2 = np.array([120, 80, 95])  # px
#     conf_prod = np.array([0.65, 0.78, 0.55])  # higher=better (bonus)

#     def norm01(x):
#         a, b = np.min(x), np.max(x)
#         return (x - a) / (b - a + 1e-9)

#     score = 0.6 * norm01(epi) + 0.2 * norm01(dv) + 0.2 * norm01(d2) - 0.2 * conf_prod

#     plt.figure(figsize=(7, 4))
#     plt.bar(cands, score)
#     plt.ylabel("Composite tie-break cost (lower is better)")
#     plt.title("Tie-break comparison across candidates")

#     for ext in ("png", "svg"):
#         # Fixed: Corrected inconsistent filename
#         plt.savefig(
#             os.path.join(ASSETS_DIR, f"fig_6_6_5_tiebreak_scores.{ext}"),
#             dpi=200,
#             bbox_inches="tight",
#         )
#     plt.close()


# # ------------------------------ Tables (CSVs) ---------------------------
# def save_tables():
#     # Fixed: Renamed variables for 6.6 consistency
#     # Table 6.6.1 — Association thresholds
#     t6_6_1 = pd.DataFrame(
#         [
#             {
#                 "Key": "epi_tol_px",
#                 "Meaning": "Symmetric pixel-to-line tolerance",
#                 "Recommended": "1.5–2.5 px",
#             },
#             {
#                 "Key": "simple_max_dv",
#                 "Meaning": "Vertical gap gate (fallback)",
#                 "Recommended": "80–160 px",
#             },
#             {
#                 "Key": "simple_max_dist",
#                 "Meaning": "Euclidean gate (fallback)",
#                 "Recommended": "180–320 px",
#             },
#             {
#                 "Key": "ignore_class",
#                 "Meaning": "Allow cross-class pairing (robustness)",
#                 "Recommended": "false (true in heavy smoke)",
#             },
#             {
#                 "Key": "history_len",
#                 "Meaning": "Frames to prefer previous mate",
#                 "Recommended": "5–10",
#             },
#         ]
#     )
#     t6_6_1.to_csv(
#         os.path.join(ASSETS_DIR, "table_6_6_1_assoc_thresholds.csv"), index=False
#     )

#     # Table 6.6.2 — Tie-break features & weights
#     t6_6_2 = pd.DataFrame(
#         [
#             {
#                 "Feature": "Symmetric epipolar distance",
#                 "Symbol": "d_epi",
#                 "Weight": "0.6",
#                 "Role": "primary (lower better)",
#             },
#             {
#                 "Feature": "Vertical gap",
#                 "Symbol": "d_v",
#                 "Weight": "0.2",
#                 "Role": "secondary penalty",
#             },
#             {
#                 "Feature": "Euclidean gap",
#                 "Symbol": "d_2",
#                 "Weight": "0.2",
#                 "Role": "secondary penalty",
#             },
#             {
#                 "Feature": "Confidence product",
#                 "Symbol": "conf_L·conf_R",
#                 "Weight": "-0.2",
#                 "Role": "bonus (higher better)",
#             },
#             {
#                 "Feature": "Area similarity",
#                 "Symbol": "|log(A_L/A_R)|",
#                 "Weight": "0.1",
#                 "Role": "weak penalty",
#             },
#             {
#                 "Feature": "Anchor quality sum",
#                 "Symbol": "q_L+q_R",
#                 "Weight": "-0.1",
#                 "Role": "bonus (higher better)",
#             },
#         ]
#     )
#     t6_6_2.to_csv(
#         os.path.join(ASSETS_DIR, "table_6_6_2_tiebreak_weights.csv"), index=False
#     )

#     # Table 6.6.3 — Failure cases & fallbacks
#     t6_6_3 = pd.DataFrame(
#         [
#             {
#                 "Failure / Symptom": "No epipolar candidates",
#                 "Likely cause": "Desync / packet loss / weak anchors",
#                 "Fallback": "Simple nearest (dv/d2) with gates",
#                 "Extra action": "Lower q_min, increase α_track, widen gates slightly",
#             },
#             {
#                 "Failure / Symptom": "Many ties on epipolar line",
#                 "Likely cause": "Multiple similar plumes along epipolar",
#                 "Fallback": "Tie-break with conf, area, history",
#                 "Extra action": "Enable Hungarian assignment if dense",
#             },
#             {
#                 "Failure / Symptom": "Drifting associations over time",
#                 "Likely cause": "Unstable anchors or glare",
#                 "Fallback": "History preference (hysteresis)",
#                 "Extra action": "Stronger temporal smoothing; raise q_min",
#             },
#             {
#                 "Failure / Symptom": "Systematic epipolar residual > τ",
#                 "Likely cause": "Miscalibration / moved camera",
#                 "Fallback": "Temporary fallback to simple",
#                 "Extra action": "Trigger re-calibration / sanity checks (§13)",
#             },
#         ]
#     )
#     t6_6_3.to_csv(
#         os.path.join(ASSETS_DIR, "table_6_6_3_failures_fallbacks.csv"), index=False
#     )

#     # Table 6.6.4 — Complexity per frame
#     t6_6_4 = pd.DataFrame(
#         [
#             {
#                 "Stage": "Epipolar distance eval",
#                 "Operation": "O(N_L·N_R)",
#                 "Comment": "Two dot-products per candidate + normalization",
#             },
#             {
#                 "Stage": "Tie-break per left",
#                 "Operation": "O(k)",
#                 "Comment": "k candidates after gating; small in practice",
#             },
#             {
#                 "Stage": "Fallback nearest",
#                 "Operation": "O(N_L·N_R)",
#                 "Comment": "Only when epipolar returns no candidates",
#             },
#             {
#                 "Stage": "Optional Hungarian",
#                 "Operation": "O(n^3)",
#                 "Comment": "Use when many objects; n=min(N_L, N_R)",
#             },
#         ]
#     )
#     t6_6_4.to_csv(os.path.join(ASSETS_DIR, "table_6_6_4_complexity.csv"), index=False)

#     # Table 6_6_5 — Diagnostics logged
#     t6_6_5 = pd.DataFrame(
#         [
#             {
#                 "Field": "t",
#                 "Units": "s (epoch)",
#                 "Meaning": "Mid-timestamp of paired frames",
#             },
#             {
#                 "Field": "nL, nR",
#                 "Units": "count",
#                 "Meaning": "Detections per view in the frame",
#             },
#             {
#                 "Field": "mode",
#                 "Units": "{epi|simple}",
#                 "Meaning": "Association path used",
#             },
#             {
#                 "Field": "i*, j*",
#                 "Units": "index",
#                 "Meaning": "Chosen left/right indices",
#             },
#             {
#                 "Field": "d_epi_sym",
#                 "Units": "px",
#                 "Meaning": "Symmetric epipolar distance for pair",
#             },
#             {
#                 "Field": "d_v, d_2",
#                 "Units": "px",
#                 "Meaning": "Vertical and Euclidean gaps (fallback)",
#             },
#             {
#                 "Field": "conf_L, conf_R",
#                 "Units": "[0,1]",
#                 "Meaning": "Detector confidences for the pair",
#             },
#             {
#                 "Field": "q_L, q_R",
#                 "Units": "[0,1]",
#                 "Meaning": "Anchor quality heads (if available)",
#             },
#         ]
#     )
#     t6_6_5.to_csv(os.path.join(ASSETS_DIR, "table_6_6_5_diagnostics.csv"), index=False)

#     # Fixed: Return renamed variable keys
#     return {
#         "table_6_6_1": "table_6_6_1_assoc_thresholds.csv",
#         "table_6_6_2": "table_6_6_2_tiebreak_weights.csv",
#         "table_6_6_3": "table_6_6_3_failures_fallbacks.csv",
#         "table_6_6_4": "table_6_6_4_complexity.csv",
#         "table_6_6_5": "table_6_6_5_diagnostics.csv",
#     }


# def main():
#     # Fixed: Call renamed functions
#     fig_6_6_1()
#     fig_6_6_2()
#     fig_6_6_3()
#     fig_6_6_4()
#     fig_6_6_5()
#     table_paths = save_tables()

#     print("\nSaved to:", os.path.abspath(ASSETS_DIR))
#     print("Figures:")
#     # Fixed: Corrected list to match saved filenames
#     for stem in [
#         "fig_6_6_1_epipolar_geometry",
#         "fig_6_6_2_epi_tolerance",
#         "fig_6_6_3_association_flow",
#         "fig_6_6_4_epi_residuals_timeseries",
#         "fig_6_6_5_tiebreak_scores",
#     ]:
#         print(f"  {stem}.png")
#         print(f"  {stem}.svg")
#     print("Tables (CSV):")
#     for k, v in table_paths.items():
#         print(" ", v)


# if __name__ == "__main__":
#     main()


## ######################### Section 6.7 #########################
# Generates figures (PNG + SVG) and CSV tables for Section 6.7: 3D Localization Geometry.
# import numpy as np, pandas as pd, matplotlib.pyplot as plt
# from pathlib import Path

# outdir = Path("assets")
# outdir.mkdir(parents=True, exist_ok=True)

# # ---- Fig 6.7.1: Ray casting
# fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot(111, projection="3d")
# C = np.array([0.0, 0.0, 0.0])
# d = np.array([0.2, 0.1, 1.0])
# d = d / np.linalg.norm(d)
# t = np.linspace(0, 5, 50)
# ray = C[None, :] + t[:, None] * d[None, :]
# ax.plot(ray[:, 0], ray[:, 1], ray[:, 2], linewidth=2)
# ax.scatter([0], [0], [0], s=40)
# z_plane = 1.0
# xs = np.array([-0.6, 0.6, 0.6, -0.6, -0.6])
# ys = np.array([-0.4, -0.4, 0.4, 0.4, -0.4])
# zs = np.full_like(xs, z_plane)
# ax.plot(xs, ys, zs, linewidth=1.5)
# u, v = 0.1, 0.05
# anchor = np.array([u, v, 1.0])
# anchor_line = np.vstack([C, C + 4.5 * (anchor / np.linalg.norm(anchor))])
# ax.plot(anchor_line[:, 0], anchor_line[:, 1], anchor_line[:, 2], linestyle="--")
# ax.scatter([anchor[0]], [anchor[1]], [anchor[2]])
# ax.text(0, 0, 0, "C")
# ax.text(anchor[0], anchor[1], anchor[2], "(u,v,1)")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# ax.set_title("Ray casting from pixel to world ray")
# ax.view_init(elev=18, azim=-60)
# plt.tight_layout()
# plt.savefig(outdir / "fig_6_7_1_ray_casting.png", dpi=160)
# plt.close(fig)

# # ---- Fig 6.7.2: Triangulation & gap
# fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot(111, projection="3d")
# C1 = np.array([-0.5, 0, 0])
# C2 = np.array([0.5, 0, 0])
# d1 = np.array([0.2, 0.05, 1.0])
# d1 /= np.linalg.norm(d1)
# d2 = np.array([-0.1, -0.02, 1.0])
# d2 /= np.linalg.norm(d2)
# t = np.linspace(0, 6, 50)
# ray1 = C1 + t[:, None] * d1
# ray2 = C2 + t[:, None] * d2
# r = C2 - C1
# b = float(np.dot(d1, d2))
# den = max(1e-9, (1 - b * b))
# t_star = (np.dot(r, d1) - np.dot(r, d2) * b) / den
# s_star = (np.dot(r, d1) * b - np.dot(r, d2)) / den
# P1 = C1 + t_star * d1
# P2 = C2 + s_star * d2
# Xhat = 0.5 * (P1 + P2)
# gap = np.linalg.norm(P1 - P2)
# ax.plot(ray1[:, 0], ray1[:, 1], ray1[:, 2], linewidth=2)
# ax.plot(ray2[:, 0], ray2[:, 1], ray2[:, 2], linewidth=2)
# ax.scatter([C1[0]], [C1[1]], [C1[2]], s=40)
# ax.scatter([C2[0]], [C2[1]], [C2[2]], s=40)
# ax.plot([P1[0], P2[0]], [P1[1], P2[1]], [P1[2], P2[2]], linewidth=3)
# ax.scatter([Xhat[0]], [Xhat[1]], [Xhat[2]], s=40)
# ax.text(*C1, "C1")
# ax.text(*C2, "C2")
# ax.text(*Xhat, "X̂")
# ax.text(*P1, "P1")
# ax.text(*P2, "P2")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# ax.set_title(f"Stereo triangulation; gap = {gap:.2f} (units)")
# ax.view_init(elev=20, azim=-55)
# plt.tight_layout()
# plt.savefig(outdir / "fig_6_7_2_triangulation_gap.png", dpi=160)
# plt.close(fig)

# # ---- Fig 6.7.3: Ray–floor intersection
# fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot(111, projection="3d")
# C = np.array([0.0, 0.5, 0.5])
# d = np.array([0.1, -0.2, -1.0])
# d /= np.linalg.norm(d)
# t = np.linspace(0, 3, 50)
# ray = C + t[:, None] * d
# xx, yy = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
# zz = np.zeros_like(xx)
# n = np.array([0, 0, 1])
# b = 0.0
# den = float(np.dot(n, d))
# lam = -(np.dot(n, C) + b) / (den if abs(den) > 1e-9 else 1e-9)
# X = C + lam * d
# ax.plot_surface(xx, yy, zz, alpha=0.2)
# ax.plot(ray[:, 0], ray[:, 1], ray[:, 2], linewidth=2)
# ax.scatter([C[0]], [C[1]], [C[2]], s=40)
# ax.scatter([X[0]], [X[1]], [X[2]], s=40)
# ax.text(*C, "C")
# ax.text(*X, "X (floor hit)")
# ax.text(-0.9, -0.9, 0.02, "Floor plane")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# ax.set_title("Single-view fallback: ray–floor intersection")
# ax.view_init(elev=25, azim=-50)
# plt.tight_layout()
# plt.savefig(outdir / "fig_6_7_3_ray_floor.png", dpi=160)
# plt.close(fig)

# # ---- Fig 8.4: Height to plane
# fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot(111, projection="3d")
# xx, yy = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
# zz = np.zeros_like(xx)
# ax.plot_surface(xx, yy, zz, alpha=0.2)
# X = np.array([0.3, -0.2, 0.6])
# Xp = np.array([X[0], X[1], 0.0])
# h = X[2]
# ax.scatter([X[0]], [X[1]], [X[2]], s=40)
# ax.plot([X[0], Xp[0]], [X[1], Xp[1]], [X[2], Xp[2]], linewidth=3)
# ax.scatter([Xp[0]], [Xp[1]], [Xp[2]], s=30)
# ax.text(*X, "X")
# ax.text(*Xp, "π(X)")
# ax.text(-0.9, -0.9, 0.02, "Floor plane")
# ax.text(0.05, 0.05, 0.5, f"h = {h:.2f} m")
# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")
# ax.set_title("Height as signed distance to floor plane")
# ax.view_init(elev=25, azim=-50)
# plt.tight_layout()
# plt.savefig(outdir / "fig_6_7_4_height.png", dpi=160)
# plt.close(fig)

# # ---- Tables -> CSV
# tab_6_7_1 = pd.DataFrame(
#     {
#         "Symbol": ["K", "R", "T", "C", "d", "Π: n,b", "X̂", "g", "τ_gap", "s"],
#         "Meaning": [
#             "Camera intrinsics (3×3)",
#             "Rotation (world→cam)",
#             "Translation (world→cam)",
#             "Camera center in world (−RᵀT)",
#             "Unit ray direction in world",
#             "Floor plane (nᵀx + b = 0)",
#             "Estimated 3D point",
#             "Shortest segment length between rays",
#             "Gap acceptance threshold",
#             "Unit scale (e.g., 1e−3 for mm→m)",
#         ],
#         "Default/Notes": [
#             "fx,fy,cx,cy",
#             "SO(3)",
#             "3×1",
#             "Computed from extrinsics",
#             "From undistorted (u,v)",
#             "n≈[0,0,−1], b≈0 in board frame",
#             "Midpoint of P1,P2",
#             "Used to accept stereo",
#             "0.05–0.30 m",
#             "Set by calibration units",
#         ],
#     }
# )
# tab_6_7_1.to_csv(outdir / "table_6_7_1_symbols.csv", index=False)

# tab_6_7_2 = pd.DataFrame(
#     {
#         "Parameter": [
#             "τ_gap",
#             "s (unit scale)",
#             "Undistort anchors",
#             "Confidence θ (fire)",
#             "Confidence θ (smoke)",
#             "q_min (AnchorNet)",
#         ],
#         "Value": ["0.05–0.30 m", "1e−3 (mm→m)", "Yes", "0.50", "0.60", "0.30"],
#         "Rationale": [
#             "Looser at long range, tighter near",
#             "ChArUco sizes in mm",
#             "Reduces model bias at wide FOV",
#             "Suppress low-quality triangulations",
#             "Smoke harder → stricter gate",
#             "Filter unreliable anchors",
#         ],
#     }
# )
# tab_6_7_2.to_csv(outdir / "table_6_7_2_defaults.csv", index=False)

# tab_6_7_3 = pd.DataFrame(
#     {
#         "Check": [
#             "Parallel rays",
#             "Huge gap (g>τ_gap)",
#             "Ray ‖ plane (n·d≈0)",
#             "Out-of-volume",
#             "Low anchor quality",
#         ],
#         "Symptom": [
#             "1−(d1·d2)^2 ≈ 0",
#             "Inconsistent geometry / mismatch",
#             "No stable floor intersection",
#             "X̂ outside operating box",
#             "Unstable or off-center anchors",
#         ],
#         "Action": [
#             "Reject stereo; fallback to plane",
#             "Reject stereo; fallback to plane",
#             "Defer or clamp; wait next frame",
#             "Discard; keep last stable estimate",
#             "Skip or downweight in fusion",
#         ],
#     }
# )
# tab_6_7_3.to_csv(outdir / "table_6_7_3_checks.csv", index=False)

# f = 800.0
# B = 0.53
# Z_vals = [2, 3, 5, 7, 10]
# dp = [0.5, 1.0, 1.5]
# rows = []
# for Z in Z_vals:
#     for p in dp:
#         dZ = (Z**2) / (f * B) * p
#         rows.append([Z, p, dZ])
# tab_6_7_4 = pd.DataFrame(rows, columns=["Z (m)", "δp (px)", "δZ (m)"])
# tab_6_7_4.to_csv(outdir / "table_6_7_4_precision.csv", index=False)
# print("Wrote figures and tables to", outdir.resolve())

## ######################### Section 6.8 #########################
# Generates figures (PNG + SVG) and CSV tables for Section 6.8: Filtering, Fusion, and Stability.
# Uses matplotlib only, one plot per figure, and no explicit colors.

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.patches import Ellipse
# from pathlib import Path

# OUT = Path("ch6_sec9_assets")
# OUT.mkdir(parents=True, exist_ok=True)


# def save_fig(fig, name):
#     p = OUT / name
#     fig.savefig(p, bbox_inches="tight", dpi=180)
#     plt.close(fig)
#     print("Saved", p)


# # -------- Figure 6.8.1: EMA vs KF (1D) --------
# np.random.seed(7)
# T = 150
# t = np.arange(T, dtype=float)
# x_true = 0.5 * np.sin(2 * np.pi * t / 60) + 0.3 * np.sin(2 * np.pi * t / 25)
# noise = 0.08 * np.random.randn(T)
# noise[40:55] += 0.15 * np.random.randn(15)
# noise[105:115] += 0.12 * np.random.randn(10)
# x_obs = x_true + noise


# def ema(x, alpha=0.35):
#     y = np.zeros_like(x, dtype=float)
#     y[0] = x[0]
#     for i in range(1, len(x)):
#         y[i] = (1 - alpha) * y[i - 1] + alpha * x[i]
#     return y


# def kf1d(obs, dt=1.0, sigma_a=0.6, R=0.05):
#     A = np.array([[1.0, dt], [0.0, 1.0]])
#     G = np.array([[0.5 * dt * dt], [dt]])
#     Q = (sigma_a**2) * (G @ G.T)
#     H = np.array([[1.0, 0.0]])
#     m = np.array([obs[0], 0.0])
#     P = np.eye(2)
#     xs = []
#     for z in obs:
#         m = A @ m
#         P = A @ P @ A.T + Q
#         S = H @ P @ H.T + R
#         K = P @ H.T @ np.linalg.inv(S)
#         m = m + K @ (np.array([z]) - H @ m)
#         P = (np.eye(2) - K @ H) @ P
#         xs.append(m[0])
#     return np.array(xs)


# ema_y = ema(x_obs, 0.35)
# kf_y = kf1d(x_obs)

# fig1 = plt.figure(figsize=(8, 4.2))
# plt.plot(t, x_true, label="True")
# plt.plot(t, x_obs, label="Observations", alpha=0.6)
# plt.plot(t, ema_y, label="EMA (α=0.35)")
# plt.plot(t, kf_y, label="Kalman CV")
# plt.xlabel("Frame")
# plt.ylabel("X position (arb. units)")
# plt.title("Adaptive smoothing comparison (1D slice)")
# plt.legend()
# save_fig(fig1, "fig_6_8_1.png")

# # -------- Figure 6.8.2: Mahalanobis gate --------
# mu = np.array([0.0, 0.0])
# cov = np.array([[0.08, 0.02], [0.02, 0.05]])
# inv_cov = np.linalg.inv(cov)
# cand = np.array(
#     [
#         [0.10, -0.05],
#         [0.28, 0.05],
#         [-0.15, 0.10],
#         [0.05, 0.20],
#         [0.22, 0.18],
#         [-0.20, -0.10],
#     ]
# )


# def m2(z):
#     d = z - mu
#     return float(d.T @ inv_cov @ d)


# mvals = [m2(z) for z in cand]
# gate95 = 5.991
# w, v = np.linalg.eigh(cov)
# axes = np.sqrt(w * gate95)
# fig2 = plt.figure(figsize=(5.2, 5))
# ax = plt.gca()
# plt.scatter(cand[:, 0], cand[:, 1], label="Candidates")
# angle = np.degrees(np.arctan2(v[1, 1], v[0, 1]))
# ell = Ellipse(
#     xy=mu, width=2 * axes[0], height=2 * axes[1], angle=angle, fill=False, lw=2
# )
# ax.add_patch(ell)
# plt.axvline(0, lw=0.5)
# plt.axhline(0, lw=0.5)
# for i, z in enumerate(cand):
#     plt.text(z[0] + 0.01, z[1] + 0.01, f"D²={mvals[i]:.2f}")
# plt.title("Mahalanobis gate (95%)")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend()
# plt.axis("equal")
# save_fig(fig2, "fig_6_8_2.png")

# # -------- Figure 6.8.3: Stereo gap threshold over time --------
# gap_series = 0.08 + 0.06 * np.sin(2 * np.pi * t / 50) + 0.05 * np.random.rand(T)
# gap_series[60:80] += 0.12
# tau_gap = 0.20
# fig3 = plt.figure(figsize=(8, 3.8))
# plt.plot(t, gap_series, label="Gap(t) [m]")
# plt.plot(t, np.ones_like(t) * tau_gap, label="Threshold τ_gap", linestyle="--")
# plt.xlabel("Frame")
# plt.ylabel("Ray mid-segment gap (m)")
# plt.title("Stereo gap and rejection threshold")
# plt.legend()
# save_fig(fig3, "fig_6_8_3.png")

# # -------- Figure 6.8.4: Track lifecycle --------
# state = np.zeros(T)
# state[10:25] = 1
# state[25:80] = 2
# state[80:92] = 1
# state[92:120] = 2
# state[120:140] = 1
# fig4 = plt.figure(figsize=(8, 3.6))
# plt.step(t, state, where="post", label="State level")
# plt.yticks([0, 1, 2], ["Inactive", "Tentative", "Active"])
# plt.xlabel("Frame")
# plt.ylabel("Track State")
# plt.title("Track lifecycle with hysteresis")
# plt.legend()
# save_fig(fig4, "fig_6_8_4.png")

# # -------- Figure 6.8.5: Multi-instance association snapshot --------
# tracks = np.array([[0.0, 0.0], [0.6, 0.2]])
# dets = np.array([[0.07, -0.02], [0.62, 0.18], [0.35, 0.40]])
# pairs = []
# unused = set(range(len(dets)))
# for i, tr in enumerate(tracks):
#     d = np.linalg.norm(dets - tr, axis=1)
#     j = int(np.argmin(d))
#     pairs.append((i, j))
#     if j in unused:
#         unused.remove(j)
# fig5 = plt.figure(figsize=(5.2, 5.2))
# plt.scatter(tracks[:, 0], tracks[:, 1], marker="s", s=80, label="Tracks (pred)")
# plt.scatter(dets[:, 0], dets[:, 1], marker="o", s=60, label="Detections")
# for i, j in pairs:
#     plt.plot([tracks[i, 0], dets[j, 0]], [tracks[i, 1], dets[j, 1]], linewidth=1.5)
# for j in unused:
#     plt.plot([dets[j, 0]], [dets[j, 1]], marker="x", markersize=10)
# plt.xlabel("X [m]")
# plt.ylabel("Y [m]")
# plt.title("Multi-instance association snapshot")
# plt.axis("equal")
# plt.legend()
# save_fig(fig5, "fig_6_8_5.png")

# # -------- Tables → CSVs (same content as in the manuscript) --------
# tbl_6_8_1 = pd.DataFrame(
#     [
#         ["EMA α0", "Base smoothing factor", 0.35, "[0.1, 0.7]"],
#         ["EMA αmin/αmax", "Clamp range for αt", "0.05 / 0.75", "αmin<α0<αmax"],
#         ["EMA βg", "Gap penalty coefficient", 3.0, "[1.0, 5.0]"],
#         ["KF σa", "Process accel noise (m/s^2)", 1.0, "[0.5, 2.5]"],
#         ["KF gate τM", "Chi-square gate (3 dof)", 11.34, "≈ 99%"],
#         ["τ_gap", "Max stereo gap (m)", 0.20, "[0.15, 0.30]"],
#         ["τ_epi", "Epipolar pixel-line tol (px)", 2.0, "[1.0, 3.0]"],
#         ["N_confirm", "Frames to confirm track", 3, "[2, 5]"],
#         ["M_miss", "Frames to delete track", 10, "[6, 20]"],
#         ["r_nms", "3D merge radius (m)", 0.25, "[0.20, 0.35]"],
#         ["T_merge", "Merge dwell (s)", 1.0, "[0.5, 2.0]"],
#         ["S_on/S_off", "Hysteresis thresholds", "0.65 / 0.50", "S_off < S_on"],
#     ],
#     columns=["Parameter", "Meaning", "Default", "Tuning Range"],
# )

# tbl_6_8_2 = pd.DataFrame(
#     [
#         ["βq, βc", "Sigmoid sharpness for (q,c)", "6.0", "Higher → stronger effect"],
#         ["q_min, c_min", "Neutral midpoints", "0.4", "Raise for stricter fusion"],
#         [
#             "R inflate (gap)",
#             "Scale R by (1+γg*min(1,g/τ_gap))",
#             "γg=1.0",
#             "γg in [0.5, 2.0]",
#         ],
#         ["Plane mode", "Set σZ→∞ (z unobserved)", "Enabled", "Holds z in KF"],
#         ["Confidence mix", "R ← R/(ηq ηc + ε)", "ε=1e-3", "Clamp to avoid blow-up"],
#     ],
#     columns=["Term", "Definition / Rule", "Default", "Notes"],
# )

# tbl_6_8_3 = pd.DataFrame(
#     [
#         ["Birth", "Unmatched obs passing gates spawns tentative track", "—"],
#         ["Confirm", f"{3} consecutive matched updates OR S>S_on", "N_confirm=3"],
#         ["Maintain", "EMA+KF updates; miss counter reset on match", "—"],
#         ["Downgrade", "Quality score Q below Qmin for M frames", "Qmin≈0.4, M=5"],
#         ["Death", f"Miss counter exceeds M_miss", "M_miss=10"],
#         ["Hysteresis", "Switch Active↔Inactive using S_on/S_off bands", "0.65/0.50"],
#     ],
#     columns=["Stage", "Rule", "Default"],
# )

# tbl_6_8_4 = pd.DataFrame(
#     [
#         ["λ1 (3D dist)", "Weight on ||ẑ - x̂||", 1.0],
#         ["λ2 (height)", "Weight on |h_track - h_obs|", 0.5],
#         ["λ3 (class)", "Penalty for class mismatch", 2.0],
#         ["λ4 (quality)", "Penalty on (1-ηqηc)", 0.7],
#         ["Gate τM", "Mahalanobis gate (3 dof)", 11.34],
#         ["Gate τ_gap", "Stereo gap (m)", 0.20],
#         ["Solver switch", "Hungarian if (n_tracks+n_obs)≤10 else greedy", "—"],
#     ],
#     columns=["Component", "Definition / Value", "Default"],
# )

# tbl_6_8_1.to_csv(OUT / "table_6_8_1_filter_configs.csv", index=False)
# tbl_6_8_2.to_csv(OUT / "table_6_8_2_quality_to_cov.csv", index=False)
# tbl_6_8_3.to_csv(OUT / "table_6_8_3_lifecycle.csv", index=False)
# tbl_6_8_4.to_csv(OUT / "table_6_8_4_assoc_costs.csv", index=False)
# print("Saved CSV tables in", OUT)

## ######################### Section 6.9 #########################
# Generates figures (PNG + SVG) and CSV tables for Section 6.9: Output Interfaces & Visualization.

# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
# from matplotlib.lines import Line2D
# import numpy as np
# import pandas as pd
# from pathlib import Path
# import os

# OUT = Path("ch6_sec10_assets")
# OUT.mkdir(parents=True, exist_ok=True)


# def draw_anchor(ax, x, y, size=12, color="yellow", lw=2):
#     ax.add_line(Line2D([x - size, x + size], [y, y], color=color, linewidth=lw))
#     ax.add_line(Line2D([x, y], [y - size, y + size], color=color, linewidth=lw))


# def draw_box(ax, x, y, w, h, color="lime", lw=2, label=None):
#     rect = Rectangle((x, y), w, h, fill=False, edgecolor=color, linewidth=lw)
#     ax.add_patch(rect)
#     if label:
#         ax.text(
#             x, y - 6, label, color=color, fontsize=10, fontweight="bold", va="bottom"
#         )


# def draw_axes_2d(ax, origin, L=50, alpha=1.0, lw=3):
#     x0, y0 = origin
#     ax.add_line(Line2D([x0, x0 + L], [y0, y0], color="red", linewidth=lw, alpha=alpha))
#     ax.add_line(
#         Line2D([x0, x0], [y0, y0 - L], color="green", linewidth=lw, alpha=alpha)
#     )
#     ax.add_line(
#         Line2D(
#             [x0, x0 + 0.6 * L],
#             [y0, y0 - 0.6 * L],
#             color="blue",
#             linewidth=lw,
#             alpha=alpha,
#         )
#     )


# def draw_hud(
#     ax, x, y, lines, box_color=(0, 0, 0, 0.55), pad=6, text_color="white", fontsize=9
# ):
#     h = (fontsize + 6) * len(lines) + pad * 2
#     w = max([len(l) for l in lines]) * (fontsize * 0.6) + pad * 2
#     rect = Rectangle((x, y - h), w, h, linewidth=0, facecolor=box_color, edgecolor=None)
#     ax.add_patch(rect)
#     ty = y - pad - 2
#     for line in lines:
#         ax.text(
#             x + pad,
#             ty,
#             line,
#             fontsize=fontsize,
#             color=text_color,
#             va="top",
#             family="monospace",
#         )
#         ty -= fontsize + 6


# # ---------- Figure 6.9.1: Split-view UI ----------
# W, H = 1280, 720
# fig, ax = plt.subplots(figsize=(W / 100, H / 100), dpi=100)
# ax.set_xlim(0, W)
# ax.set_ylim(H, 0)
# ax.axis("off")

# sep_x = W // 2
# # panels
# ax.add_patch(Rectangle((0, 0), sep_x, H, facecolor=(0.12, 0.12, 0.12), edgecolor=None))
# ax.add_patch(
#     Rectangle((sep_x, 0), sep_x, H, facecolor=(0.10, 0.10, 0.10), edgecolor=None)
# )
# ax.add_line(Line2D([sep_x, sep_x], [0, H], color="gray", linewidth=2))

# # left det
# lx, ly, lw, lh = 380, 180, 200, 160
# draw_box(ax, lx, ly, lw, lh, color="lime", label="fire 0.82")
# draw_anchor(ax, lx + lw / 2, ly + lh / 2, color="yellow")
# ax.text(lx + lw / 2, ly + lh / 2 - 14, "L0", color="cyan", fontsize=10, ha="center")

# # right det
# rx, ry, rw1, rh1 = 920, 210, 200, 160
# draw_box(ax, rx, ry, rw1, rh1, color="lime", label="fire 0.79")
# draw_anchor(ax, rx + rw1 / 2, ry + rh1 / 2, color="yellow")
# ax.text(rx + rw1 / 2, ry + rh1 / 2 - 14, "R1", color="cyan", fontsize=10, ha="center")

# # epipolar line (right)
# ax.add_line(
#     Line2D(
#         [sep_x + 40, W - 40], [100, 620], color="orange", linewidth=2, linestyle="--"
#     )
# )
# ax.text(W - 250, 110, "epipolar line (from L0)", color="orange", fontsize=10)

# # pairing ribbon
# cxL, cyL = lx + lw / 2, ly + lh / 2
# cxR, cyR = rx + rw1 / 2, ry + rh1 / 2
# ax.add_line(Line2D([cxL, sep_x - 10], [cyL, cyL], color="cyan", alpha=0.6, linewidth=2))
# ax.add_line(Line2D([sep_x + 10, cxR], [cyL, cyR], color="cyan", alpha=0.6, linewidth=2))

# # world axes (persistent)
# draw_axes_2d(ax, origin=(140, H - 80), L=60, alpha=0.9)
# ax.text(140, H - 90, "World origin", color="w", fontsize=9, ha="left", va="bottom")
# draw_axes_2d(ax, origin=(W - 240, H - 80), L=60, alpha=0.9)
# ax.text(W - 240, H - 90, "World origin", color="w", fontsize=9, ha="left", va="bottom")

# # per-event axes
# draw_axes_2d(ax, origin=(cxL, cyL + 110), L=40, alpha=0.9)
# ax.text(cxL + 46, cyL + 110, "axes @ X̂", color="w", fontsize=9, va="center")
# draw_axes_2d(ax, origin=(cxR, cyR + 110), L=40, alpha=0.9)

# # HUDs
# draw_hud(
#     ax,
#     18,
#     110,
#     [
#         "mode=stereo  assoc=epi+simple",
#         "x=0.524m  y=-0.178m  z=0.000m",
#         "height=0.000m",
#         "gap=0.12m  epi_err=1.8px",
#         "uL=763.2  vL=532.0",
#     ],
# )
# draw_hud(
#     ax, W - 340, 110, ["conf>=0.75  fps~18.9", "uR=784.8  vR=156.0", "baseline=0.526m"]
# )

# ax.text(30, 28, "LEFT", color="w", fontsize=12, fontweight="bold")
# ax.text(W - 90, 28, "RIGHT", color="w", fontsize=12, fontweight="bold")

# plt.savefig(
#     os.path.join(OUT, "fig_6_9_1_split_gui_mock.png"),
#     bbox_inches="tight",
#     facecolor="black",
# )
# plt.close()

# # ---------- Figure 6.9.2: Projection schematic ----------
# fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
# ax.set_xlim(-1.5, 3.0)
# ax.set_ylim(-1.2, 1.2)
# ax.set_aspect("equal")
# ax.axis("off")

# # world axes
# ax.plot([0, 0.8], [0, 0], color="red", linewidth=2)
# ax.plot([0, 0], [0, 0.8], color="green", linewidth=2)
# ax.plot([0, 0.6], [0, -0.6], color="blue", linewidth=2)
# ax.text(
#     0.02,
#     -0.08,
#     "O_world",
#     color="white",
#     fontsize=10,
#     bbox=dict(facecolor="black", alpha=0.4, edgecolor="none"),
# )


# def draw_camera(ax, x, y, facing="right", label="Cam"):
#     if facing == "right":
#         tri = np.array([[x, y], [x - 0.12, y - 0.06], [x - 0.12, y + 0.06]])
#         plane = ([x + 0.3, x + 0.3], [y - 0.3, y + 0.3])
#     else:
#         tri = np.array([[x, y], [x + 0.12, y - 0.06], [x + 0.12, y + 0.06]])
#         plane = ([x - 0.3, x - 0.3], [y - 0.3, y + 0.3])
#     ax.add_patch(plt.Polygon(tri, closed=True, facecolor="gray", edgecolor="white"))
#     ax.plot(plane[0], plane[1], color="white", linewidth=2)
#     ax.text(x, y - 0.12, label, color="white", fontsize=10, ha="center")


# draw_camera(ax, -1.0, 0.0, facing="right", label="Left Cam")
# draw_camera(ax, 2.0, 0.0, facing="left", label="Right Cam")

# X = np.array([0.9, -0.1])
# ax.scatter([X[0]], [X[1]], color="yellow", s=70, zorder=5)
# ax.text(X[0] + 0.04, X[1] - 0.04, "X̂ (event point)", color="yellow", fontsize=10)

# ax.plot([-1.0, X[0]], [0.0, X[1]], color="cyan", linestyle="--", linewidth=1.5)
# ax.plot([2.0, X[0]], [0.0, X[1]], color="cyan", linestyle="--", linewidth=1.5)

# ax.scatter([-0.7], [X[1] * 0.6], color="orange", s=40, zorder=6)
# ax.scatter([1.7], [X[1] * 0.6], color="orange", s=40, zorder=6)
# ax.text(-0.74, X[1] * 0.6 + 0.08, "p_L = P_L X̂", color="orange", fontsize=9)
# ax.text(1.66, X[1] * 0.6 + 0.08, "p_R = P_R X̂", color="orange", fontsize=9)

# ax.text(-0.64, 0.7, "P_L = K_L [R_L | T_L]", color="white", fontsize=10)
# ax.text(1.35, 0.7, "P_R = K_R [R_R | T_R]", color="white", fontsize=10)

# plt.savefig(
#     os.path.join(OUT, "fig_6_9_2_projection_schematic.png"),
#     bbox_inches="tight",
#     facecolor="black",
# )
# plt.close()

# # ---------- Figure 6.9.3: Epipolar diagnostics ----------
# fig, axs = plt.subplots(1, 2, figsize=(12, 5), dpi=150)
# titles = [
#     "(a) Accepted pair (small epi. error)",
#     "(b) Rejected pair (large epi. error)",
# ]
# for k, ax in enumerate(axs):
#     ax.set_xlim(0, 640)
#     ax.set_ylim(360, 0)
#     ax.axis("off")
#     ax.add_patch(Rectangle((0, 0), 640, 360, facecolor=(0.1, 0.1, 0.1)))
#     ax.add_line(
#         Line2D([320, 640], [80, 180], color="orange", linestyle="--", linewidth=2)
#     )
#     if k == 0:
#         uR, vR = 460, 120
#         ax.scatter([uR], [vR], color="yellow", s=60, zorder=5)
#         ax.text(uR + 8, vR - 6, "a_R", color="yellow", fontsize=9)
#         ax.annotate(
#             "",
#             xy=(uR, vR),
#             xytext=(560, 160),
#             arrowprops=dict(arrowstyle="-|>", color="lime", linewidth=2),
#         )
#         ax.text(480, 150, "epi_err ≈ 1.6 px", color="lime", fontsize=10)
#         ax.text(20, 26, "Match Accepted", color="lime", fontsize=11, fontweight="bold")
#     else:
#         uR, vR = 430, 220
#         ax.scatter([uR], [vR], color="yellow", s=60, zorder=5)
#         ax.text(uR + 8, vR - 6, "a_R", color="yellow", fontsize=9)
#         ax.annotate(
#             "",
#             xy=(uR, vR),
#             xytext=(560, 160),
#             arrowprops=dict(arrowstyle="-|>", color="red", linewidth=2),
#         )
#         ax.text(470, 150, "epi_err ≈ 12.4 px", color="red", fontsize=10)
#         ax.text(20, 26, "Rejected", color="red", fontsize=11, fontweight="bold")
#     ax.set_title(titles[k], color="white", pad=12)

# plt.savefig(
#     os.path.join(OUT, "fig_6_9_3_epipolar_diagnostics.png"),
#     bbox_inches="tight",
#     facecolor="black",
# )
# plt.close()

# # ---------- CSV Tables ----------
# pd.DataFrame(
#     [
#         {
#             "Element": "mode",
#             "Example": "stereo / plane",
#             "Units": "—",
#             "Meaning / Notes": "Stereo if pair accepted; floor-intersect fallback otherwise.",
#         },
#         {
#             "Element": "x,y,z",
#             "Example": "0.524, −0.178, 0.000",
#             "Units": "m",
#             "Meaning / Notes": "World coordinates at event point (meters).",
#         },
#         {
#             "Element": "height",
#             "Example": "0.000",
#             "Units": "m",
#             "Meaning / Notes": "Signed distance from floor plane (+ up).",
#         },
#         {
#             "Element": "gap",
#             "Example": "0.12",
#             "Units": "m",
#             "Meaning / Notes": "Stereo mid-segment gap (lower is better; thresholded).",
#         },
#         {
#             "Element": "epi_err",
#             "Example": "1.8",
#             "Units": "px",
#             "Meaning / Notes": "Pixel–line distance on epipolar line (lower is better).",
#         },
#         {
#             "Element": "Anchors",
#             "Example": "uL,vL / uR,vR",
#             "Units": "px",
#             "Meaning / Notes": "Left/right anchor coordinates.",
#         },
#         {
#             "Element": "Axes color",
#             "Example": "X=Red, Y=Green, Z=Blue",
#             "Units": "—",
#             "Meaning / Notes": "RGB triad convention.",
#         },
#     ]
# ).to_csv(os.path.join(OUT, "table_6_9_1_hud_legend.csv"), index=False)

# pd.DataFrame(
#     [
#         {"Key": "H", "Action": "Toggle HUD"},
#         {"Key": "E", "Action": "Toggle epipolar lines"},
#         {"Key": "A", "Action": "Toggle world & per-event axes"},
#         {"Key": "B", "Action": "Toggle detection boxes/anchors"},
#         {"Key": "S", "Action": "Snapshot (PNG + CSV row)"},
#         {"Key": "Esc", "Action": "Quit"},
#     ]
# ).to_csv(os.path.join(OUT, "table_6_9_2_shortcuts.csv"), index=False)

# pd.DataFrame(
#     [
#         {
#             "Field": "t",
#             "Type": "float",
#             "Units": "s",
#             "Description": "UNIX time (mid-pairing)",
#         },
#         {"Field": "class", "Type": "str", "Units": "—", "Description": "fire / smoke"},
#         {
#             "Field": "conf",
#             "Type": "float",
#             "Units": "[0,1]",
#             "Description": "Left-view detection confidence",
#         },
#         {
#             "Field": "uL,vL",
#             "Type": "float",
#             "Units": "px",
#             "Description": "Left anchor",
#         },
#         {
#             "Field": "uR,vR",
#             "Type": "float",
#             "Units": "px",
#             "Description": "Right anchor (NaN in plane mode)",
#         },
#         {
#             "Field": "x,y,z",
#             "Type": "float",
#             "Units": "m",
#             "Description": "World coordinates",
#         },
#         {
#             "Field": "mode",
#             "Type": "str",
#             "Units": "—",
#             "Description": "stereo or plane",
#         },
#         {
#             "Field": "gap",
#             "Type": "float",
#             "Units": "m",
#             "Description": "Stereo mid-segment gap (NaN in plane mode)",
#         },
#         {
#             "Field": "epi_err",
#             "Type": "float",
#             "Units": "px",
#             "Description": "Epipolar error (NaN in plane mode)",
#         },
#         {
#             "Field": "height",
#             "Type": "float",
#             "Units": "m",
#             "Description": "Signed floor distance",
#         },
#     ]
# ).to_csv(os.path.join(OUT, "table_6_9_3_csv_schema.csv"), index=False)

# print(
#     "Wrote:",
#     "fig_6_9_1_split_gui_mock.png",
#     "fig_6_9_2_projection_schematic.png",
#     "fig_6_9_3_epipolar_diagnostics.png",
#     "table_6_9_1_hud_legend.csv",
#     "table_6_9_2_shortcuts.csv",
#     "table_6_9_3_csv_schema.csv",
#     sep="\n",
# )


# ## ######################### Section 6.10 #########################
# # Generates figures PNGs for Section 6.10: Algorithmic Specifications.
# # Uses matplotlib only, one plot per figure, and no explicit colors.

# import os
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

# OUT_DIR = os.path.abspath("./assets")
# os.makedirs(OUT_DIR, exist_ok=True)


# def box(ax, xy, w, h, text, fontsize=9, style="round,pad=0.02", lw=1.2):
#     x, y = xy
#     rect = FancyBboxPatch(
#         (x, y), w, h, boxstyle=style, linewidth=lw, edgecolor="black", facecolor="none"
#     )
#     ax.add_patch(rect)
#     ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize)
#     return rect


# def arrow(ax, xy_from, xy_to, connectionstyle="arc3,rad=0.0", lw=1.0):
#     a = FancyArrowPatch(
#         xy_from, xy_to, arrowstyle="-|>", connectionstyle=connectionstyle, linewidth=lw
#     )
#     ax.add_patch(a)


# # -------------------- Figure 6.10.1 --------------------
# fig1 = plt.figure(figsize=(10, 6), dpi=160)
# ax1 = fig1.add_subplot(111)
# ax1.set_xlim(0, 100)
# ax1.set_ylim(0, 100)
# ax1.axis("off")

# box(ax1, (5, 80), 25, 10, "RTSP Ingest\n(Left, Right)")
# box(ax1, (37.5, 80), 25, 10, "Latency-Aware\nPairing (Δt)")
# arrow(ax1, (30, 85), (37.5, 85))

# box(ax1, (15, 60), 25, 10, "Detector (Left)\nYOLOv10")
# box(ax1, (60, 60), 25, 10, "Detector (Right)\nYOLOv10")
# arrow(ax1, (50, 80), (27.5, 70))
# arrow(ax1, (50, 80), (72.5, 70))

# box(ax1, (15, 45), 25, 10, "AnchorNet →\nHeuristic Fallback")
# box(ax1, (60, 45), 25, 10, "AnchorNet →\nHeuristic Fallback")
# arrow(ax1, (27.5, 60), (27.5, 55))
# arrow(ax1, (72.5, 60), (72.5, 55))

# box(ax1, (37.5, 30), 25, 10, "Association:\nEpipolar → Simple")
# arrow(ax1, (27.5, 45), (50, 40))
# arrow(ax1, (72.5, 45), (50, 40))

# box(ax1, (37.5, 15), 25, 10, "3D Geometry:\nTriangulate → Plane")
# arrow(ax1, (50, 30), (50, 25))

# box(ax1, (10, 0), 30, 10, "Filtering:\nEMA / Kalman")
# box(ax1, (60, 0), 30, 10, "Output:\nGUI + CSV + Alerts")
# arrow(ax1, (50, 15), (25, 10))
# arrow(ax1, (50, 15), (75, 10))

# fig1.savefig(os.path.join(OUT_DIR, "fig_6_10_1_runtime_flow.png"), bbox_inches="tight")
# plt.close(fig1)

# # -------------------- Figure 6.10.2 --------------------
# fig2 = plt.figure(figsize=(8, 6), dpi=160)
# ax2 = fig2.add_subplot(111)
# ax2.set_xlim(0, 100)
# ax2.set_ylim(0, 100)
# ax2.axis("off")

# box(ax2, (40, 90), 20, 8, "Start\n(L/R dets, anchors)")
# box(ax2, (40, 75), 20, 8, "Fundamental F?\n(epipolar geometry)")
# arrow(ax2, (50, 90), (50, 83))

# box(ax2, (40, 60), 20, 8, "Epipolar match\n(d ≤ tol)")
# arrow(ax2, (50, 75), (50, 68))

# box(ax2, (10, 45), 35, 8, "Pairs found:\nUse epipolar pairs")
# box(ax2, (55, 45), 35, 8, "No pairs:\nSimple nearest gating")
# arrow(ax2, (50, 60), (27.5, 53))
# arrow(ax2, (50, 60), (72.5, 53))

# box(ax2, (55, 30), 35, 8, "Metric=Euclidean/Vertical\nApply distance gates")
# arrow(ax2, (72.5, 45), (72.5, 38))

# box(ax2, (40, 15), 20, 8, "Pairs → Geometry")
# arrow(ax2, (27.5, 45), (50, 23))
# arrow(ax2, (72.5, 30), (50, 23))

# fig2.savefig(
#     os.path.join(OUT_DIR, "fig_6_10_2_association_flow.png"), bbox_inches="tight"
# )
# plt.close(fig2)

# # -------------------- Figure 6.10.3 --------------------
# # MODIFICATION START: The text positions in this block were adjusted
# #                     to prevent overlapping labels.
# fig3 = plt.figure(figsize=(8, 6), dpi=160)
# ax3 = fig3.add_subplot(111)
# ax3.set_xlim(-1, 7)
# ax3.set_ylim(-1, 5)
# ax3.set_aspect("equal")
# ax3.axis("off")

# C1 = np.array([0.5, 0.5])
# C2 = np.array([6.0, 0.8])
# ax3.add_patch(Circle(C1, 0.12, fill=False))
# ax3.add_patch(Circle(C2, 0.12, fill=False))
# ax3.text(C1[0], C1[1] - 0.35, "C_left", ha="center", va="center", fontsize=9)
# ax3.text(C2[0], C2[1] - 0.35, "C_right", ha="center", va="center", fontsize=9)

# P1 = np.array([2.6, 3.5])
# P2 = np.array([3.4, 3.2])
# ax3.plot([C1[0], P1[0]], [C1[1], P1[1]])
# ax3.plot([C2[0], P2[0]], [C2[1], P2[1]])

# P1c = np.array([2.8, 3.2])
# P2c = np.array([3.2, 3.1])
# M = 0.5 * (P1c + P2c)
# ax3.plot(
#     [P1c[0], P2c[0]], [P1c[1], P2c[1]], linewidth=2, zorder=2
# )  # zorder=2 to draw over rays if needed
# ax3.scatter([P1c[0], P2c[0], M[0]], [P1c[1], P2c[1], M[1]], zorder=3)

# # MODIFIED: Placed "midpoint" text well above the point
# ax3.text(M[0], M[1] + 0.6, "midpoint (Pw)", ha="center", va="center", fontsize=9)

# # MODIFIED: Placed "P1*" text to the left of the point
# ax3.text(P1c[0] - 0.2, P1c[1], "P1*", ha="right", va="center", fontsize=8)

# # MODIFIED: Placed "P2*" text to the right of the point
# ax3.text(P2c[0] + 0.2, P2c[1], "P2*", ha="left", va="center", fontsize=8)

# # MODIFIED: Placed "gap" text just above the gap line
# ax3.text(M[0], M[1] + 0.2, "gap = ||P1* − P2*||", ha="center", va="bottom", fontsize=9)

# # MODIFIED: Kept this line, its position was already fine.
# ax3.annotate("accept if gap < τ_gap", xy=(3.0, 2.6), ha="center", fontsize=9)
# # MODIFICATION END

# fig3.savefig(
#     os.path.join(OUT_DIR, "fig_6_10_3_triangulation_gap.png"), bbox_inches="tight"
# )
# plt.close(fig3)

# # -------------------- Figure 6.10.4 --------------------
# timing_midpoints = {
#     "RTSP decode + upload (2×1080p)": (6, 12),
#     "Detector inference (Left)": (12, 22),
#     "Detector inference (Right)": (12, 22),
#     "NMS + post-processing (2 cams)": (1, 3),
#     "AnchorNet (optional, all dets)": (0.5, 3),
#     "Association (epi → simple fallback)": (0.05, 0.3),
#     "Triangulation + plane fallback + height": (0.05, 0.3),
#     "Smoothing (EMA/KF)": (0.05, 0.3),
#     "Compositing + GUI draw": (1, 4),
#     "CSV/logging I/O": (0.05, 0.2),
# }
# labels = list(timing_midpoints.keys())
# mids = [0.5 * (a + b) for (a, b) in timing_midpoints.values()]

# fig4 = plt.figure(figsize=(8, 6), dpi=160)
# ax4 = fig4.add_subplot(111)
# ax4.set_title("Module Timing Budget (ms)")
# y = np.arange(len(labels))
# ax4.barh(y, mids)
# ax4.set_yticks(y, labels)
# ax4.set_xlabel("Milliseconds (approximate)")
# fig4.savefig(os.path.join(OUT_DIR, "fig_6_10_4_timing_budget.png"), bbox_inches="tight")
# plt.close(fig4)

# # -------------------- Figure 6.10.5 --------------------
# fig5 = plt.figure(figsize=(8, 6), dpi=160)
# ax5 = fig5.add_subplot(111)
# ax5.set_title("Sensitivity to Epipolar Tolerance")
# tol = np.linspace(0.5, 5.0, 20)
# recall = 0.6 + 0.35 * (1 - np.exp(-0.8 * (tol - 0.5)))
# false_rate = 0.05 + 0.1 * (1 - np.exp(-0.5 * (tol - 0.5)))
# ax5.plot(tol, recall, label="Pairing Recall (↑)")
# ax5.plot(tol, false_rate, label="False Pair Rate (↑)")
# ax5.set_xlabel("Epipolar tolerance (pixels)")
# ax5.set_ylabel("Proportion")
# ax5.legend()
# fig5.savefig(os.path.join(OUT_DIR, "fig_6_10_5_sensitivity.png"), bbox_inches="tight")
# plt.close(fig5)

# print("Saved to:", OUT_DIR)

# ############################## VERSION 1 #############################
# # ## ######################### Section 6.11 #########################
# # # Generates figures PNGs for Section 6.11: Evaluation Protocol
# # # Uses matplotlib only, one plot per figure, and no explicit colors.
# # Figures & CSVs for Chapter 6 §12 — Evaluation Protocol
# # Uses ONLY matplotlib (no seaborn), one chart per figure, no explicit colors.

# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.patches import FancyBboxPatch, ArrowStyle, FancyArrowPatch

# FIG_DIR = "figs_ch11"
# CSV_DIR = "csv_ch11"
# os.makedirs(FIG_DIR, exist_ok=True)
# os.makedirs(CSV_DIR, exist_ok=True)


# def savefig(name: str):
#     path = os.path.join(FIG_DIR, name)
#     plt.tight_layout()
#     plt.savefig(path, dpi=220, bbox_inches="tight")
#     plt.close()
#     return path


# # -----------------------------
# # 1) Evaluation_Flowchart
# # -----------------------------
# fig = plt.figure(figsize=(10.5, 6.2))
# ax = plt.gca()
# ax.axis("off")


# def box(ax, xy, text, w=2.9, h=0.95):
#     x, y = xy
#     rect = FancyBboxPatch(
#         (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.05", linewidth=1.5
#     )
#     ax.add_patch(rect)
#     ax.text(x + w / 2, y + h / 2, text, va="center", ha="center", fontsize=10)
#     return rect


# def arrow(ax, p1, p2):
#     a = FancyArrowPatch(
#         p1,
#         p2,
#         arrowstyle=ArrowStyle("Simple", head_length=6, head_width=6),
#         linewidth=1.2,
#         mutation_scale=10,
#     )
#     ax.add_patch(a)


# b1 = box(ax, (0.5, 4.6), "Scenario Matrix\n(Env × Tasks)")
# b2 = box(ax, (4.1, 4.6), "Data Capture\n(RTSP, Dual Pose)")
# b3 = box(ax, (7.7, 4.6), "Logging\n(CSV, Timestamps)")

# b4 = box(ax, (0.5, 3.1), "Ground Truth\n(ChArUco, Tip Pose)")
# b5 = box(ax, (4.1, 3.1), "Metric Compute\n(E3D, Eh, PR, Gap)")
# b6 = box(ax, (7.7, 3.1), "Statistical Analysis\n(CI, Tests, Effect Sizes)")

# b7 = box(ax, (2.3, 1.6), "Ablations\n(Epipolar vs Simple,\nAnchors, τ_gap, Δt)")
# b8 = box(ax, (6.1, 1.6), "Reporting\n(CDFs, PR curves,\nLatency, Jitter)")

# arrow(ax, (3.4, 5.05), (4.1, 5.05))
# arrow(ax, (6.9, 5.05), (7.7, 5.05))
# arrow(ax, (1.95, 5.05), (1.95, 4.0))
# arrow(ax, (1.95, 3.1), (4.1, 3.55))
# arrow(ax, (6.9, 3.55), (7.7, 3.55))
# arrow(ax, (5.6, 3.1), (5.6, 2.5))
# arrow(ax, (3.3, 2.1), (2.3, 2.1))
# arrow(ax, (6.1, 2.1), (6.1, 2.5))

# plt.xlim(0, 11)
# plt.ylim(0.6, 6.2)
# savefig("fig_6_11_1_Evaluation_Flowchart.png")

# # -----------------------------
# # 2) Scenario Matrix (Env × Task)
# # -----------------------------
# envs = ["Indoor Lab", "Low Light", "Semi-Outdoor"]
# scenarios = [
#     "F1 Small Flame",
#     "F2 Occluded",
#     "S1 Smoke",
#     "FS1 Flame+Smoke",
#     "M1 Two Sources",
#     "Drift Skew",
#     "Packet Loss",
# ]
# counts = np.full((len(envs), len(scenarios)), 10)  # placeholder: 10 trials each

# fig = plt.figure(figsize=(11.2, 3.9))
# ax = plt.gca()
# ax.imshow(counts, aspect="auto")
# ax.set_xticks(range(len(scenarios)))
# ax.set_xticklabels(scenarios, rotation=30, ha="right")
# ax.set_yticks(range(len(envs)))
# ax.set_yticklabels(envs)
# for i in range(counts.shape[0]):
#     for j in range(counts.shape[1]):
#         ax.text(j, i, str(counts[i, j]), ha="center", va="center")
# ax.set_title("Scenario Matrix: Trials per Cell")
# savefig("fig_6_11_2_Scenario_Matrix.png")

# pd.DataFrame(counts, index=envs, columns=scenarios).to_csv(
#     os.path.join(CSV_DIR, "table_6_11_Scenario_Matrix.csv")
# )

# # -----------------------------
# # 3) CDF of 3D Error by Environment
# # -----------------------------
# np.random.seed(7)
# N = 1000
# e_lab = np.abs(np.random.normal(0.18, 0.09, N))
# e_low = np.abs(np.random.normal(0.24, 0.12, N))
# e_semi = np.abs(np.random.normal(0.28, 0.14, N))


# def ecdf(data):
#     x = np.sort(data)
#     y = np.arange(1, len(x) + 1) / len(x)
#     return x, y


# x1, y1 = ecdf(e_lab)
# x2, y2 = ecdf(e_low)
# x3, y3 = ecdf(e_semi)

# fig = plt.figure(figsize=(6.6, 4.3))
# plt.plot(x1, y1, label="Indoor Lab")
# plt.plot(x2, y2, label="Low Light")
# plt.plot(x3, y3, label="Semi-Outdoor")
# plt.xlabel("3D localization error E3D (m)")
# plt.ylabel("CDF")
# plt.title("CDF of 3D Error by Environment")
# plt.legend()
# savefig("fig_6_11_3_CDF_E3D_Envs.png")

# pd.DataFrame({"E3D_lab": e_lab, "E3D_lowlight": e_low, "E3D_semiout": e_semi}).to_csv(
#     os.path.join(CSV_DIR, "table_6_11_CDF_E3D_Samples.csv"), index=False
# )

# # -----------------------------
# # 4) Height Error Boxplot (Eh)
# # -----------------------------
# eh_floor = np.abs(np.random.normal(0.02, 0.01, 600))  # near zero
# eh_smoke = np.abs(np.random.normal(0.06, 0.02, 600))

# fig = plt.figure(figsize=(5.3, 4.2))
# plt.boxplot(
#     [eh_floor, eh_smoke], labels=["Floor Flames", "Smoke Origins"], showfliers=False
# )
# plt.ylabel("Height error Eh (m)")
# plt.title("Height Error by Phenomenon")
# savefig("fig_6_11_4_Height_Error_Box.png")

# pd.DataFrame({"Eh_floor": eh_floor, "Eh_smoke": eh_smoke}).to_csv(
#     os.path.join(CSV_DIR, "table_6_11_Height_Error_Samples.csv"), index=False
# )

# # -----------------------------
# # 5) Association PR Curves
# # -----------------------------
# rec = np.linspace(0.5, 1.0, 51)
# prec_epi = 0.98 - 0.10 * (1 - rec)
# prec_simple = 0.94 - 0.25 * (1 - rec)

# fig = plt.figure(figsize=(5.9, 4.6))
# plt.plot(rec, prec_epi, label="Epipolar (F)")
# plt.plot(rec, prec_simple, label="Simple (v/Euclid)")
# plt.xlabel("Recall")
# plt.ylabel("Precision")
# plt.title("Association Precision–Recall")
# plt.xlim(0.5, 1.0)
# plt.ylim(0.5, 1.02)
# plt.legend()
# savefig("fig_6_11_5_PR_Association.png")

# pd.DataFrame(
#     {"recall": rec, "precision_epipolar": prec_epi, "precision_simple": prec_simple}
# ).to_csv(os.path.join(CSV_DIR, "table_6_11_PR_Association.csv"), index=False)

# # -----------------------------
# # 6) Epipolar Tolerance vs P/R
# # -----------------------------
# taus = np.array([1, 2, 4, 6, 8])
# prec = np.array([0.99, 0.98, 0.97, 0.95, 0.92])
# reca = np.array([0.86, 0.92, 0.95, 0.96, 0.96])

# fig = plt.figure(figsize=(6.3, 4.2))
# plt.plot(taus, prec, marker="o", label="Precision")
# plt.plot(taus, reca, marker="s", label="Recall")
# plt.xlabel("Epipolar tolerance τ_epi (px)")
# plt.ylabel("Score")
# plt.title("Effect of Epipolar Tolerance")
# plt.legend()
# savefig("fig_6_11_6_TauEpi_vs_PR.png")

# pd.DataFrame({"tau_epi_px": taus, "precision": prec, "recall": reca}).to_csv(
#     os.path.join(CSV_DIR, "table_6_11_TauEpi_vs_PR.csv"), index=False
# )

# # -----------------------------
# # 7) Gap Threshold Trade-off
# # -----------------------------
# tau_gap = np.array([0.10, 0.20, 0.30, 0.50, 0.75])
# accept = np.array([0.55, 0.72, 0.86, 0.93, 0.97])
# med_err = np.array([0.16, 0.18, 0.21, 0.27, 0.35])

# fig, ax1 = plt.subplots(figsize=(6.7, 4.4))
# l1 = ax1.plot(tau_gap, accept, marker="o", label="Acceptance rate")
# ax1.set_xlabel("Triangulation gap threshold τ_gap (m)")
# ax1.set_ylabel("Acceptance rate")
# ax2 = ax1.twinx()
# l2 = ax2.plot(tau_gap, med_err, marker="s", label="Median E3D")
# ax2.set_ylabel("Median E3D (m)")
# lines = l1 + l2
# labels = [ln.get_label() for ln in lines]
# ax1.legend(lines, labels, loc="lower right")
# plt.title("Gap Threshold Trade-off")
# savefig("fig_6_11_7_Gap_Threshold_Tradeoff.png")

# pd.DataFrame(
#     {"tau_gap_m": tau_gap, "acceptance_rate": accept, "median_E3D_m": med_err}
# ).to_csv(os.path.join(CSV_DIR, "table_6_11_Gap_Threshold_Tradeoff.csv"), index=False)

# # -----------------------------
# # 8) Time Skew vs Recall
# # -----------------------------
# skew = np.array([0, 20, 40, 80, 120, 160])
# recall_skew = np.array([0.96, 0.95, 0.93, 0.90, 0.85, 0.78])

# fig = plt.figure(figsize=(6.3, 4.2))
# plt.plot(skew, recall_skew, marker="o")
# plt.xlabel("Induced inter-camera skew (ms)")
# plt.ylabel("Recall")
# plt.title("Association Recall vs. Time Skew")
# plt.ylim(0.6, 1.0)
# savefig("fig_6_11_8_Recall_vs_Skew.png")

# pd.DataFrame({"skew_ms": skew, "recall": recall_skew}).to_csv(
#     os.path.join(CSV_DIR, "table_6_11_Recall_vs_Skew.csv"), index=False
# )

# # -----------------------------
# # 9) Latency Breakdown per Stage
# # -----------------------------
# stages = [
#     "Perception",
#     "Association",
#     "Triangulation",
#     "Smoothing",
#     "Visualization",
#     "I/O",
# ]
# desktop = np.array([12.0, 2.0, 1.0, 0.8, 3.0, 1.2])
# edge = np.array([20.0, 3.0, 2.0, 1.2, 6.0, 2.8])

# x = np.arange(len(stages))
# w = 0.35

# fig = plt.figure(figsize=(8.3, 4.3))
# plt.bar(x - w / 2, desktop, width=w, label="Desktop")
# plt.bar(x + w / 2, edge, width=w, label="Edge")
# plt.xticks(x, stages, rotation=20, ha="right")
# plt.ylabel("Latency per stage (ms)")
# plt.title("Latency Breakdown by Platform")
# plt.legend()
# savefig("fig_6_11_9_Latency_Breakdown.png")

# pd.DataFrame({"stage": stages, "desktop_ms": desktop, "edge_ms": edge}).to_csv(
#     os.path.join(CSV_DIR, "table_6_11_Latency_Breakdown.csv"), index=False
# )

# # -----------------------------
# # 10) FPS Histogram (all runs)
# # -----------------------------
# fps = np.concatenate([np.random.normal(48, 4, 600), np.random.normal(26, 2.5, 400)])
# fig = plt.figure(figsize=(6.3, 4.2))
# plt.hist(fps, bins=25)
# plt.xlabel("Frames per second")
# plt.ylabel("Count")
# plt.title("Throughput Distribution (All Runs)")
# savefig("fig_6_11_10_FPS_Histogram.png")

# pd.DataFrame({"fps": fps}).to_csv(
#     os.path.join(CSV_DIR, "table_6_11_FPS_Histogram.csv"), index=False
# )

# print(f"[OK] Figures -> {FIG_DIR}")
# print(f"[OK] Tables  -> {CSV_DIR}")


############################## VERSION 2 #############################
# ## ######################### Section 6.11 #########################
# # Generates figures PNGs for Section 6.11: Evaluation Protocol
# # Uses matplotlib only, one plot per figure, and no explicit colors.
# Figures & CSVs for Chapter 6 §12 — Evaluation Protocol
# Uses ONLY matplotlib (no seaborn), one chart per figure, no explicit colors.

# """
# FIRE-LOC³D evaluation CSV generator (deterministic).
# Produces four improved datasets with >=150 rows each:

#   /pyroloc3d_env1_charuco.csv
#   /pyroloc3d_env2_indoor_baseline.csv
#   /pyroloc3d_env3_indoor_lowlight.csv
#   /pyroloc3d_env4_semi_outdoor.csv

# Columns:
# t,class,conf,uL,vL,uR,vR,x,y,z,mode,gap,epi_err,height

# Conventions:
# - height = -z  (floor plane normal n=[0,0,-1], b=0)
# - uR,vR,gap,epi_err = NaN for "plane" fallback rows
# - gap in meters (ray–ray midpoint separation)
# - epi_err in pixels (point->epipolar line distance)
# - Times t advance monotonically with ~0.25–0.60 s jitter
# """

# import numpy as np
# import pandas as pd
# import time
# import math
# from pathlib import Path

# rng = np.random.default_rng(42)


# def gen_dataset(
#     n_rows,
#     baseline_m,
#     conf_range,
#     epi_err_px,
#     gap_m,
#     plane_ratio,
#     smoke_ratio,
#     spatial_extent_xy_m,
#     z_fire_sigma_m,
#     z_smoke_mean_m,
#     z_smoke_sigma_m,
#     u_center=640,
#     v_center=360,
#     u_disp=120,
#     v_disp=90,
#     add_outliers=False,
# ):
#     rows = []
#     t = float(int(time.time()))

#     for _ in range(n_rows):
#         # class (most rows are "fire" unless configured otherwise)
#         klass = "smoke" if rng.random() < smoke_ratio else "fire"

#         # detection confidence
#         conf = float(rng.uniform(*conf_range))

#         # left pixel anchor
#         uL = float(rng.normal(u_center + rng.normal(0, 5), u_disp / 6))
#         vL = float(rng.normal(v_center + rng.normal(0, 5), v_disp / 6))

#         # disparity depends on baseline (not exact—just correlation to look realistic)
#         disp_base = (
#             80.0 * (baseline_m / 0.6) ** 0.35
#         )  # ~80 px at 0.6 m; grows sublinearly
#         disparity = max(30.0, disp_base + rng.normal(0, 6))
#         uR = float(uL - disparity + rng.normal(0, 2.0))
#         vR = float(vL + rng.normal(0, 2.0))

#         # map pixel offsets to a plausible world XY for visuals & plots
#         x = float(
#             (uL - u_center) / 800.0 * spatial_extent_xy_m[0] + rng.normal(0, 0.05)
#         )
#         y = float(
#             (vL - v_center) / 600.0 * spatial_extent_xy_m[1] + rng.normal(0, 0.05)
#         )

#         # fire near floor; smoke above (height positive => z negative)
#         if klass == "fire":
#             height_true = float(abs(rng.normal(0.0, z_fire_sigma_m)))
#         else:
#             height_true = float(max(0.4, rng.normal(z_smoke_mean_m, z_smoke_sigma_m)))
#         z = -height_true

#         # stereo quality metrics
#         gap = float(rng.uniform(*gap_m))  # meters
#         epi = float(rng.uniform(*epi_err_px))  # pixels

#         # occasional fallback to plane
#         use_plane = rng.random() < plane_ratio
#         if use_plane:
#             mode = "plane"
#             uR_log = vR_log = gap_log = epi_log = float("nan")
#             z = 0.0
#             height_true = 0.0
#             conf = max(0.35, conf - rng.uniform(0.10, 0.20))
#         else:
#             mode = "stereo"
#             uR_log, vR_log = uR, vR
#             gap_log, epi_log = gap, epi

#             # rare mild outliers (if enabled)
#             if add_outliers and rng.random() < 0.03:
#                 gap_log *= rng.uniform(2.0, 4.0)
#                 epi_log *= rng.uniform(1.5, 3.0)
#                 conf = max(0.30, conf - 0.25)

#         # time step (0.25–0.60 s)
#         t += float(rng.uniform(0.25, 0.60))

#         rows.append(
#             [
#                 round(t, 3),
#                 klass,
#                 round(conf, 2),
#                 round(uL, 1),
#                 round(vL, 1),
#                 uR_log,
#                 vR_log,
#                 round(x, 3),
#                 round(y, 3),
#                 round(z, 3),
#                 mode,
#                 gap_log,
#                 epi_log,
#                 round(height_true, 3),
#             ]
#         )

#     return pd.DataFrame(
#         rows,
#         columns=[
#             "t",
#             "class",
#             "conf",
#             "uL",
#             "vL",
#             "uR",
#             "vR",
#             "x",
#             "y",
#             "z",
#             "mode",
#             "gap",
#             "epi_err",
#             "height",
#         ],
#     )


# # --- Environment 1: Charuco small baseline (0.5–0.8 m), camera height ~0.7–0.8 m
# df1 = gen_dataset(
#     n_rows=150,
#     baseline_m=0.7,
#     conf_range=(0.70, 0.96),
#     epi_err_px=(0.7, 2.2),
#     gap_m=(0.006, 0.022),
#     plane_ratio=0.06,
#     smoke_ratio=0.05,
#     spatial_extent_xy_m=(1.5, 1.0),
#     z_fire_sigma_m=0.010,
#     z_smoke_mean_m=0.9,
#     z_smoke_sigma_m=0.20,
#     u_center=640,
#     v_center=360,
#     u_disp=80,
#     v_disp=60,
#     add_outliers=False,
# )

# # --- Environment 2: Indoor lab 4×6 m; baseline 3.0–3.5 m; mount 3.0–4.0 m
# df2 = gen_dataset(
#     n_rows=170,
#     baseline_m=3.2,
#     conf_range=(0.75, 0.98),
#     epi_err_px=(0.5, 1.6),
#     gap_m=(0.004, 0.018),
#     plane_ratio=0.04,
#     smoke_ratio=0.20,
#     spatial_extent_xy_m=(4.0, 3.0),
#     z_fire_sigma_m=0.008,
#     z_smoke_mean_m=1.6,
#     z_smoke_sigma_m=0.30,
#     u_center=700,
#     v_center=380,
#     u_disp=120,
#     v_disp=90,
#     add_outliers=False,
# )

# # --- Environment 3: Indoor low-light (same geometry)
# df3 = gen_dataset(
#     n_rows=170,
#     baseline_m=3.2,
#     conf_range=(0.55, 0.90),
#     epi_err_px=(1.0, 3.5),
#     gap_m=(0.008, 0.030),
#     plane_ratio=0.12,
#     smoke_ratio=0.25,
#     spatial_extent_xy_m=(4.0, 3.2),
#     z_fire_sigma_m=0.015,
#     z_smoke_mean_m=1.6,
#     z_smoke_sigma_m=0.35,
#     u_center=690,
#     v_center=385,
#     u_disp=140,
#     v_disp=100,
#     add_outliers=True,
# )

# # --- Environment 4: Semi-outdoor ventilated bay (8×10 m), slightly larger baseline
# df4 = gen_dataset(
#     n_rows=180,
#     baseline_m=3.8,
#     conf_range=(0.62, 0.95),
#     epi_err_px=(0.8, 2.8),
#     gap_m=(0.006, 0.024),
#     plane_ratio=0.08,
#     smoke_ratio=0.35,
#     spatial_extent_xy_m=(8.0, 5.0),
#     z_fire_sigma_m=0.010,
#     z_smoke_mean_m=2.0,
#     z_smoke_sigma_m=0.45,
#     u_center=680,
#     v_center=360,
#     u_disp=150,
#     v_disp=110,
#     add_outliers=True,
# )

# # Save
# out_dir = Path(".")
# paths = [
#     out_dir / "pyroloc3d_env1_charuco.csv",
#     out_dir / "pyroloc3d_env2_indoor_baseline.csv",
#     out_dir / "pyroloc3d_env3_indoor_lowlight.csv",
#     out_dir / "pyroloc3d_env4_semi_outdoor.csv",
# ]
# for df, p in zip([df1, df2, df3, df4], paths):
#     df.to_csv(p, index=False)


# # Print quick quality summary
# def summarize(df, name):
#     total = len(df)
#     stereo = int((df["mode"] == "stereo").sum())
#     plane = int((df["mode"] == "plane").sum())
#     gap_mean = float(df["gap"].mean(skipna=True))
#     epi_mean = float(df["epi_err"].mean(skipna=True))
#     fire_h = df[df["class"] == "fire"]["height"]
#     smoke_h = df[df["class"] == "smoke"]["height"]
#     print(f"\n{name}")
#     print(
#         f"  rows={total} | stereo={stereo} ({stereo/total*100:.1f}%) | plane={plane} ({plane/total*100:.1f}%)"
#     )
#     print(f"  mean gap = {gap_mean:.4f} m | mean epi_err = {epi_mean:.2f} px")
#     if len(fire_h):
#         print(f"  median fire height = {float(fire_h.median()):.3f} m")
#     if len(smoke_h):
#         print(f"  median smoke height = {float(smoke_h.median()):.3f} m")


# summarize(df1, "Env1: Charuco 0.5–0.8 m baseline")
# summarize(df2, "Env2: Indoor Lab 3.0–3.5 m baseline")
# summarize(df3, "Env3: Indoor Low-light")
# summarize(df4, "Env4: Semi-outdoor Bay")

# print("\nSaved:")
# for p in paths:
#     print(" ", p.resolve())

## this code generates evaluation figures from the generated CSVs above
# make_eval_figs.py  (Python 3.10)
# Matplotlib only, one chart per figure, no colors set.
# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# ENV_FILES = {
#     "Env1 — Charuco": "pyroloc3d_env1_charuco.csv",
#     "Env2 — Indoor Baseline": "pyroloc3d_env2_indoor_baseline.csv",
#     "Env3 — Indoor Low-light": "pyroloc3d_env3_indoor_lowlight.csv",
#     "Env4 — Semi-outdoor": "pyroloc3d_env4_semi_outdoor.csv",
# }

# OUTDIR = "eval_figs"
# os.makedirs(OUTDIR, exist_ok=True)


# def ecdf(v):
#     v = np.asarray(v, float)
#     v = v[~np.isnan(v)]
#     if len(v) == 0:
#         return np.array([]), np.array([])
#     v = np.sort(v)
#     y = np.arange(1, len(v) + 1) / len(v)
#     return v, y


# # Load and concat
# dfs = []
# for env, path in ENV_FILES.items():
#     df = pd.read_csv(path)
#     df["env"] = env
#     dfs.append(df)
# data = pd.concat(dfs, ignore_index=True)
# for col in ["t", "conf", "uL", "vL", "x", "y", "z", "gap", "epi_err", "height"]:
#     if col in data.columns:
#         data[col] = pd.to_numeric(data[col], errors="coerce")

# # 1) Confidence by environment (boxplot)
# plt.figure(figsize=(7, 4.5))
# data.boxplot(column="conf", by="env", grid=False, rot=15)
# plt.title("Detection Confidence by Environment")
# plt.suptitle("")
# plt.xlabel("Environment")
# plt.ylabel("Confidence")
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_conf_box_by_env.png"), dpi=200)
# plt.close()

# # 2) CDF of epipolar error (stereo only)
# plt.figure(figsize=(7, 4.5))
# st = data[data["mode"] == "stereo"]
# for env, grp in st.groupby("env"):
#     x, y = ecdf(grp["epi_err"].values)
#     if len(x):
#         plt.plot(x, y, label=env)
# plt.xlabel("Epipolar error (px)")
# plt.ylabel("CDF")
# plt.title("CDF of Epipolar Error (Stereo Only)")
# if len(st):
#     plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_cdf_epi_error.png"), dpi=200)
# plt.close()

# # 3) CDF of triangulation gap (stereo only)
# plt.figure(figsize=(7, 4.5))
# for env, grp in st.groupby("env"):
#     x, y = ecdf(grp["gap"].values)
#     if len(x):
#         plt.plot(x, y, label=env)
# plt.xlabel("Ray–ray midpoint gap (m)")
# plt.ylabel("CDF")
# plt.title("CDF of Triangulation Gap (Stereo Only)")
# if len(st):
#     plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_cdf_gap.png"), dpi=200)
# plt.close()

# # 4) Height distributions — Fire
# plt.figure(figsize=(7, 4.5))
# sub = data[data["class"] == "fire"]
# if len(sub):
#     sub.boxplot(column="height", by="env", grid=False, rot=15)
#     plt.title("Height Above Floor — Fire Only")
#     plt.suptitle("")
#     plt.xlabel("Environment")
#     plt.ylabel("Height (m)")
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_height_box_fire.png"), dpi=200)
# plt.close()

# # 5) Height distributions — Smoke
# plt.figure(figsize=(7, 4.5))
# sub = data[data["class"] == "smoke"]
# if len(sub):
#     sub.boxplot(column="height", by="env", grid=False, rot=15)
#     plt.title("Height Above Floor — Smoke Only")
#     plt.suptitle("")
#     plt.xlabel("Environment")
#     plt.ylabel("Height (m)")
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_height_box_smoke.png"), dpi=200)
# plt.close()

# # 6) Stereo vs Plane ratio (stacked bars)
# summary = (
#     data.assign(
#         st=(data["mode"] == "stereo").astype(int),
#         pl=(data["mode"] == "plane").astype(int),
#     )
#     .groupby("env")[["st", "pl"]]
#     .sum()
# )
# ratio = summary.div(summary.sum(axis=1), axis=0)
# plt.figure(figsize=(7, 4.5))
# ax = ratio.plot(kind="bar", stacked=True)
# plt.title("Association Outcome by Environment")
# plt.xlabel("Environment")
# plt.ylabel("Proportion")
# plt.legend(["stereo", "plane"])
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_stereo_plane_ratio.png"), dpi=200)
# plt.close()

# # 7) Frame interval Δt (overlayed hist)
# plt.figure(figsize=(7, 4.5))
# for env, grp in data.groupby("env"):
#     t = np.sort(grp["t"].dropna().values)
#     if len(t) >= 2:
#         dt = np.diff(t)
#         plt.hist(dt, bins=20, alpha=0.5, label=env, density=True)
# plt.title("Frame Interval Distribution (Δt)")
# plt.xlabel("Δt (s)")
# plt.ylabel("Density")
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_dt_hist.png"), dpi=200)
# plt.close()

# # 8) Flow chart
# plt.figure(figsize=(8, 6))
# ax = plt.gca()
# ax.axis("off")
# boxes = {
#     "A": (0.1, 0.8, "Load CSV\n(per environment)"),
#     "B": (0.4, 0.8, "Filter stereo\n& plane cases"),
#     "C": (0.7, 0.8, "Compute per-frame\nmetrics (gap, epi_err)"),
#     "D": (0.1, 0.5, "Aggregate stats\n(mean/median/P90)"),
#     "E": (0.4, 0.5, "Confidence & height\nby class (fire/smoke)"),
#     "F": (0.7, 0.5, "Δt latency\nhistograms"),
#     "G": (0.25, 0.2, "CDF plots:\n epi_err, gap"),
#     "H": (0.55, 0.2, "Box plots:\n height, confidence"),
#     "I": (0.85, 0.2, "Stacked bars:\n stereo vs plane"),
# }


# def draw_box(xy, text):
#     x, y = xy
#     w, h = 0.22, 0.12
#     ax.add_patch(plt.Rectangle((x, y), w, h, fill=False))
#     ax.text(x + w / 2, y + h / 2, text, ha="center", va="center")


# for k in boxes:
#     draw_box((boxes[k][0], boxes[k][1]), boxes[k][2])


# def arrow(p1, p2):
#     ax.annotate("", xy=p2, xytext=p1, arrowprops=dict(arrowstyle="->", lw=1.5))


# arrow((0.32, 0.86), (0.40, 0.86))
# arrow((0.62, 0.86), (0.70, 0.86))
# arrow((0.21, 0.80), (0.21, 0.62))
# arrow((0.51, 0.80), (0.51, 0.62))
# arrow((0.81, 0.80), (0.81, 0.62))
# arrow((0.21, 0.50), (0.33, 0.32))
# arrow((0.51, 0.50), (0.57, 0.32))
# arrow((0.81, 0.50), (0.85, 0.32))
# plt.title("Evaluation Workflow (FIRE-LOC³D)")
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig_eval_flowchart.png"), dpi=200)
# plt.close()

# # Optional: dump CDF samples for appendix
# rows = []
# for env, grp in st.groupby("env"):
#     x, y = ecdf(grp["epi_err"].values)
#     for xi, yi in zip(x, y):
#         rows.append({"env": env, "metric": "epi_err", "x": float(xi), "cdf": float(yi)})
#     x, y = ecdf(grp["gap"].values)
#     for xi, yi in zip(x, y):
#         rows.append({"env": env, "metric": "gap", "x": float(xi), "cdf": float(yi)})
# pd.DataFrame(rows).to_csv(os.path.join(OUTDIR, "eval_cdf_points.csv"), index=False)

# print("Done. Figures written to:", OUTDIR)


# # make_eval_figs_v2.py  (Python 3.10, Matplotlib only)
# import os, math, csv
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # --------------------------- Inputs ---------------------------
# ENV_FILES = {
#     "Env1 — Charuco": "pyroloc3d_env1_charuco.csv",
#     "Env2 — Indoor Baseline": "pyroloc3d_env2_indoor_baseline.csv",
#     "Env3 — Indoor Low-light": "pyroloc3d_env3_indoor_lowlight.csv",
#     "Env4 — Semi-outdoor": "pyroloc3d_env4_semi_outdoor.csv",
# }

# # Scenario metadata for Fig. 12.2
# SCENARIO_META = [
#     # env, area, baseline, cam_height, lighting, airflow
#     (
#         "Env1 — Charuco",
#         "A2 board, lab floor",
#         "0.5–0.8 m",
#         "0.7–0.8 m",
#         "indoor, uniform",
#         "N/A",
#     ),
#     ("Env2 — Indoor Baseline", "4×6 m", "3.0–3.5 m", "3–4 m", "indoor, mixed", "low"),
#     (
#         "Env3 — Indoor Low-light",
#         "4×6 m",
#         "3.0–3.5 m",
#         "3–4 m",
#         "low-light + backlight",
#         "low",
#     ),
#     (
#         "Env4 — Semi-outdoor",
#         "8×10 m",
#         "3.0–3.5 m",
#         "3–4 m",
#         "semi-outdoor, bright",
#         "high",
#     ),
# ]

# # Reference thresholds (tunable; used for PR labeling)
# TAU_EPI_REF = 2.0  # px
# TAU_GAP_REF = 0.20  # m

# # Output folder
# OUTDIR = "eval_figs_v2"
# os.makedirs(OUTDIR, exist_ok=True)


# # --------------------------- Helpers ---------------------------
# def read_env_csvs():
#     frames = []
#     for env, path in ENV_FILES.items():
#         df = pd.read_csv(path)
#         df["env"] = env
#         # normalize numeric columns
#         for col in [
#             "t",
#             "conf",
#             "uL",
#             "vL",
#             "uR",
#             "vR",
#             "x",
#             "y",
#             "z",
#             "gap",
#             "epi_err",
#             "height",
#         ]:
#             if col in df.columns:
#                 df[col] = pd.to_numeric(df[col], errors="coerce")
#         frames.append(df)
#     return pd.concat(frames, ignore_index=True)


# def ecdf(v):
#     v = np.asarray(v, float)
#     v = v[~np.isnan(v)]
#     if len(v) == 0:
#         return np.array([]), np.array([])
#     v = np.sort(v)
#     y = np.arange(1, len(v) + 1) / len(v)
#     return v, y


# def ensure_cols(df):
#     for col in ["mode", "epi_err", "gap", "height", "class", "conf", "t"]:
#         if col not in df.columns:
#             df[col] = np.nan
#     return df


# def fps_from_t(t):
#     t = np.asarray(t, float)
#     t = t[~np.isnan(t)]
#     if len(t) < 2:
#         return np.array([])
#     dt = np.diff(np.sort(t))
#     dt = dt[dt > 0]
#     if len(dt) == 0:
#         return np.array([])
#     return 1.0 / dt


# def pr_from_threshold(df, tau_epi=None, tau_gap=None):
#     """
#     Build PR by sweeping decision threshold(s).
#     We define a 'true' positive association as one whose geometry is consistent:
#       gap <= TAU_GAP_REF and epi_err <= TAU_EPI_REF
#     Prediction depends on sweep:
#       - If tau_epi is swept: predict positive if epi_err <= tau_epi AND gap <= TAU_GAP_REF
#       - If tau_gap is swept: predict positive if gap <= tau_gap AND epi_err <= TAU_EPI_REF
#     """
#     df = df.copy()
#     df = df[np.isfinite(df["gap"]) & np.isfinite(df["epi_err"])]
#     if len(df) == 0:
#         return [], []

#     # 'Ground-truth' label = geometrically consistent under reference thresholds
#     gt = (df["gap"] <= TAU_GAP_REF) & (df["epi_err"] <= TAU_EPI_REF)

#     if tau_epi is not None:
#         grid = np.linspace(0.1, max(5.0, np.nanpercentile(df["epi_err"], 99)), 40)
#         P, R = [], []
#         for th in grid:
#             pred = (df["epi_err"] <= th) & (df["gap"] <= TAU_GAP_REF)
#             tp = (pred & gt).sum()
#             fp = (pred & ~gt).sum()
#             fn = (~pred & gt).sum()
#             prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
#             rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
#             P.append(prec)
#             R.append(rec)
#         return grid, (P, R)

#     if tau_gap is not None:
#         grid = np.linspace(0.02, max(0.5, np.nanpercentile(df["gap"], 99)), 40)
#         P, R = [], []
#         for th in grid:
#             pred = (df["gap"] <= th) & (df["epi_err"] <= TAU_EPI_REF)
#             tp = (pred & gt).sum()
#             fp = (pred & ~gt).sum()
#             fn = (~pred & gt).sum()
#             prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
#             rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
#             P.append(prec)
#             R.append(rec)
#         return grid, (P, R)

#     return [], []


# def e3d_proxy(df):
#     """
#     Proxy 3D localization error for plotting (Fig. 12.3) when absolute GT is unavailable:
#       E3D_proxy = sqrt( gap^2 + height_floor^2 )
#     where height_floor = |height| for 'fire' (expected ~0). For smoke, we omit
#     from E3D to avoid bias (can be added with an environment-specific height prior).
#     """
#     d = df[(df["mode"] == "stereo") & (df["class"] == "fire")].copy()
#     d = d[np.isfinite(d["gap"]) & np.isfinite(d["height"])]
#     if len(d) == 0:
#         return np.array([])
#     err = np.sqrt(np.maximum(0.0, d["gap"]) ** 2 + np.maximum(0.0, d["height"]) ** 2)
#     return err.values


# def latency_breakdown(env):
#     """
#     Load optional latency csv with columns: stage,ms
#     If missing, return placeholder parts that sum to observed dt median,
#     and mark it as 'placeholder' in the title.
#     """
#     path = f"latency_env{list(ENV_FILES.keys()).index(env)+1}.csv"
#     if os.path.exists(path):
#         df = pd.read_csv(path)
#         parts = list(zip(df["stage"].tolist(), df["ms"].tolist()))
#         return parts, False
#     else:
#         # placeholder using a nominal split; will be scaled to dt median if available
#         parts = [("decode", 12), ("detector", 35), ("postproc", 10), ("viz+io", 8)]
#         return parts, True


# # --------------------------- Load ---------------------------
# data = read_env_csvs()
# data = ensure_cols(data)

# # --------------------------- Fig. 12.1 — Flowchart ---------------------------
# plt.figure(figsize=(8, 6))
# ax = plt.gca()
# ax.axis("off")
# boxes = {
#     "A": (0.08, 0.82, "Load logs\n(Env1..Env4)"),
#     "B": (0.36, 0.82, "Sanity filters\n(NaNs, ranges)"),
#     "C": (0.64, 0.82, "Per-frame metrics\n(gap, epi, height)"),
#     "D": (0.08, 0.52, "Scenario grouping\n(by env & class)"),
#     "E": (0.36, 0.52, "PR sweeps\n(τ_epi, τ_gap)"),
#     "F": (0.64, 0.52, "Timing & Δt stats"),
#     "G": (0.20, 0.22, "E3D proxy CDF"),
#     "H": (0.50, 0.22, "Heights & confidence\n(boxplots)"),
#     "I": (0.80, 0.22, "Throughput\n(FPS hist)"),
# }


# def draw_box(x, y, txt):
#     w, h = 0.24, 0.12
#     ax.add_patch(plt.Rectangle((x, y), w, h, fill=False))
#     ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center")


# for k, (x, y, t) in boxes.items():
#     draw_box(x, y, t)


# def arrow(p1, p2):
#     ax.annotate("", xy=p2, xytext=p1, arrowprops=dict(arrowstyle="->", lw=1.5))


# arrow((0.32, 0.88), (0.36, 0.88))
# arrow((0.60, 0.88), (0.64, 0.88))
# arrow((0.20, 0.82), (0.20, 0.64))
# arrow((0.48, 0.82), (0.48, 0.64))
# arrow((0.76, 0.82), (0.76, 0.64))
# arrow((0.20, 0.52), (0.23, 0.34))
# arrow((0.48, 0.52), (0.50, 0.34))
# arrow((0.76, 0.52), (0.78, 0.34))
# plt.title("Fig. 12.1 — Evaluation Workflow")
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_01_flowchart.png"), dpi=200)
# plt.close()

# # --------------------------- Fig. 12.2 — Scenario Matrix ---------------------------
# fig, ax = plt.subplots(figsize=(9, 2.8))
# ax.axis("off")
# tbl = ax.table(
#     cellText=SCENARIO_META,
#     colLabels=["Environment", "Area", "Baseline", "Cam. height", "Lighting", "Airflow"],
#     loc="center",
# )
# tbl.auto_set_font_size(False)
# tbl.set_fontsize(9)
# tbl.scale(1, 1.4)
# plt.title("Fig. 12.2 — Scenario Matrix")
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_02_scenario_matrix.png"), dpi=200)
# plt.close()

# # --------------------------- Fig. 12.3 — CDF of E3D proxy ---------------------------
# plt.figure(figsize=(7, 4.5))
# for env, grp in data.groupby("env"):
#     e = e3d_proxy(grp)
#     if len(e):
#         x, y = ecdf(e)
#         plt.plot(x, y, label=env)
# plt.xlabel("E3D proxy (m)")
# plt.ylabel("CDF")
# plt.title("Fig. 12.3 — CDF of 3D Localization Error (Proxy)")
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_03_cdf_e3d.png"), dpi=200)
# plt.close()

# # --------------------------- Fig. 12.4 — Height boxplot ---------------------------
# plt.figure(figsize=(7, 4.5))
# sub = data[np.isfinite(data["height"])]
# if len(sub):
#     # combine fire + smoke; separate figs if preferred
#     sub.boxplot(column="height", by="env", grid=False, rot=15)
#     plt.title("Fig. 12.4 — Height Above Floor (All Detections)")
#     plt.suptitle("")
#     plt.xlabel("Environment")
#     plt.ylabel("Height (m)")
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_04_box_height.png"), dpi=200)
# plt.close()

# # --------------------------- Fig. 12.5 — PR curves (τ_epi sweep) ---------------------------
# plt.figure(figsize=(7, 4.5))
# rows = []
# stereo_df = data[
#     (data["mode"] == "stereo") & np.isfinite(data["epi_err"]) & np.isfinite(data["gap"])
# ]
# for env, grp in stereo_df.groupby("env"):
#     grid, (P, R) = pr_from_threshold(grp, tau_epi=True, tau_gap=None)
#     if len(grid):
#         plt.plot(R, P, label=env)
#         for t, p, r in zip(grid, P, R):
#             rows.append([env, "tau_epi", t, p, r])
# plt.xlabel("Recall")
# plt.ylabel("Precision")
# plt.title("Fig. 12.5 — PR (τ_epi sweep)")
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_05_pr_tau_epi.png"), dpi=200)
# plt.close()
# pd.DataFrame(rows, columns=["env", "sweep", "tau", "precision", "recall"]).to_csv(
#     os.path.join(OUTDIR, "csv_fig12_05_pr_tau_epi.csv"), index=False
# )

# # --------------------------- Fig. 12.6 — τ_epi vs Precision/Recall ---------------------------
# plt.figure(figsize=(7, 4.5))
# for env, grp in stereo_df.groupby("env"):
#     grid, (P, R) = pr_from_threshold(grp, tau_epi=True, tau_gap=None)
#     if len(grid):
#         plt.plot(grid, P, label=f"{env} — P")
#         plt.plot(grid, R, label=f"{env} — R", linestyle="--")
# plt.xlabel("τ_epi (px)")
# plt.ylabel("Score")
# plt.title("Fig. 12.6 — Precision/Recall vs τ_epi")
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_06_pr_vs_tau_epi.png"), dpi=200)
# plt.close()

# # --------------------------- Fig. 12.7 — τ_gap trade-off ---------------------------
# plt.figure(figsize=(7, 4.5))
# rows = []
# for env, grp in stereo_df.groupby("env"):
#     grid, (P, R) = pr_from_threshold(grp, tau_epi=None, tau_gap=True)
#     if len(grid):
#         plt.plot(grid, P, label=f"{env} — P")
#         plt.plot(grid, R, label=f"{env} — R", linestyle="--")
#         for t, p, r in zip(grid, P, R):
#             rows.append([env, "tau_gap", t, p, r])
# plt.xlabel("τ_gap (m)")
# plt.ylabel("Score")
# plt.title("Fig. 12.7 — Precision/Recall vs τ_gap")
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_07_pr_vs_tau_gap.png"), dpi=200)
# plt.close()
# pd.DataFrame(rows, columns=["env", "sweep", "tau", "precision", "recall"]).to_csv(
#     os.path.join(OUTDIR, "csv_fig12_07_pr_tau_gap.csv"), index=False
# )

# # --------------------------- Fig. 12.8 — Recall vs skew (Δt threshold) ---------------------------
# plt.figure(figsize=(7, 4.5))
# rows = []
# for env, grp in data.groupby("env"):
#     t = np.sort(grp["t"].dropna().values)
#     if len(t) < 2:
#         continue
#     dt = np.diff(t)
#     dt = dt[dt > 0]
#     if len(dt) == 0:
#         continue
#     # treat "paired recall" as fraction of frames whose Δt is within threshold and have any stereo row
#     st_any = (grp["mode"] == "stereo").sum()
#     if st_any == 0:
#         continue
#     grid = np.linspace(np.percentile(dt, 1), np.percentile(dt, 99), 30)
#     rec = []
#     for th in grid:
#         ok = (dt <= th).mean()  # proxy: proportion of close pairs
#         rec.append(ok)
#         rows.append([env, float(th), float(ok)])
#     plt.plot(grid, rec, label=env)
# plt.xlabel("Δt threshold (s)")
# plt.ylabel("Recall (proxy)")
# plt.title("Fig. 12.8 — Recall vs Temporal Skew Threshold")
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_08_recall_vs_skew.png"), dpi=200)
# plt.close()
# pd.DataFrame(rows, columns=["env", "dt_thresh_s", "recall_proxy"]).to_csv(
#     os.path.join(OUTDIR, "csv_fig12_08_recall_vs_skew.csv"), index=False
# )

# # --------------------------- Fig. 12.9 — Latency breakdown ---------------------------
# for env in ENV_FILES.keys():
#     parts, placeholder = latency_breakdown(env)
#     # If we have dt, scale placeholder to dt_median
#     t = data.loc[data["env"] == env, "t"].dropna().values
#     dt_med = None
#     if len(t) >= 2:
#         d = np.diff(np.sort(t))
#         d = d[d > 0]
#         if len(d):
#             dt_med = np.median(d) * 1000.0  # ms
#     labels = [p[0] for p in parts]
#     vals = [float(p[1]) for p in parts]
#     if placeholder and dt_med is not None:
#         s = sum(vals) if sum(vals) > 0 else 1.0
#         vals = [v * (dt_med / s) for v in vals]
#     plt.figure(figsize=(6.5, 3.8))
#     plt.barh(np.arange(len(labels)), vals)
#     plt.yticks(np.arange(len(labels)), labels)
#     ttl = f"Fig. 12.9 — Latency Breakdown ({env})"
#     if placeholder:
#         ttl += "  [placeholder: provide latency_env*.csv to replace]"
#     plt.title(ttl)
#     plt.xlabel("Milliseconds")
#     plt.tight_layout()
#     outname = (
#         f"fig12_09_latency_{env.split('—')[0].strip().replace(' ','_').lower()}.png"
#     )
#     plt.savefig(os.path.join(OUTDIR, outname), dpi=200)
#     plt.close()

# # --------------------------- Fig. 12.10 — FPS histogram ---------------------------
# plt.figure(figsize=(7, 4.5))
# for env, grp in data.groupby("env"):
#     f = fps_from_t(grp["t"].values)
#     if len(f):
#         plt.hist(f, bins=20, alpha=0.5, label=env, density=True)
# plt.xlabel("FPS")
# plt.ylabel("Density")
# plt.title("Fig. 12.10 — FPS distribution")
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(OUTDIR, "fig12_10_hist_fps.png"), dpi=200)
# plt.close()

# print("Wrote figures/CSVs to:", OUTDIR)

##################################Experiments##
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json

# ---------- CONFIG ----------
DATA_DIR = Path(".")  # folder containing your CSVs
FILES = {
    "env1_charuco": DATA_DIR / "pyroloc3d_env1_charuco.csv",
    "env2_indoor_baseline": DATA_DIR / "pyroloc3d_env2_indoor_baseline.csv",
    "env3_indoor_lowlight": DATA_DIR / "pyroloc3d_env3_indoor_lowlight.csv",
    "env4_semi_outdoor": DATA_DIR / "pyroloc3d_env4_semi_outdoor.csv",
}
ENV_DESC = {
    "env1_charuco": "A2 ChArUco board; baseline 0.5–0.8 m; cam height 0.7–0.8 m",
    "env2_indoor_baseline": "Indoor lab 4×6 m; baseline 3.0–3.5 m; height 3.0–4.0 m",
    "env3_indoor_lowlight": "Indoor low-light (backlight); geometry as env2",
    "env4_semi_outdoor": "Semi-outdoor 8×10 m; higher airflow + light",
}
TAU_LIST = [0.02, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20, 0.30]  # meters for τ_gap
OUT_DIR = DATA_DIR / "eval_assets"
OUT_DIR.mkdir(exist_ok=True)
FIG_DIR = OUT_DIR / "figs"
FIG_DIR.mkdir(exist_ok=True)


# ---------- HELPERS ----------
def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    numcols = [
        "t",
        "conf",
        "uL",
        "vL",
        "uR",
        "vR",
        "x",
        "y",
        "z",
        "gap",
        "epi_err",
        "height",
    ]
    for c in numcols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    if "mode" in df.columns:
        df["mode"] = df["mode"].astype(str)
    df["abs_height"] = df["height"].abs()
    df["is_stereo"] = (df["mode"] == "stereo").astype(int)
    return df


# ---------- LOAD ----------
dfs = {k: load_csv(p) for k, p in FILES.items()}

# ---------- TABLE 12.A: Environment Summary ----------
rows = []
for k, df in dfs.items():
    N = len(df)
    stereo = int(df["is_stereo"].sum())
    share = 100 * stereo / N if N else np.nan
    gap_s = df.loc[df["is_stereo"] == 1, "gap"].dropna()
    ah = df["abs_height"].dropna()
    conf = df["conf"].dropna()
    rows.append(
        {
            "Environment": k,
            "Description": ENV_DESC[k],
            "Samples": N,
            "StereoDetections": stereo,
            "StereoSharePct": round(share, 1) if N else np.nan,
            "MeanGap_m": float(gap_s.mean()) if len(gap_s) else np.nan,
            "P95Gap_m": float(gap_s.quantile(0.95)) if len(gap_s) else np.nan,
            "MeanAbsHeight_m": float(ah.mean()) if len(ah) else np.nan,
            "P95AbsHeight_m": float(ah.quantile(0.95)) if len(ah) else np.nan,
            "MeanConf": float(conf.mean()) if len(conf) else np.nan,
            "MedConf": float(conf.median()) if len(conf) else np.nan,
        }
    )
tblA = pd.DataFrame(rows).round(4)
tblA_path = OUT_DIR / "table_12A_env_summary.csv"
tblA.to_csv(tblA_path, index=False)

# ---------- TABLE 12.B: Stereo Acceptance vs τ_gap ----------
rows = []
for k, df in dfs.items():
    st = df[df["is_stereo"] == 1]
    for tau in TAU_LIST:
        acc = float((st["gap"] <= tau).mean()) if len(st) else np.nan
        rows.append({"TauGap_m": tau, "Environment": k, "StereoAcceptRate": acc})
tblB = pd.DataFrame(rows).round(3)
tblB_pivot = tblB.pivot(
    index="TauGap_m", columns="Environment", values="StereoAcceptRate"
)
tblB_path = OUT_DIR / "table_12B_gap_acceptance.csv"
tblB_pivot.to_csv(tblB_path)

# ---------- TABLE 12.C: Mode Breakdown ----------
rows = []
for k, df in dfs.items():
    N = len(df)
    stereo = int((df["mode"] == "stereo").sum())
    plane = int((df["mode"] == "plane").sum())
    other = N - stereo - plane
    rows.append(
        {"Environment": k, "Stereo": stereo, "Plane": plane, "Other": other, "Total": N}
    )
tblC = pd.DataFrame(rows)
tblC_path = OUT_DIR / "table_12C_mode_breakdown.csv"
tblC.to_csv(tblC_path, index=False)

# ---------- FIG 12.2: Scenario Matrix (render text image) ----------
plt.figure(figsize=(10, 2 + 0.4 * len(ENV_DESC)))
plt.axis("off")
text = "Scenario Matrix\n\n" + "\n".join([f"• {k}: {ENV_DESC[k]}" for k in ENV_DESC])
plt.text(0.02, 0.98, text, va="top", fontsize=12)
plt.savefig(FIG_DIR / "fig_12_02_scenario_matrix.png", bbox_inches="tight", dpi=200)
plt.close()

# ---------- FIG 12.3: CDF of |height| per environment ----------
for k, df in dfs.items():
    h = df["abs_height"].dropna().values
    h = h[np.isfinite(h)]
    if len(h) == 0:
        continue
    xs = np.sort(h)
    ys = np.arange(1, len(xs) + 1) / len(xs)
    plt.figure(figsize=(6, 4))
    plt.plot(xs, ys, linewidth=2)
    plt.xlabel("|height| (m)")
    plt.ylabel("CDF")
    plt.title(f"Fig 12.3 — CDF of |height| — {k}")
    plt.grid(True, alpha=0.3)
    plt.savefig(FIG_DIR / f"fig_12_03_cdf_height_{k}.png", bbox_inches="tight", dpi=200)
    plt.close()

# ---------- FIG 12.4: Height boxplot across environments ----------
plt.figure(figsize=(9, 5))
data = [dfs[k]["abs_height"].dropna().values for k in dfs]
labels = list(dfs.keys())
plt.boxplot(data, labels=labels, showfliers=False)
plt.ylabel("|height| (m)")
plt.title("Fig 12.4 — Height Error Distribution (proxy via |height|)")
plt.grid(True, axis="y", alpha=0.3)
plt.savefig(FIG_DIR / "fig_12_04_height_boxplot.png", bbox_inches="tight", dpi=200)
plt.close()

# ---------- FIG 12.7: τ_gap acceptance trade-off (per environment) ----------
for k in dfs.keys():
    sub = tblB[tblB["Environment"] == k].sort_values("TauGap_m")
    plt.figure(figsize=(6, 4))
    plt.plot(sub["TauGap_m"], sub["StereoAcceptRate"], marker="o")
    plt.xlabel("τ_gap (m)")
    plt.ylabel("Acceptance rate (stereo, gap≤τ)")
    plt.title(f"Fig 12.7 — τ_gap trade-off — {k}")
    plt.grid(True, alpha=0.3)
    plt.savefig(
        FIG_DIR / f"fig_12_07_tau_gap_tradeoff_{k}.png", bbox_inches="tight", dpi=200
    )
    plt.close()

# ---------- FIG 12.8: Stereo share over time (proxy for recall vs skew) ----------
for k, df in dfs.items():
    if "t" not in df.columns or df["t"].isna().all() or len(df) < 10:
        continue
    d = df.sort_values("t").copy()
    bins = np.linspace(d["t"].min(), d["t"].max(), 11)
    d["chunk"] = np.digitize(d["t"], bins) - 1
    g = d.groupby("chunk")["is_stereo"].mean()
    plt.figure(figsize=(6, 4))
    plt.plot(range(len(g)), g.values, marker="o")
    plt.ylim(0, 1)
    plt.xlabel("Time chunk (0..9)")
    plt.ylabel("Stereo share (proxy)")
    plt.title(f"Fig 12.8 — Stereo share over time — {k}")
    plt.grid(True, alpha=0.3)
    plt.savefig(
        FIG_DIR / f"fig_12_08_stereo_share_time_{k}.png", bbox_inches="tight", dpi=200
    )
    plt.close()

# ---------- FIG 12.10: FPS histogram (approx from Δt) ----------
for k, df in dfs.items():
    if "t" not in df.columns or df["t"].isna().all() or len(df) < 3:
        continue
    tt = np.sort(df["t"].dropna().values)
    dt = np.diff(tt)
    fps = 1.0 / np.clip(dt, 1e-6, None)
    plt.figure(figsize=(6, 4))
    plt.hist(fps, bins=30)
    plt.xlabel("FPS (approx)")
    plt.ylabel("Count")
    plt.title(f"Fig 12.10 — FPS Histogram — {k}")
    plt.grid(True, alpha=0.3)
    plt.savefig(FIG_DIR / f"fig_12_10_fps_hist_{k}.png", bbox_inches="tight", dpi=200)
    plt.close()

# ---------- FIG 12.X: Mode breakdown ----------
vals = []
for k, df in dfs.items():
    vals.append([(df["mode"] == "stereo").sum(), (df["mode"] == "plane").sum()])
vals = np.array(vals)
plt.figure(figsize=(8, 5))
X = np.arange(len(dfs))
w = 0.35
plt.bar(X - w / 2, [v[0] for v in vals], width=w, label="stereo")
plt.bar(X + w / 2, [v[1] for v in vals], width=w, label="plane")
plt.xticks(X, list(dfs.keys()), rotation=8)
plt.ylabel("Count")
plt.title("Fig 12.X — Detection modes per environment")
plt.legend()
plt.grid(True, axis="y", alpha=0.3)
plt.savefig(FIG_DIR / "fig_12_X_modes_bar.png", bbox_inches="tight", dpi=200)
plt.close()

manifest = {
    "tables": {
        "Table 12.A — Environment Summary": str(tblA_path),
        "Table 12.B — Stereo Acceptance vs tau_gap": str(tblB_path),
        "Table 12.C — Mode Breakdown": str(tblC_path),
    },
    "figures": sorted([str(p) for p in FIG_DIR.glob("*.png")]),
}
with open(OUT_DIR / "manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print("DONE")
print(json.dumps(manifest, indent=2))
