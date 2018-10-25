# -*- coding: utf-8 -*-
import os
import cv2
import glob
import argparse


parser = argparse.ArgumentParser(description='This script is ...')
parser.add_argument('--input_dir',
    action='store',
    type=str)
parser.add_argument('--output',
    action='store',
    default='video.mp4',
    type=str)
args = parser.parse_args()


def main():
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter(args.output, fourcc, 20.0, (720, 405))

    # read paths of file
    files = glob.glob(os.path.join(args.input_dir, '*.png'))

    for f in files:
        img = cv2.imread(f)
        img = cv2.resize(img, (720,405))
        video.write(img)

    video.release()

if __name__ == "__main__":
    main()
