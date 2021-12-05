#!/bin/bash

set -e
source /workspaces/ws/install/setup.bash

ros2 run camera_calibration cameracalibrator \
  --size=6x9 \
  --square=0.025 \
  --approximate=0.3 \
  --no-service-check \
  /left:=/stereo/left/image_raw/uncompressed \
  /right:=/stereo/right/image_raw/uncompressed