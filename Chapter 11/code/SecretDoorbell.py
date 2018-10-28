from bluedot import BlueDot
from signal import pause
from DoorbellAlarmAdvanced import DoorbellAlarmAdvanced

class SecretDoorbell:
        
    def swiped(swipe):
        
        if swipe.up:
            doorbell_alarm = DoorbellAlarmAdvanced(5, 0.5)
            doorbell_alarm.play_sequence()
        elif swipe.down:
            doorbell_alarm = DoorbellAlarmAdvanced(3, 2)
            doorbell_alarm.play_sequence()
        elif swipe.left:
            doorbell_alarm = DoorbellAlarmAdvanced(1, 5)
            doorbell_alarm.play_sequence()
        elif swipe.right:
            doorbell_alarm = DoorbellAlarmAdvanced(1, 0.5)
            doorbell_alarm.play_sequence()
       
    
    blue_dot = BlueDot()
    blue_dot.when_swiped = swiped

    
        
if __name__=="__main__":

    doorbell = SecretDoorbell()
    pause()
    

    
    