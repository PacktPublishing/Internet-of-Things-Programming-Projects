from gpiozero import Button
from sense_emu import SenseHat
from time import sleep

button = Button(4)
sense = SenseHat()

def display_x_mark(rate=1):
    sense.clear()
    X = (255,0,0)
    O = (255,255,255)
    x_mark = [
              X,O,O,O,O,O,O,X,
              O,X,O,O,O,O,X,O,
              O,O,X,O,O,X,O,O,
              O,O,O,X,X,O,O,O,
              O,O,O,X,X,O,O,O,
              O,O,X,O,O,X,O,O,
              O,X,O,O,O,O,X,O,
              X,O,O,O,O,O,O,X
    ]
    sense.set_pixels(x_mark)
   
while True:
    if button.is_pressed:
        display_x_mark()
        sleep(1)
    else:
        sense.clear()








