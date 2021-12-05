#!/bin/bash
WORKSPACE=/home/pi/stereo_ws
set -e
source /home/pi/stereo_ws/install/setup.bash

#ros2 run v4l2_camera v4l2_camera_node --ros-args -p video_device:=/dev/video0 -r __ns:=/stereo/right &
#ros2 run v4l2_camera v4l2_camera_node --ros-args -p video_device:=/dev/video1 -r __ns:=/stereo/left
ros2 run opencv_cam opencv_cam_main --ros-args -p index:=0 -r __ns:=/stereo/right -p fps:=20 -p height:=480 -p width:=640 -p camera_info_path:=$WORKSPACE/config/calibration/camera/stereopi/stereo/right.yaml &
ros2 run opencv_cam opencv_cam_main --ros-args -p index:=1 -r __ns:=/stereo/left -p fps:=20 -p height:=480 -p width:=640 -p camera_info_path:=$WORKSPACE/config/calibration/camera/stereopi/stereo/left.yaml &
sleep 2
ros2 run image_transport republish raw --ros-args -r in:=/stereo/right/image_raw -r out/compressed:=/stereo/right/image_raw/compressed -r out/compressedDepth:=/stereo/right/image_raw/compressedDepth -r out/theora:=/stereo/right/image_raw/theora &
ros2 run image_transport republish raw --ros-args -r in:=/stereo/left/image_raw -r out/compressed:=/stereo/left/image_raw/compressed -r out/compressedDepth:=/stereo/left/image_raw/compressedDepth -r out/theora:=/stereo/left/image_raw/theora

