from gpiozero import DistanceSensor
from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep

distance_sensor = DistanceSensor(echo=18, trigger=17)
motion_sensor = MotionSensor(4)
led = LED(21)

while True:
    
    if(motion_sensor.motion_detected):
        blink_time=distance_sensor.distance
        led.blink(blink_time,blink_time,None,True)
    sleep(2)