# ObjectDetection
In this package you can use a Xbox Kinect for Object/Person Detection. 

It uses PointCloud data received from the kinect to analyse the distance of objects. 
These objects are clustered with a maximum of 6 objects.

Requirements:
  - install the Freenect drivers or the OpenNI drivers
  - the kin_dis_test.py node
  
Steps:
  - run 'roslaunch freenect_launch freenect.launch
    or:
    run 'roslaunch openni_launch openni.launch
  - go to the folder where kin_dis_test.py is located
  - run 'python kin_dis_test.py'
