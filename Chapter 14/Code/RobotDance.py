from RobotWheels import RobotWheels
from RobotBeep import RobotBeep
from TailLights import TailLights
from RobotCamera import RobotCamera

class RobotDance:
    
    light_show = [2,1,4,5,3,1]
    
    def __init__(self):
        
        self.robot_wheels = RobotWheels()
        self.robot_beep = RobotBeep()
        self.tail_lights = TailLights()
        self.robot_camera = RobotCamera()
        
    
    def lets_dance_incognito(self):
        for tail_light_repetition in self.light_show:
            self.robot_wheels.dance()
            self.robot_beep.play_song()
            self.tail_lights.alarm(tail_light_repetition)
            self.robot_camera.secret_dance()

if __name__=="__main__":
 
    robot_dance = RobotDance()
    robot_dance.lets_dance_incognito()
    
    