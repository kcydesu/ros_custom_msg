# ros_custom_msg
A repository to hold instructions to create a custom ros message and an example subscriber.

# Before you start
This guide assumes that you have created a catkin_workspace already and have also already created a package. My workspace was called '''catkin_ws''' and my package was called '''templecar'''.

# Creating the message
The first step in creating your custom message type is to enter your package and create a new directory to hold custom messages. 
'''
roscd templecar
mkdir msg
'''
Next, you can enter this directory, create a file that contains your custom message type.
'''
cd msg
touch Drive.msg
sudo nano Drive.msg
'''
Now you can add the two elements of our message that we would like.
(In Drive.msg)
```
float32 steering
float32 speed
```

# Setting up the workspace
Now, we need to make sure that we tell our workspace to generate and use these custom message types. We can do this by first editing the *package.xml* file to include the following lines (if it doesn't already).
'''
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
'''
Next we need to make a few edits to *CMakeLists.txt*.
First add '''message_generation''' to the find dependencies as shown below.
'''
# Do not just add this to your CMakeLists.txt, modify the existing text to add message_generation before the closing parenthesis
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)
'''
Next, make sure that we export the runtime dependency.
'''
catkin_package(
  ...
  CATKIN_DEPENDS message_runtime ...
  ...)
'''
Finally, add the following block of code to the end of the file.
'''
add_message_files(
  FILES
  Drive.msg
)
'''
After this, run the following commands inside your catkin_ws.
'''
catkin_make
source devel/setup.bash
'''
