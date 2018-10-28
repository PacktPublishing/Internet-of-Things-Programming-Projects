from gpiozero import MotionSensor
import Adafruit_DHT

class SensoryData:
    humidity=''
    temperature=''
    detected_motion=''
    
    dht_pin = 19
    dht_sensor = Adafruit_DHT.DHT11
    motion_sensor = MotionSensor(4)
    
    def __init__(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.dht_sensor, self.dht_pin)
        self.motion_detected = self.motion_sensor.motion_detected
    
    def getTemperature(self):
        return self.temperature
    
    def getHumidity(self):
        return self.humidity
    
    def getMotionDetected(self):
        return self.motion_detected

    
if __name__ == "__main__":
    
    while True:
        sensory_data = SensoryData()
        print(sensory_data.getTemperature())
        print(sensory_data.getHumidity())
        print(sensory_data.getMotionDetected())
   