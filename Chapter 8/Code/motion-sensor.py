from gpiozero import MotionSensor
from time import sleep

motion_sensor = MotionSensor(4)

while True:
    if motion_sensor.motion_detected:
        print('Dectected Motion!')
        sleep(2)
    else:
        print('No Motion Detected!')
        sleep(2)


        
