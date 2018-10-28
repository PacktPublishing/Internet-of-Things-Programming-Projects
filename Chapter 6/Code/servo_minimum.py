from gpiozero import Servo
servoPin=17

servoCorrection=0.5
maxPW=(2.0+servoCorrection)/1000
minPW=(1.0-servoCorrection)/1000

servo=Servo(servoPin, min_pulse_width=minPW, max_pulse_width=maxPW)

servo.min()