# ObjectDetection
In this package you can use a Xbox Kinect for Object/Person Detection. 

It uses PointCloud data received from the kinect to analyse the distance of objects. 
These objects are clustered with a maximum of 6 objects.

Requirements:
  - install the Freenect drivers or the OpenNI drivers:
  - https://github.com/OpenKinect/libfreenect#build-instructions
  - https://github.com/OpenNI/OpenNI
  - the kin_dis_test.py script
  
Steps:
  - make sure the Xbox Kinect is connected
  - run 'roslaunch freenect_launch freenect.launch'   or   'roslaunch openni_launch openni.launch
  - go to the folder where kin_dis_test.py is located
  - run 'python kin_dis_test.py'
  
When running the program, the Topic 'DetectedObjects' will represent a MarkerArray with all the detected Objects.
The x, y and z coordinates and scale of the detected objects are found in this MarkerArray.

To verify the PointCloud data is received correctly from the kinect
  - run 'rosrun rviz rviz'
  - in 'Global Options' set the 'Fixed Frame' to 'camera_depth_frame'
  - add PointCloud2
  
To see distance:
  - set as topic: 'camera/depth/points'
  - set intensity as z
  
To combine PointCloud with camera:
  - set as topic: 'camera/depth/points_registered
  - set color transform: 'RGB8'
  
