from gpiozero import Robot
from time import sleep

class RobotWheels:
    
    robot = Robot(left=(5, 6), right=(22, 27))
    
    def __init__(self):
        pass
    
    def move_forward(self):
        self.robot.forward(0.2)
        
    def move_backwards(self):
        self.robot.backward(0.2)
        
    def turn_right(self):
        self.robot.right(0.2)
        
    def turn_left(self):
        self.robot.left(0.2)
        
    def dance(self):
        self.move_forward()
        sleep(0.5)
        self.stop()
        self.move_backwards()
        sleep(0.5)
        self.stop()
        self.turn_right()
        sleep(0.5)
        self.stop()
        self.turn_left()
        sleep(0.5)
        self.stop()

    def stop(self):
        self.robot.stop()


if __name__=="__main__":

    robot_wheels = RobotWheels()
    robot_wheels.dance()
    
    



