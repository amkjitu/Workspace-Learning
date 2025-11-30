import yaml, argparse
from src.localize3d import localize_pair

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/cameras.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config))
    localize_pair(cfg)
