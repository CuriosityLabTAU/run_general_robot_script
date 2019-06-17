import json
import rospy
from std_msgs.msg import String
import threading
from condition import *


the_lecture_flow_json_file = 'flow_files/"robotator_study.json"'


class ManagerNode():


    def __init__(self):
        rospy.init_node('manager_node') #init a listener:

        if ROBOT == 'nao':
            self.robot_publisher = rospy.Publisher('to_nao', String, queue_size=10)
            self.robot_sound_path = '/home/nao/naoqi/sounds/HCI/'
            self.robot_behavior_path = 'animations/Stand/Gestures/'
        elif ROBOT == 'robotod':
            self.robot_publisher = rospy.Publisher('to_robotod', String, queue_size=10)
            self.robot_sound_path = '../../catkin_ws/src/ROS_recorder/sounds/shorashim/'
            self.robot_behavior_path = '../../catkin_ws/src/ROS_recorder/blocks/shorashim/'

        rospy.Subscriber('to_manager', String, self.manage)

        rospy.spin()

    def manage(self, data):
        print('ManagerNode: ', data.data)
        self.run_script()

    def run_script(self):
        # robot_message = {'action': 'print_installed_behaviors'}

        # # NAO
        # robot_message = {
        #     'action': 'run_behavior_and_sound',
        #     'parameters': [self.robot_behavior_path + 'Explain_1',
        #                    self.robot_sound_path + 'general_next_statement.wav']
        # }

        # Robotod
        robot_message = {
            'action': 'run_behavior_and_sound',
            'parameters': [self.robot_behavior_path + 'explain_3',
                           self.robot_sound_path + 'explain_3']
        }


        self.robot_publisher.publish(json.dumps(robot_message))

mn = ManagerNode()
