#!/usr/bin/env python
from roslib import message
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
import time
from geometry_msgs.msg import Pose, PoseArray
from visualization_msgs.msg import Marker, MarkerArray
 
# Subscribe to PointCloud2 Topic:
def listen():

    rospy.init_node('listen', anonymous=True)
    rospy.Subscriber("/camera/depth/points", PointCloud2, callback_kinect1)
    rospy.spin()
 


def callback_kinect1(data):

#Publish the Topic 'DetectedObjects' as MarkerArray
    pose_pub = rospy.Publisher("DetectedObjects", MarkerArray, queue_size=50)
    pose1 = Marker()
    pose2 = Marker()
    pose3 = Marker()
    pose4 = Marker()
    pose5 = Marker()
    pose6 = Marker()
    pose_array = MarkerArray()
#

#Variables
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    i = 0

    #Minimum distance before detection
    zMinimum = 2.2

    #Difference in seperation of objects
    xDif = 0.3
    yDif = 0.3
    zDif = 0.3

    xArray = []
    yArray = []
    zArray = []
    xArray2 = []
    yArray2 = []
    zArray2 = []
    xArray3 = []
    yArray3 = []
    zArray3 = []
    xArray4 = []
    yArray4 = []
    zArray4 = []
    xArray5 = []
    yArray5 = []
    zArray5 = []
    xArray6 = []
    yArray6 = []
    zArray6 = []
#


    for p in pc2.read_points(data, field_names = ("x", "y", "z"), skip_nans=True):
        i = i + 1
        # all data within the zMin marker will be added to the x, y or z Array
        if(p[2] <= zMinimum):
            a = a + 1
            #print(a)
            if (a == 1):
                xArray.append(p[0])
                yArray.append(p[1])
                zArray.append(p[2])
            elif ((zArray[-1]-zDif)<p[2]<(zArray[-1]+zDif)) and (((xArray[-1]-xDif)<p[0]<(xArray[-1]+xDif)) or ((xArray[0]-xDif)<p[0]<(xArray[0]+xDif))) and ((yArray[-1]-yDif)<p[1]<(yArray[-1]+yDif)):
                xArray.append(p[0])
                yArray.append(p[1])
                zArray.append(p[2])
            else:
                b = b + 1
                if (b == 1):
                    xArray2.append(p[0])
                    yArray2.append(p[1])
                    zArray2.append(p[2])
                elif ((zArray2[-1]-zDif)<p[2]<(zArray2[-1]+zDif)) and (((xArray2[-1]-xDif)<p[0]<(xArray2[-1]+xDif)) or ((xArray2[0]-xDif)<p[0]<(xArray2[0]+xDif)))  and ((yArray2[-1]-yDif)<p[1]<(yArray2[-1]+yDif)):
                    xArray2.append(p[0])
                    yArray2.append(p[1])
                    zArray2.append(p[2])
                else:
                    c = c + 1
                    if (c == 1):
                        xArray3.append(p[0])
                        yArray3.append(p[1])
                        zArray3.append(p[2])
                    elif ((zArray3[-1]-zDif)<p[2]<(zArray3[-1]+zDif)) and (((xArray3[-1]-xDif)<p[0]<(xArray3[-1]+xDif)) or ((xArray3[0]-xDif)<p[0]<(xArray3[0]+xDif))) and ((yArray3[-1]-yDif)<p[1]<(yArray3[-1]+yDif)):
                        xArray3.append(p[0])
                        yArray3.append(p[1])
                        zArray3.append(p[2])
                    else:
                        d = d + 1
                        if (d == 1):
                            xArray4.append(p[0])
                            yArray4.append(p[1])
                            zArray4.append(p[2])
                        elif ((zArray4[-1]-zDif)<p[2]<(zArray4[-1]+zDif)) and (((xArray4[-1]-xDif)<p[0]<(xArray4[-1]+xDif)) or ((xArray4[0]-xDif)<p[0]<(xArray4[0]+xDif))) and ((yArray4[-1]-yDif)<p[1]<(yArray4[-1]+yDif)):
                            xArray4.append(p[0])
                            yArray4.append(p[1])
                            zArray4.append(p[2])
                        else:
                            e = e + 1
                            if (e == 1):
                                xArray5.append(p[0])
                                yArray5.append(p[1])
                                zArray5.append(p[2])
                            elif ((zArray5[-1]-zDif)<p[2]<(zArray5[-1]+zDif)) and (((xArray5[-1]-xDif)<p[0]<(xArray5[-1]+xDif)) or ((xArray5[0]-xDif)<p[0]<(xArray5[0]+xDif))) and ((yArray5[-1]-yDif)<p[1]<(yArray5[-1]+yDif)):
                                xArray5.append(p[0])
                                yArray5.append(p[1])
                                zArray5.append(p[2])
                            else:
                                f = f + 1
                                if (f == 1):
                                    xArray6.append(p[0])
                                    yArray6.append(p[1])
                                    zArray6.append(p[2])
                                elif ((zArray6[-1]-zDif)<p[2]<(zArray6[-1]+zDif)) and (((xArray6[-1]-xDif)<p[0]<(xArray6[-1]+xDif)) or ((xArray6[0]-xDif)<p[0]<(xArray6[0]+xDif))) and ((yArray6[-1]-yDif)<p[1]<(yArray6[-1]+yDif)):
                                    xArray6.append(p[0])
                                    yArray6.append(p[1])
                                    zArray6.append(p[2])
    
    if (len(zArray) > 1000):
        xMax = max(xArray)
        xMin = min(xArray)
        yMax = max(yArray)
        yMin = min(yArray)
        zMin = min(zArray)

    if (len(zArray2) > 1000):
        xMax2 = max(xArray2)
        xMin2 = min(xArray2)
        yMax2 = max(yArray2)
        yMin2 = min(yArray2)
        zMin2 = min(zArray2)

    if (len(zArray3) > 1000):
        xMax3 = max(xArray3)
        xMin3 = min(xArray3)
        yMax3 = max(yArray3)
        yMin3 = min(yArray3)
        zMin3 = min(zArray3)

    if (len(zArray4) > 1000):
        xMax4 = max(xArray4)
        xMin4 = min(xArray4)
        yMax4 = max(yArray4)
        yMin4 = min(yArray4)
        zMin4 = min(zArray4)

    if (len(zArray5) > 1000):
        xMax5 = max(xArray5)
        xMin5 = min(xArray5)
        yMax5 = max(yArray5)
        yMin5 = min(yArray5)
        zMin5 = min(zArray5)

    if (len(zArray6) > 1000):
        xMax6 = max(xArray6)
        xMin6 = min(xArray6)
        yMax6 = max(yArray6)
        yMin6 = min(yArray6)
        zMin6 = min(zArray6)

    print("==============")
    print("1:", len(zArray))
    print(" ")
    print("2:", len(zArray2))
    print(" ")
    print("3:", len(zArray3))
    print(" ")
    print("4:", len(zArray4))
    print(" ")
    print("5:", len(zArray5))
    print(" ")
    print("6:", len(zArray6))
    print("==============")


#####################################################
#          PUBLISH RESULTS TO POSE TOPIC            #

    if (i < 60000):
        pose1.pose.position.x = 0
        pose1.pose.position.z = 0.1
        pose1.pose.position.y = 0
        pose1.scale.x = 1
        pose1.scale.z = 1
        pose1.scale.y = 1
        pose_array.markers.append(pose1)
        pose_pub.publish(pose_array)
    else:
        if (len(zArray) > 1000):
            pose1.pose.position.x = zMin + 0.2
            pose1.pose.position.z = (yMax+yMin)/2
            pose1.pose.position.y = -(xMax+xMin)/2
            pose1.scale.x = 1
            pose1.scale.z = yMax - yMin
            pose1.scale.y = xMax - xMin
            pose1.color.r = 255
            pose1.color.g = 255
            pose1.color.b = 0
            pose_array.markers.append(pose1)

        if (len(zArray2) > 1000):
            pose2.pose.position.x = zMin2 + 0.2
            pose2.pose.position.z = (yMax2+yMin2)/2
            pose2.pose.position.y = -(xMax2+xMin2)/2
            pose2.scale.x = 1
            pose2.scale.z = yMax2 - yMin2
            pose2.scale.y = xMax2 - xMin2
            pose2.color.r = 255
            pose2.color.g = 0
            pose2.color.b = 0
            pose_array.markers.append(pose2)

        if (len(zArray3) > 1000):
            pose3.pose.position.x = zMin3 + 0.2
            pose3.pose.position.z = (yMax3+yMin3)/2
            pose3.pose.position.y = (xMax3+xMin3)/2
            pose3.scale.x = 1
            pose3.scale.z = yMax3 - yMin3
            pose3.scale.y = xMax3 - xMin3
            pose3.color.r = 0
            pose3.color.g = 255
            pose3.color.b = 0
            pose_array.markers.append(pose3)

        if (len(zArray4) > 1000):
            pose4.pose.position.x = zMin4 + 0.2
            pose4.pose.position.z = (yMax4+yMin4)/2
            pose4.pose.position.y = (xMax4+xMin4)/2
            pose4.scale.x = 1
            pose4.scale.z = yMax4 - yMin4
            pose4.scale.y = xMax4 - xMin4
            pose4.color.r = 0
            pose4.color.g = 0
            pose4.color.b = 255
            pose_array.markers.append(pose4)

        if (len(zArray5) > 1000):   
            pose5.pose.position.x = zMin5 + 0.2
            pose5.pose.position.z = (yMax5+yMin5)/2
            pose5.pose.position.y = -(xMax5+xMin5)/2
            pose5.scale.x = 1
            pose5.scale.z = yMax5 - yMin5
            pose5.scale.y = xMax5 - xMin5
            pose5.color.r = 0
            pose5.color.g = 255
            pose5.color.b = 255
            pose_array.markers.append(pose5)

        if (len(zArray6) > 1000):   
            pose6.pose.position.x = zMin6 + 0.2
            pose6.pose.position.z = (yMax6+yMin6)/2
            pose6.pose.position.y = -(xMax6+xMin6)/2
            pose6.scale.x = 1
            pose6.scale.z = yMax6 - yMin6
            pose6.scale.y = xMax6 - xMin6
            pose6.color.r = 255
            pose6.color.g = 0
            pose6.color.b = 255
            pose_array.markers.append(pose6)

        pose_pub.publish(pose_array)

#                                                   #
#####################################################
 
if __name__ == '__main__':
    try:
        listen()
    except rospy.ROSInterruptException:
        pass

