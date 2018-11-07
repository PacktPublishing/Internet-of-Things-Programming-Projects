from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=17, green=27, blue=22, active_high=False)

while True:
    led.color=(1,0,0)
    print("red")
    sleep(2)
    led.color=(0,1,0)
    print("green")
    sleep(2)
    led.color=(0,0,1)
    print("blue")
    sleep(2)
    led.off()
    print("blue")
    sleep(2)