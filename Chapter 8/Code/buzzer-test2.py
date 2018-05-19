from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

while True:
    buzzer.toggle()
    sleep(2)
    