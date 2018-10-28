from time import sleep
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
from gpiozero import MotionSensor

host = 'demo.thingsboard.io'
access_token = '<<access token>>'
dht_sensor = Adafruit_DHT.DHT11
dht11_pin = 19
motion_sensor = MotionSensor(4)

sensor_data = {'temperature': 0, 'humidity': 0, 'Motion Detected':False}

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

client.connect(host, 1883, 60)

client.loop_start()

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht11_pin)
        motion_detected = motion_sensor.motion_detected
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%, Motion Detected: {:g}".format(temperature, humidity, motion_detected))
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity
        sensor_data['Motion Detected'] = motion_detected

        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        sleep(10)
        
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()