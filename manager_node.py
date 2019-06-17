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
            self.sound_suffix = '.wav'
            self.robot_behavior_path = 'animations/Stand/Gestures/'
        elif ROBOT == 'robotod':
            self.robot_publisher = rospy.Publisher('to_robotod', String, queue_size=10)
            self.robot_sound_path = '../../catkin_ws/src/ROS_recorder/sounds/shorashim/'
            self.sound_suffix = ''
            self.robot_behavior_path = '../../catkin_ws/src/ROS_recorder/blocks/shorashim/'

        rospy.Subscriber('to_manager', String, self.manage)

        rospy.spin()

    def manage(self, data):
        print('ManagerNode: ', data.data)
        self.load_script()
        self.run_script()

    def load_script(self):
        self.script = json.load(open('lesson_1.json'))
        print('The script:', self.script)

    def run_script(self):

        for s in self.script:
            robot_message = {
                'action': 'run_behavior_and_sound',
                'parameters': [self.robot_behavior_path + s['behavior'],
                               self.robot_sound_path + s['sound'] + self.sound_suffix]
            }
            self.robot_publisher.publish(json.dumps(robot_message))

mn = ManagerNode()
