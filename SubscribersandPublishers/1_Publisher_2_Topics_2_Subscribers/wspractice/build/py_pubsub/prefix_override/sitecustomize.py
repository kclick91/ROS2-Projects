import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rosworker/ROS2Projects/SubscribersandPublishers/1_Publisher_2_Topics_2_Subscribers/wspractice/install/py_pubsub'
