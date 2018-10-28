from gpiozero import RGBLED
from gpiozero import Buzzer
from time import sleep

class DoorbellAlarm:
    
    led = RGBLED(red=17, green=22, blue=27)
    buzzer = Buzzer(26)
    num_of_times = 0
    
    def __init__(self, num_of_times):
        self.num_of_times = num_of_times
            
        
    def play_sequence(self):
        num = 0
        while num < self.num_of_times:
            self.buzzer.on()
            self.light_show()
            sleep(0.5)
            self.buzzer.off()
            sleep(0.5)
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

    doorbell_alarm = DoorbellAlarm(5)
    doorbell_alarm.play_sequence()
    
    


