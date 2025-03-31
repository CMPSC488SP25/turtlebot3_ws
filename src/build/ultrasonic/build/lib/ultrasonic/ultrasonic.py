import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class UltrasonicSensorNode(Node):
    def __init__(self):
        super().__init__('ultrasonic_sensor_node')
        self.publisher_ = self.create_publisher(Range, '/ultrasonic_distance', 10)
        self.timer = self.create_timer(0.1, self.publish_distance)  # 10 Hz

    def publish_distance(self):
        distance = self.get_ultrasonic_reading()
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "ultrasonic_sensor"
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = 0.5
        msg.min_range = 0.02
        msg.max_range = 4.0
        msg.range = distance

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published distance: {distance} meters')

    def get_ultrasonic_reading(self):
        import random
        return round(random.uniform(0.02, 4.0), 2)

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicSensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
