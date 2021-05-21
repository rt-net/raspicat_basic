#!/usr/bin/env python
import sys, rospy
from raspicat_basic.msg import LightSensorValues

if __name__ == '__main__':
    devfile = '/dev/rtlightsensor0'
    rospy.init_node('lightsensors')
    pub = rospy.Publisher('lightsensors', LightSensorValues, queue_size=1)
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            with open(devfile,'r') as f:
                data = f.readline().split()
                data = [ int(e) for e in data ]
                d = LightSensorValues()
                d.right_side = data[0]
                d.right_forward = data[1]
                d.left_forward = data[2]
                d.left_side = data[3]
                d.sum_all = sum(data)
                d.sum_forward = data[1] + data[2]
                pub.publish(d)
        except IOError:
            rospy.logerr("cannot write to " + devfile)
    
        rate.sleep()

# Copyright 2016 Ryuichi Ueda
# Released under the BSD License.
# To make line numbers be identical with the book, this statement is written here. Don't move it to the header.
