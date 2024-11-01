#import ROS related packages
import rclpy
from rclpy.node import Node

#import std_message for transport
# TODO:Customize CAN message Data field 
from can_msg.msg import OdriveCAN


class CAN_Message_Parser(Node):
    
    def __init__(self):
        super().__init__('can_message_parser')
        print("CAN Gateway started")
        self.subscription = self.create_subscription(
            OdriveCAN,
            'topic',
            self.listener_callback,
            10 )
        self.subscription #IGNORE: supress unused variable warning
        
    def listener_callback(self, msg):
        
        self.get_logger().info('Message Receiver: "%s"' %msg.message.arbitration_id)
        
      
        
def main(args = None):
    rclpy.init(args=args)

    can_message_parser = CAN_Message_Parser()

    rclpy.spin(can_message_parser)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    can_message_parser.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
    