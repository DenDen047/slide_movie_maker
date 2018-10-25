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
parser.add_argument('--pause',
    default=10,
    type=int)
args = parser.parse_args()


def main():
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter(args.output, fourcc, 20.0, (720, 405))

    # read paths of file
    files = sorted(glob.glob(os.path.join(args.input_dir, '*.png')))

    # write image
    for f in files:
        img = cv2.imread(f)
        img = cv2.resize(img, (720,405))
        # pause
        for _ in range(args.pause):
            video.write(img)

    # generate
    video.release()

if __name__ == "__main__":
    main()
