import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():          #ヘッダの下にTalkerというクラスを作成
      def __init__(self):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0

rclpy.init()
node = Node("talker")
talker = Talker()

def cd():
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)
    talker.n += 1

node.create_timer(0.5, cd)
rclpy.spin(node)

