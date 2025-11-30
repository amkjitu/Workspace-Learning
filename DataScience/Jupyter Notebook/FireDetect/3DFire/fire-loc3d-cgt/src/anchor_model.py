import torch, torch.nn as nn, torch.nn.functional as F


class AnchorNet(nn.Module):
    # tiny CNN on ROI crops -> normalized (du,dv) and q
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, 2, 1)
        self.conv2 = nn.Conv2d(16, 32, 3, 2, 1)
        self.conv3 = nn.Conv2d(32, 64, 3, 2, 1)
        self.gap = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(64, 3)  # du, dv, q_logit

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = self.gap(x).flatten(1)
        out = self.fc(x)
        du, dv, q = out[:, 0], out[:, 1], out[:, 2]
        return du, dv, q


def size_norm(w, h):
    return 2 * w * h / (w + h + 1e-6)


def apply_anchor_heuristic(cls_name, box):
    x1, y1, x2, y2 = box
    w = x2 - x1
    h = y2 - y1
    cx = (x1 + x2) / 2
    if cls_name.lower().startswith("fire"):
        return cx, y2 - 0.10 * h, 0.4  # near base
    else:  # smoke
        return cx, y1 + 0.65 * h, 0.3  # lower portion of plume
