# Copyright 2022 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import namedtuple

Mapping = namedtuple('Mapping', ('ros_type', 'ign_type'))

# List of known mappings
#
# The pattern for adding a new mapping
#
#   'ros2_package_name': [
#       Mapping('ros2_message_name', 'ignition_message_name'),
#   ],
MAPPINGS = {
    'builtin_interfaces': [
        Mapping('Time', 'Time'),
    ],
    'geometry_msgs': [
        Mapping('Point', 'Vector3d'),
        Mapping('Pose', 'Pose'),
        Mapping('PoseStamped', 'Pose'),
        Mapping('PoseWithCovariance', 'PoseWithCovariance'),
        Mapping('Quaternion', 'Quaternion'),
        Mapping('Transform', 'Pose'),
        Mapping('TransformStamped', 'Pose'),
        Mapping('Twist', 'Twist'),
        Mapping('TwistWithCovariance', 'TwistWithCovariance'),
        Mapping('Vector3', 'Vector3d'),
        Mapping('Wrench', 'Wrench'),
    ],
    'nav_msgs': [
        Mapping('Odometry', 'Odometry'),
        Mapping('Odometry', 'OdometryWithCovariance'),
    ],
    'ros_ign_interfaces': [
        Mapping('Contact', 'Contact'),
        Mapping('Contacts', 'Contacts'),
        Mapping('Entity', 'Entity'),
        Mapping('GuiCamera', 'GUICamera'),
        Mapping('JointWrench', 'JointWrench'),
        Mapping('Light', 'Light'),
        Mapping('StringVec', 'StringMsg_V'),
        Mapping('TrackVisual', 'TrackVisual'),
        Mapping('VideoRecord', 'VideoRecord'),
        Mapping('WorldControl', 'WorldControl'),
    ],
    'rosgraph_msgs': [
        Mapping('Clock', 'Clock'),
    ],
    'sensor_msgs': [
        Mapping('FluidPressure', 'FluidPressure'),
        Mapping('Image', 'Image'),
        Mapping('CameraInfo', 'CameraInfo'),
        Mapping('Imu', 'IMU'),
        Mapping('JointState', 'Model'),
        Mapping('LaserScan', 'LaserScan'),
        Mapping('MagneticField', 'Magnetometer'),
        Mapping('PointCloud2', 'PointCloudPacked'),
        Mapping('BatteryState', 'BatteryState'),
    ],
    'std_msgs': [
        Mapping('Bool', 'Boolean'),
        Mapping('ColorRGBA', 'Color'),
        Mapping('Empty', 'Empty'),
        Mapping('Float32', 'Float'),
        Mapping('Float64', 'Double'),
        Mapping('Header', 'Header'),
        Mapping('Int32', 'Int32'),
        Mapping('UInt32', 'UInt32'),
        Mapping('String', 'StringMsg'),
    ],
    'tf2_msgs': [
        Mapping('TFMessage', 'Pose_V'),
    ],
    'trajectory_msgs': [
        Mapping('JointTrajectory', 'JointTrajectory'),
    ],
}

MAPPINGS_8_4_0 = {
    'ros_ign_interfaces': [
        Mapping('Dataframe', 'Dataframe'),
    ],
}