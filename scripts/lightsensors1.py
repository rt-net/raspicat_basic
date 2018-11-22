#!/usr/bin/env python
import sys, rospy
from raspicat_basic.msg import LightSensorValues

rospy.init_node('lightsensors')

# Copyright 2016 Ryuichi Ueda
# Released under the BSD License.
# To make line numbers be identical with the book, this statement is written here. Don't move it to the header.
