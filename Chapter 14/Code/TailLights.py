from gpiozero import LEDBoard
from time import sleep


class TailLights:
    
    led_lights = LEDBoard(red=21, green=20)
    
    
    def __init__(self):
        self.led_lights.on()
        sleep(0.25)
        self.led_lights.off()
        sleep(0.25)
        
    def blink_red(self, num, duration):
        for x in range(num):
            self.led_lights.red.on()
            sleep(duration)
            self.led_lights.red.off()
            sleep(duration)
    
    def blink_green(self, num, duration):
        for x in range(num):
            self.led_lights.green.on()
            sleep(duration)
            self.led_lights.green.off()
            sleep(duration)
        
    def blink_alternating(self, num, duration):
        for x in range(num):
            self.led_lights.red.off()
            self.led_lights.green.on()
            sleep(duration)
            self.led_lights.red.on()
            self.led_lights.green.off()
            sleep(duration)
        self.led_lights.red.off()
        
    def blink_together(self, num, duration):
        for x in range(num):
            self.led_lights.on()
            sleep(duration)
            self.led_lights.off()
            sleep(duration)
    
    def alarm(self, num):
        for x in range(num):
            self.blink_alternating(2, 0.25)
            self.blink_together(2, 0.5)
        

if __name__=="__main__":

    tail_lights = TailLights()
    tail_lights.alarm(20)
    
    