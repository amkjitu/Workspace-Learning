import numpy as np


def simple_nearest(detsL, detsR, max_dv=40):
    pairs = []
    used = set()
    for i, (clsL, boxL, confL) in enumerate(detsL):
        cyL = (boxL[1] + boxL[3]) / 2
        cand = [
            (j, abs((boxR[1] + boxR[3]) / 2 - cyL))
            for j, (clsR, boxR, confR) in enumerate(detsR)
            if j not in used and clsR == clsL
        ]
        if not cand:
            continue
        j, dv = min(cand, key=lambda t: t[1])
        if dv <= max_dv:
            pairs.append((i, j))
            used.add(j)
    return pairs


def fundamental_from_KRT(KL, RL, TL, KR, RR, TR):
    # relative pose from Left to Right
    R = RR @ RL.T
    C_L = (-RL.T @ TL).reshape(3)
    C_R = (-RR.T @ TR).reshape(3)
    t = C_R - R @ C_L
    tx = np.array([[0, -t[2], t[1]], [t[2], 0, -t[0]], [-t[1], t[0], 0]])
    F = np.linalg.inv(KR).T @ tx @ R @ np.linalg.inv(KL)
    return F


def epipolar_pairs(detsL, detsR, F, tol=2.0):
    pairs = []
    used = set()

    def pt_center(box):
        return np.array([(box[0] + box[2]) / 2, (box[1] + box[3]) / 2, 1.0])

    for i, (clsL, boxL, _) in enumerate(detsL):
        pL = pt_center(boxL)
        lR = F @ pL
        bestj, besterr = -1, 1e9
        for j, (clsR, boxR, _) in enumerate(detsR):
            if j in used or clsR != clsL:
                continue
            pR = pt_center(boxR)
            err = abs(lR @ pR) / np.sqrt(lR[0] ** 2 + lR[1] ** 2 + 1e-12)
            if err < besterr:
                besterr, bestj = err, j
        if bestj >= 0 and besterr < tol:
            pairs.append((i, bestj))
            used.add(bestj)
    return pairs
