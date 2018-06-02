from time import sleep
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json

host = 'demo.thingsboard.io'
access_token = '<<access token>>'
dht_sensor = Adafruit_DHT.DHT11
pin = 19

sensor_data = {'temperature': 0, 'humidity': 0}

client = mqtt.Client()
client.username_pw_set(access_token)

while True:
    humidity, temperature = Adafruit_DHT
                                .read_retry(dht_sensor, pin)

    print(u"Temperature: {:g}\u00b0C, Humidity{:g}%".format(temperature, humidity))

    sensor_data['temperature'] = temperature
    sensor_data['humidity'] = humidity
    client.connect(host, 1883, 20)
    client.publish('v1/devices/me/telemetry', 
                json.dumps(sensor_data), 1)
    client.disconnect()
    sleep(10)
