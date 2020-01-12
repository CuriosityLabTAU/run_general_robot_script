import json
import rospy
from std_msgs.msg import String
import sys
import time



class ManagerNode():


    def __init__(self, lesson='lesson_1', ROBOT='patricc', the_path=''):
        self.the_json_file = lesson + '.json'
        self.the_path = the_path
        self.ROBOT = ROBOT
        rospy.init_node('manager_node') #init a listener:

        self.ROBOT == 'patricc'
        self.robot_publisher = rospy.Publisher('to_robotod', String, queue_size=10)
        self.robot_sound_path = '%s/sounds/' % self.the_path
        self.sound_suffix = ''
        self.robot_behavior_path = '%s/blocks/' % self.the_path

        rospy.Subscriber('to_manager', String, self.manage)

        rospy.spin()

    def manage(self, data):
        print('ManagerNode: ', data.data)
        self.load_script()
        self.run_script()

    def load_script(self):
        self.script = json.load(open(self.the_json_file))
        print('The script:', self.script)

    def run_script(self):

        for s in self.script:
            robot_message = {
                'action': 'run_behavior_and_sound',
                'parameters': []
            }
            if 'behavior' in s:
                robot_message['parameters'].append(self.robot_behavior_path + s['behavior'])
            else:
                robot_message['parameters'].append('')

            if 'sound' in s:
                robot_message['parameters'].append(self.robot_sound_path + s['sound'] + self.sound_suffix)
            else:
                robot_message['parameters'].append('')

            if 'lip' in s:
                robot_message['parameters'].append(self.robot_sound_path + s['lip'] + self.sound_suffix)
            else:
                robot_message['parameters'].append(self.robot_sound_path + s['sound'] + self.sound_suffix)


            self.robot_publisher.publish(json.dumps(robot_message))
            time.sleep(7)


if len(sys.argv) > 1:
    print('sys.argv', sys.argv)
    mn = ManagerNode(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    mn = ManagerNode()

