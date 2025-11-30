import numpy as np, json


def load_calib(npz_path):
    D = np.load(npz_path)
    return D["K"], D["R"], D["T"], D["P"]


def load_planes(json_path):
    J = json.load(open(json_path))
    out = {}
    for k, v in J.items():
        out[k] = {"n": np.array(v["n"], dtype=float), "b": float(v["b"])}
    return out
