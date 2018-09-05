import paho.mqtt.client as mqtt
from gpiozero import LED
import json

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = '6Y9GFdEcsOAs40RfrJWl'
green_led=LED(21)

def on_connect(client, userdata, rc, *extra_params):
    print('Connected with result code ' + str(rc))
    client.subscribe('v1/devices/me/rpc/request/+')

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode("utf-8"))         
    
    if data['method'] == 'toggleGreenTailLight':
        if data['params']:
            green_led.on()
        else:
            green_led.off()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_forever()

