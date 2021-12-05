#!/bin/bash

set -e
source /workspaces/ws/install/setup.bash

ros2 run image_transport republish compressed --ros-args -r in/compressed:=/left/image_raw/compressed -r out:=/left/image_raw/uncompressed &
ros2 run image_transport republish compressed --ros-args -r in/compressed:=/right/image_raw/compressed -r out:=/right/image_raw/uncompressed
