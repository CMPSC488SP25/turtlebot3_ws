import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/shared/students/turtlebot3_ws/install/ultrasonic_sensor'
