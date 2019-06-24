import os
import threading
import time
import sys


the_json_file = 'lesson_1.json'
ROBOT = 'robotod' # 'nao'


def intro(group_id=0, nao_ip='192.168.0.103'):
    start_working(group_id, nao_ip)

    time.sleep(60)


def start_working(group_id, nao_ip):

    def worker0():
        os.system('roscore')
        threading._sleep(1.0)
        return

    def worker1():
        os.system('python ~/PycharmProjects/twisted_server_ros_2_0/scripts/nao_ros_listener.py ' + nao_ip)
        # os.system('python ~/pycharm/curious_game/nao_ros.py ' + nao_ip)
        return

    def worker2():
        os.system('python ~/PycharmProjects/twisted_server_ros_2_0/scripts/robotod_ros_listener.py')
        # os.system('python ~/pycharm/curious_game/nao_ros.py ' + nao_ip)
        return

    def worker10():
        os.system('python manager_node.py %s %s' % (the_json_file, ROBOT))

    def worker12():
        os.system('rostopic pub -1 /to_manager std_msgs/String "start"')

    threading.Thread(target=worker0).start()

    if ROBOT == 'robotod':
        t1 = threading.Thread(target=worker2)
        t1.start()
        threading._sleep(2.5)
    elif ROBOT == 'nao':
        t1 = threading.Thread(target=worker1)
        t1.start()
        threading._sleep(2.5)

    t10 = threading.Thread(target=worker10)
    t10.start()
    threading._sleep(0.5)

    lecture_number = raw_input('Press any key to start ...')

    t12 = threading.Thread(target=worker12)
    t12.start()
    threading._sleep(0.2)


if len(sys.argv) > 1:
    print('sys.argv', sys.argv)
    intro(int(sys.argv[1]), sys.argv[2])
else:
    intro()