from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(25)
buzzer.on()
sleep(5)
buzzer.off()


