from bluedot import BlueDot
from signal import pause
from DoorbellAlarmAdvanced import DoorbellAlarmAdvanced

class SimpleDoorbell:
        
    def pressed():
        doorbell_alarm = DoorbellAlarmAdvanced(5, 1)
        doorbell_alarm.play_sequence()
       
    
    blue_dot = BlueDot()
    blue_dot.when_pressed = pressed

    
        
if __name__=="__main__":

    doorbell_alarm = SimpleDoorbell()
    pause()
    

    
    