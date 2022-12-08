import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

def cd(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "person", cd, 10)

rclpy.spin(node)

