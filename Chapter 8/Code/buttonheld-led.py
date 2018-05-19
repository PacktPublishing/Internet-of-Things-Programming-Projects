from gpiozero import LED
from gpiozero import Button

led = LED(17)
button = Button(4)
button.hold_time=5

while True:
    button.when_held = lambda: led.toggle()