import json, numpy as np, argparse, cv2
from numpy.linalg import svd


def dlt(points):
    # points: list of {"world":[x,y,z], "pixel":[u,v]}
    A = []
    for p in points:
        x, y, z = p["world"]
        u, v = p["pixel"]
        A.append([x, y, z, 1, 0, 0, 0, 0, -u * x, -u * y, -u * z, -u])
        A.append([0, 0, 0, 0, x, y, z, 1, -v * x, -v * y, -v * z, -v])
    A = np.asarray(A)
    U, S, Vt = svd(A)
    P = Vt[-1, :].reshape(3, 4)
    # Decompose: use OpenCV's stable routine (equivalent to QR/RQ factorization)
    K, R, t, C, _, _, _ = cv2.decomposeProjectionMatrix(P)
    K = K / K[2, 2]
    R = R
    C = (C[:3] / C[3]).reshape(3, 1)
    T = -R @ C
    P2 = K @ np.hstack([R, T])
    return K, R, T, P2


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--points", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    points = json.load(open(args.points))
    K, R, T, P = dlt(points)
    np.savez(args.out, K=K, R=R, T=T, P=P)
    print(f"[OK] saved {args.out}")
