#!/bin/bash

set -e
source /home/pi/stereo_ws/install/setup.bash

/home/pi/stereo_ws/scripts/camera_drivers.sh &
sleep 2
ros2 run stereo_image_proc disparity_node --ros-args -r __ns:=/stereo -r /stereo/left/image_rect:=/stereo/left/image_raw -r /stereo/right/image_rect:=/stereo/right/image_raw

#ros2 run stereo_image_proc point_cloud_node --ros-args -r __ns:=/stereo -r /left/image_rect:=/left/image_raw -r /right/image_rect:=/right/image_raw
#sleep 5

#ros2 run image_transport republish in_transport --ros-args -r in:=/stereo/left/image_rect -r out:=/stereo/left/image_rect/compressed &
#sleep 1

#ros2 run image_transport republish in_transport --ros-args -r in:=/stereo/right/image_rect -r out:=/stereo/right/image_rect/compressed
