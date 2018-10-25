#!/bin/bash

IMAGE=jjanzic/docker-python3-opencv
CMD="python3 src/main.py \
    --input_dir input \
    --output output/video.mp4
"

docker run -it --rm \
    -v ${PWD}:/root/work \
    -w /root/work \
    ${IMAGE} \
    /bin/bash -c "${CMD}"
