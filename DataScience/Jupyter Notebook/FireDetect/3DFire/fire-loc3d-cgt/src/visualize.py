import cv2, numpy as np


def draw_det(img, dets, anchors=None, color=(0, 255, 0)):
    for i, (cls, box, conf) in enumerate(dets):
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            img,
            f"{cls}:{conf:.2f}",
            (x1, y1 - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            1,
        )
        if anchors and anchors[i] is not None:
            u, v, _ = anchors[i]
            cv2.circle(img, (int(u), int(v)), 3, (0, 0, 255), -1)
    return img


def put_point(img, P, txt, color=(0, 255, 255)):
    if P is None:
        return img
    cv2.putText(
        img,
        f"{txt}: ({P[0]:.2f},{P[1]:.2f},{P[2]:.2f})",
        (10, 30 if txt == "FIRE" else 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2,
    )
    return img
