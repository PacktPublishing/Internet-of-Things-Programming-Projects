from gpiozero import MotionSensor
from gpiozero import Button
from datetime import datetime
from picamera import PiCamera
from gpiozero import Buzzer
from time import sleep

class SecurityData:
    alarm_status=''
    detected_message=''
    
    switch = Button(8)
    motion_sensor = MotionSensor(4)
    pi_cam = PiCamera()
    buzzer = Buzzer(17)
    
    def sound_alarm(self):
        self.buzzer.beep(0.5,0.5, 5, True)
        sleep(1)
    
    def getAlarmStatus(self):
        
        if not(self.switch.is_pressed):
            self.alarm_status = 'not-armed'
            return "Not Armed"
            
        elif self.motion_sensor.motion_detected:
            self.alarm_status = 'motion-detected'
            self.sound_alarm()
            return "Motion Detected"

        else:
            self.alarm_status = 'all-clear'
            return "All Clear"
    
    def getDetectedMessage(self):
        return self.detected_message
    
    def getArmedStatus(self):
        if self.switch.is_pressed:
            return "on"
        else:
            return "off"

    def getSecurityImage(self):
        
        if self.alarm_status=='not-armed':
            self.detected_message = ''
            return "/not-armed.png"
            
        elif self.alarm_status=='motion-detected':
            self.pi_cam.resolution = (500, 375)
            self.pi_cam.capture("/home/pi/images/intruder.png")
            self.detected_message = "Detected at:  " + self.getTime()
            return "/intruder.png"

        else:
            self.detected_message = ''
            return "/all-clear.png"
    
    def getTime(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    
if __name__ == "__main__":
    
    while True:
        security_data = SecurityData()
        print(security_data.getArmedStatus())
        print(security_data.getTime())
    

    


    

    