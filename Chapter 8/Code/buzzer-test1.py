from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

while True:
    buzzer.on()
    sleep(2)
    buzzer.off()
    sleep(2)
