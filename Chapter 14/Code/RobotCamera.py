from time import sleep
from time import ctime
from picamera import PiCamera
import Adafruit_PCA9685

class RobotCamera:
    
    pan_min = 150
    pan_centre = 375
    pan_max = 600
    tilt_min = 150
    tilt_max = 200
    camera = PiCamera()
    pwm = Adafruit_PCA9685.PCA9685()
    
    def __init__(self):
        self.tilt_up()
    
    def pan_right(self):
        self.pwm.set_pwm(0, 0, self.pan_min)
        sleep(2)
        
    def pan_left(self):
        self.pwm.set_pwm(0, 0, self.pan_max)
        sleep(2)
        
    def pan_mid(self):
        self.pwm.set_pwm(0, 0, self.pan_centre)
        sleep(2)
        
    def tilt_down(self):
        self.pwm.set_pwm(1, 0, self.tilt_max)
        sleep(2)
        
    def tilt_up(self):
        self.pwm.set_pwm(1, 0, self.tilt_min)
        sleep(2)
    
    def take_picture(self):
        sleep(2)
        self.camera.capture("/home/pi/image-" + ctime() + ".png")
        
    def dance(self):
        self.pan_right()
        self.tilt_down()
        self.tilt_up()
        self.pan_left()
        self.pan_mid()
        
    def secret_dance(self):
        self.pan_right()
        self.tilt_down()
        self.tilt_up()
        self.pan_left()
        self.pan_mid()
        self.take_picture()
        

if __name__=="__main__":
 
    robot_camera = RobotCamera()
    robot_camera.dance()
    
    
    
    


    
