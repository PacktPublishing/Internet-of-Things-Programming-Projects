from gpiozero import MotionSensor
from gpiozero import Button
from datetime import datetime
from picamera import PiCamera
import Adafruit_DHT

class SecurityData:
    humidity=''
    temperature=''
    detected_message=''
    
    dht_pin = 19
    dht_sensor = Adafruit_DHT.DHT11
    switch = Button(8)
    motion_sensor = MotionSensor(4)
    pi_cam = PiCamera()
    
    def getRoomConditions(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht_sensor, self.dht_pin)
        return str(temperature) + 'C / ' + str(humidity) + '%'
    
    def getDetectedMessage(self):
        return self.detected_message
    
    def getArmedStatus(self):
        if self.switch.is_pressed:
            return "on"
        else:
            return "off"

    def getSecurityImage(self):
        
        if not(self.switch.is_pressed):
            self.detected_message = ''
            return "/not-armed.png"
            
        elif self.motion_sensor.motion_detected:
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
        print(security_data.getRoomConditions())
        print(security_data.getArmedStatus())
        print(security_data.getTime())
    

    


    

    