from gpiozero import Buzzer
from time import sleep

class RobotBeep:
    
    buzzer = Buzzer(12)
    notes = [[0.5,0.5],[0.5,1],[0.2,0.5],[0.5,0.5],[0.5,1],[0.2,0.5]]
    
    def __init__(self, play_init=False):
        
        if play_init:
            self.buzzer.on()
            sleep(0.1)
            self.buzzer.off()
            sleep(1)
        
    def play_song(self):
        
        for note in self.notes:
            self.buzzer.on()
            sleep(note[0])
            self.buzzer.off()
            sleep(note[1])
            

if __name__=="__main__":

    robot_beep = RobotBeep(True)
 
    
    


