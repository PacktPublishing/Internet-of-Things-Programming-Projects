import paho.mqtt.client as mqtt
from time import sleep

mqttc = mqtt.Client()
mqttc.username_pw_set("vectydkb", "ZpiPufitxnnT")
mqttc.connect('m10.cloudmqtt.com', 18215)

while True:
    try:
        mqttc.publish("test", "Hello from Raspberry Pi")
    except:
        print("Could not send message!")
    sleep(10)
    
    
    
