#!/bin/bash

set -e
source /workspaces/ws/install/setup.bash
CAM_NAME=${1:-"left"}

ros2 run camera_calibration cameracalibrator \
  --size=6x9 \
  --square=0.025 \
  --no-service-check \
  --camera_name="stereopi_$CAM_NAME" \
  /image:=/stereo/$CAM_NAME/image_raw/uncompressed