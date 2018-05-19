from gpiozero import Button
from time import sleep

button = Button(4)

while True:
    if button.is_pressed:
        print("The Button on GPIO 2 has been pressed")
        sleep(1)
        
