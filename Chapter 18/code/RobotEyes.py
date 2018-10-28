from  gpiozero  import  DistanceSensor
from time import sleep
import paho.mqtt.client as mqtt
import json

class RobotEyes:
    
    distance_sensor  =  DistanceSensor(echo=18,  trigger=17)
    host = 'demo.thingsboard.io'
    access_token='qHdv9z2Yvn38OtuHqBGc'
    
    def get_distance(self):
        return self.distance_sensor.distance*100
    
    def publish_distance(self):
        distance = self.get_distance()
        sensor_data = {'distance': 0}
        sensor_data['distance'] = distance
        client = mqtt.Client()
        client.username_pw_set(self.access_token)
        client.connect(self.host, 1883, 20)
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        client.disconnect()
    
    
if __name__=="__main__":
    
    robot_eyes = RobotEyes()
    
    while True:
        
        print('Distance:  ', robot_eyes.get_distance())
        robot_eyes.publish_distance()
        
        sleep(5)
        