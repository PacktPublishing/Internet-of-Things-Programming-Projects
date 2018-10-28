from gpiozero import RGBLED
from gpiozero import Buzzer
from time import sleep

class DoorbellAlarmAdvanced:
    
    led = RGBLED(red=17, green=22, blue=27)
    buzzer = Buzzer(26)
    num_of_times = 0
    delay = 0
    
    def __init__(self, num_of_times, delay):
        self.num_of_times = num_of_times
        self.delay = delay
            
        
    def play_sequence(self):
        num = 0
        while num < self.num_of_times:
            self.buzzer.on()
            self.light_show()
            sleep(self.delay)
            self.buzzer.off()
            sleep(self.delay)
            num += 1
            
            
    def light_show(self):
        self.led.color=(1,0,0)
        sleep(0.1)
        self.led.color=(0,1,0)
        sleep(0.1)
        self.led.color=(0,0,1)
        sleep(0.1)
        self.led.off()
            

if __name__=="__main__":

    doorbell_alarm = DoorbellAlarmAdvanced(5,1)
    doorbell_alarm.play_sequence()
    
    


