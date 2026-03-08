import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rosworker/ROS2Projects/SubscribersandPublishers/3 Publishers and 1 Subscriber to a topic/wspractice/install/my_first_package'
