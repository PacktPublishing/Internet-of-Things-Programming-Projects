import paho.mqtt.client as mqtt
import json
from SensoryData import SensoryData
from time import sleep

class SensoryDashboard:
    
    host = 'demo.thingsboard.io'
    access_token = '<<access token>>'
    client = mqtt.Client()
    client.username_pw_set(access_token)
    
    def __init__(self):
        self.client.connect(self.host, 1883, 60)
        
    def publishSensoryData(self, sensoryData):
        sensoryData = sensoryData
        sensor_data = {'temperature': 0, 'humidity': 0, 'Motion Detected':False}
        sensor_data['temperature'] = sensoryData.getTemperature()
        sensor_data['humidity'] = sensoryData.getHumidity()
        sensor_data['Motion Detected'] = sensoryData.getMotionDetected()

        self.client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        
        return sensor_data['Motion Detected']
    
    
if __name__=="__main__":
    
    sensory_dashboard = SensoryDashboard()
    
    while True:
        sensoryData = SensoryData()
        print("Motion Detected: " + str(sensory_dashboard.publishSensoryData(sensoryData)))
        sleep(10)
    
    
    
    
    
    

    