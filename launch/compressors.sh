#!/bin/bash
WORKSPACE=/home/pi/stereo_ws
set -e
source /home/pi/stereo_ws/install/setup.bash

ros2 run image_transport republish raw --ros-args -r in:=/right/image_raw -r out/compressed:=/right/image_raw/compressed -r out/compressedDepth:=/right/image_raw/compressedDepth -r out/theora:=/right/image_raw/theora &
ros2 run image_transport republish raw --ros-args -r in:=/left/image_raw -r out/compressed:=/left/image_raw/compressed -r out/compressedDepth:=/left/image_raw/compressedDepth -r out/theora:=/left/image_raw/theora

