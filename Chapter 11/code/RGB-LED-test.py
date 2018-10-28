from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=17, green=27, blue=22)

while True:
    led.color=(1,0,0)
    sleep(2)
    led.color=(0,1,0)
    sleep(2)
    led.color=(0,0,1)
    sleep(2)
    led.off()
    sleep(2)