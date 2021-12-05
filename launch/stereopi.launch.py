# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Software License Agreement (BSD License 2.0)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

import launch_ros.actions
import launch_ros.descriptions
#ros2 run opencv_cam opencv_cam_main --ros-args -p index:=0 -r __ns:=/stereo/right -p fps:=20 -p height:=480 -p width:=640 -p camera_info_path:=$WORKSPACE/config/calibration/camera/stereopi/stereo/right.yaml &
#ros2 run opencv_cam opencv_cam_main --ros-args -p index:=1 -r __ns:=/stereo/left -p fps:=20 -p height:=480 -p width:=640 -p camera_info_path:=$WORKSPACE/config/calibration/camera/stereopi/stereo/left.yaml &
#sleep 2
#ros2 run image_transport republish raw --ros-args -r in:=/stereo/right/image_raw -r out/compressed:=/stereo/right/image_raw/compressed -r out/compressedDepth:=/stereo/right/image_raw/compressedDepth -r out/theora$
#ros2 run image_transport republish raw --ros-args -r in:=/stereo/left/image_raw -r out/compressed:=/stereo/left/image_raw/compressed -r out/compressedDepth:=/stereo/left/image_raw/compressedDepth -r out/theora:=/$

#TODO put as launch params
FPS=1
CALIBRATION_PATH='/home/pi/stereo_ws/config/calibration'
WIDTH=640
HEIGHT=480
def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.ComposableNodeContainer(
            name='container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                # Driver itself
                launch_ros.descriptions.ComposableNode(
                    package='opencv_cam',
                    plugin='opencv_cam::OpencvCamNode',
                    name='opencv_cam_left',
                    namespace='/left',
                    parameters=[ 
                        {'index':0},
                        {'fps':FPS},
                        {'height':HEIGHT},
                        {'width':WIDTH},
                        {'camera_info_path':CALIBRATION_PATH+'/camera/stereopi/stereo/left.yaml'},
                    ]
                ),
                launch_ros.descriptions.ComposableNode(
                    package='opencv_cam',
                    plugin='opencv_cam::OpencvCamNode',
                    name='opencv_cam_right',
                    namespace='/right',
                    parameters=[ 
                        {'index':1},
                        {'fps':FPS},
                        {'height':HEIGHT},
                        {'width':WIDTH},
                        {'camera_info_path':CALIBRATION_PATH+'/camera/stereopi/stereo/right.yaml'},
                    ]
                ),
                launch_ros.descriptions.ComposableNode(
                    package='stereo_image_proc',
                    plugin='stereo_image_proc::DisparityNode',
                    name='disparity_node',
                    namespace='',
                    remappings=[
                        ('/left/image_rect','/left/image_raw'),
                        ('/right/image_rect','/right/image_raw')
                    ],
                    parameters=[
                        {"approximate_sync":True}
                    ]
                )

            ],
            output='screen',
        ),
    ])

