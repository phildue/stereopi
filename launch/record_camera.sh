#!/bin/bash

set -e
source /home/pi/stereo_ws/install/setup.bash

ros2 run v4l2_camera v4l2_camera_node --ros-args -p video_device:=/dev/video0 -r __ns:=/stereo/right &
ros2 run v4l2_camera v4l2_camera_node --ros-args -p video_device:=/dev/video1 -r __ns:=/stereo/left &
sleep 5
ros2 bag record "/stereo/left/camera_info" "/stereo/left/image_raw/compressed" "/stereo/right/image_raw/compressed" "stereo/right/camera_info"

