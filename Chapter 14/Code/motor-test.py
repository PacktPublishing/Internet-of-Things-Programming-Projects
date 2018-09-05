from gpiozero import Robot
from time import sleep

robot = Robot(left=(5, 6), right=(22, 27))

robot.forward(0.2)
sleep(0.5)
robot.backward(0.2)
sleep(0.5)
robot.stop()




