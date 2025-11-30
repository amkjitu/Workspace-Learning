from ultralytics import YOLO


class FireSmokeDetector:
    def __init__(self, weights_path, conf=0.25):
        self.model = YOLO(weights_path)
        self.conf = conf
        # expect classes: 0:fire, 1:smoke (rename here if needed)
        self.names = self.model.names

    def infer(self, frame):
        res = self.model.predict(frame, conf=self.conf, verbose=False)[0]
        dets = []
        for b in res.boxes:
            x1, y1, x2, y2 = b.xyxy[0].tolist()
            cls = int(b.cls)
            conf = float(b.conf)
            dets.append((cls, (x1, y1, x2, y2), conf))
        return dets
