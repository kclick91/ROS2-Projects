#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')  # Name of the node
        # Create publisher on 'chatter' topic with String type
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer_period = 10.0  # seconds
        # Timer calls self.timer_callback every 1 second
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.count = 0
        self.time = self.timer_period

    def timer_callback(self):
        msg = String()
        msg.data = f'COUNT: {self.count}, SECONDS SINCE START: {self.time}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1
        self.time += self.timer_period

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean shutdown
        minimal_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
