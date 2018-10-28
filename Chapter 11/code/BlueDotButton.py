from bluedot import BlueDot
from signal import pause

class BlueDotButton:
    
    def swiped(swipe):
        
        if swipe.up:
            print("Blue Dot Swiped Up")
        elif swipe.down:
            print("Blue Dot Swiped Down")
        elif swipe.left:
            print("Blue Dot Swiped Left")
        elif swipe.right:
            print("Blue Dot Swiped Right")
       
        
    def pressed(pos):
        if pos.top:
            print("Blue Dot Pressed from Top")
        elif pos.bottom:
            print("Blue Dot Pressed from Bottom")
        elif pos.left:
            print("Blue Dot Pressed from Left")
        elif pos.right:
            print("Blue Dot Pressed from Right")
        elif pos.middle:
            print("Blue Dot Pressed from Middle")
        
        
    def double_pressed():
        print("Blue Dot Double Pressed")
       
    
    blue_dot = BlueDot()
    blue_dot.when_swiped = swiped
    blue_dot.when_pressed = pressed
    blue_dot.when_double_pressed = double_pressed
    
        
        
if __name__=="__main__":

    blue_dot_button = BlueDotButton()
    pause()
    

    
    