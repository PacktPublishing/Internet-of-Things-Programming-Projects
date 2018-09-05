import Adafruit_PCA9685
from time import sleep

pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

while True:
    pwm.set_pwm(0, 0, servo_min)
    sleep(5)
    pwm.set_pwm(0, 0, servo_max)
    sleep(5)
    
    

    
