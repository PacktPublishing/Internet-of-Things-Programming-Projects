import paho.mqtt.client as mqtt
from time import sleep
from RobotDance import RobotDance
from RobotWheels import RobotWheels
from RobotBeep import RobotBeep
from RobotCamera import RobotCamera
from  gpiozero  import  DistanceSensor

distance_sensor  =  DistanceSensor(echo=18,  trigger=17)
    
def on_message(client, userdata, message):
    command = message.payload.decode("utf-8")
    
    if command == "Forward":
        move_forward()
    elif command == "Backward":
        move_backward()
    elif command == "Left":
        turn_left()
    elif command == "Right":
        turn_right()
    elif command == "Picture":
        take_picture()
    elif command == "Alarm":
        sound_alarm()
    elif command == "Dance":
        robot_dance()
        
def move_forward():
    robotWheels = RobotWheels()
    robotWheels.move_forward()
    sleep(1)
    print("Moved forward")
    robotWheels.stop()
    watchMode()
    
def move_backward():
    robotWheels = RobotWheels()
    robotWheels.move_backwards()
    sleep(1)
    print("Moved backwards")
    robotWheels.stop()
    watchMode()
    
def turn_left():
    robotWheels = RobotWheels()
    robotWheels.turn_left()
    sleep(1)
    print("Turned left")
    robotWheels.stop()
    watchMode()

def turn_right():
    robotWheels = RobotWheels()
    robotWheels.turn_right()
    print("Turned right")
    robotWheels.stop()
    watchMode()
    
def take_picture():
    robotCamera = RobotCamera()
    robotCamera.take_picture()
    watchMode()
    
def sound_alarm():
    robotBeep = RobotBeep()
    robotBeep.play_song()
    
def robot_dance():
    robotDance = RobotDance()
    robotDance.lets_dance_incognito()
    print("Finished dancing now back to work")
    watchMode()

def watchMode():
    print("Watching.....")
    mqttc = mqtt.Client()
    mqttc.username_pw_set("vectydkb", "ZpiPufitxnnT")
    mqttc.connect('m10.cloudmqtt.com', 18215)
    mqttc.on_message = on_message
    mqttc.subscribe("RobotControl")

    while True:
        distance = distance_sensor.distance*100
        mqttc.loop()
        mqttc.publish("distance", distance)
        sleep(2)
        
watchMode()
