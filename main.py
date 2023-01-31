import sys
import torch
import argparse

# Additional Scripts
from train import TrainTestPipe
from inference import SegInference


def main_pipeline(parser):
    device = 'cpu:0'
    if torch.cuda.is_available():
        device = 'cuda:0'

    if parser.mode == 'train':
        ttp = TrainTestPipe(train_path=parser.train_path,
                            test_path=parser.test_path,
                            model_path=parser.model_path,
                            device=device)

        ttp.train()

    elif parser.mode == 'inference':
        inf = SegInference(model_path=parser.model_path,
                           device=device)

        _ = inf.infer(parser.image_path)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default="train")
    parser.add_argument('--model_path', type=str, default="./path/model/ViT-B_16.npz")

    parser.add_argument('--train_path', required='train' in sys.argv,  type=str, default="./data/train")
    parser.add_argument('--test_path', required='train' in sys.argv, type=str, default="./data/test")

    parser.add_argument('--image_path', required='infer' in sys.argv, type=str, default="./data/val")
    parser = parser.parse_args()

    main_pipeline(parser)

