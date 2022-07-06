Thesis title: Learning sequential manipulation skills from human demonstration for 3D printing automation

Thesis content till now:
(1) Robot target detection platform: panda arm, detection platform, Intel RealSense D435i camera and server

(2) Localization and classification: using YOLOv5-network combined with camera to do object classification and object localization

(2.1) Object classification: First, we need to collect our own object images(3d printed objects) to make a new data set, and divide it into training set (90%), validation set, and test set. The data format of the Voc dataset, including the object name and the basic information of the tag box. Use labelImg to label the corresponding xml file, and then extract the box information from each xml label into txt format. Each image corresponds to a txt file, and each line of the file is the information of a target, including the format of class, x coordinate center, y coordinate center, width, and height. Then, train the YOLOv5 model on the dataset. Finally, the object images are classified to improve the accuracy and precision of object classification.

(2.2) Object location: Use the depth camera to obtain the position and depth information of the object. Second, calculate the 3D pose of the object. Then, the relative pose transformation matrix between each coordinate system is obtained by using the hand-eye calibration method. In this experiment, the camera is fixedly mounted next to the robot, we need to find the transformation from the camera coordinate system to the robot base coordinate system, so that anything found in the camera coordinates can be easily transformed into the robot's system, Establish a stable relationship between the camera, the robotic arm, and the object. Therefore, we use the ("Eye-To-Hand") method to locate the target object. Finally, the three-dimensional pose of the object relative to the robot is obtained through the pose transformation matrix.

(3) Control robot arm to reach to the object: drag the robot arm to reach to the first target and collect the responding cartesian coordinates,  joint coordinates, velocity and acceleration information and do smooth trajectory by frankx ruckig, and then use these coordinates to control robot moving(but there is still problem for discontinous velocity) , and read the localization of other  targets on the table, change the target localization and reproduce similar trajectory by using method of Dynamic motion primitives. And we can set the time for different motion to achieve a repeated pick and place.


