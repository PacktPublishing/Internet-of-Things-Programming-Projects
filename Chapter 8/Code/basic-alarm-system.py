from gpiozero import MotionSensor
from gpiozero import Buzzer
from gpiozero import Button
from time import sleep

buzzer = Buzzer(17)
motion_sensor = MotionSensor(4)
switch = Button(8)

while True:
    if switch.is_pressed:
        if motion_sensor.motion_detected:
            buzzer.beep(0.5,0.5, None, True)
            print('Intruder Alert')
            sleep(1)
        else:
            buzzer.off()
            print('Quiet')
            sleep(1)
    else:
        buzzer.off()
        sleep(1)
        
