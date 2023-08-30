import numpy as np
import os
import random
import torch
from Core.Train import train, val, test


def seed_everything(seed=6767):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def main():
    seed_everything(seed=6767)
    # for dim in [16, 32, 48, 64, 80]:
    #     for dim_mults in [[1], [1, 2], [1, 2, 4], [1, 2, 4, 8], [1, 2, 4, 8, 16]]:
    model_config = {"state": "test", "epoch": 200, "batch_size": 256, "T": 200,
                    "missing_type_train": "scatter", "missing_rate_train": 0.5,
                    "missing_type_test": "scatter", "missing_rate_test": 0.5,
                    "thres": 0.1, "dataset": "ECG", "device": "cuda:0", "w": 1,
                    "save_dir": "./Checkpoints/", "save_weight_dir": "./Checkpoints/",
                    "save_gen": False, "dropout": 0.15, "lr": 1e-4, "multiplier": 2.,
                    "beta_1": 1e-4, "beta_T": 0.02, "grad_clip": 1.}
    if not os.path.exists(model_config["save_dir"]):
        os.makedirs(model_config["save_dir"])
    if model_config["state"] == "train":
        train(model_config)
    elif model_config["state"] == "val":
        val(model_config)
    elif model_config["state"] == "test":
        test(model_config)


if __name__ == '__main__':
    main()

