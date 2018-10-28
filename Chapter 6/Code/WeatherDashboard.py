from gpiozero import Servo
from gpiozero import LED
from time import sleep
from WeatherData import WeatherData

class WeatherDashboard:
    
    servo_pin = 17
    led_pin = 14
    servoCorrection=0.5
    maxPW=(2.0+servoCorrection)/1000
    minPW=(1.0-servoCorrection)/1000
    
    def __init__(self, servo_position=0, led_status=0):
        
        self.servo = Servo(self.servo_pin, min_pulse_width=self.minPW, max_pulse_width=self.maxPW)
        self.led = LED(self.led_pin)
        
        self.move_servo(servo_position)
        self.set_led_status(led_status)
        
        
    def move_servo(self, servo_position=0): 
        self.servo.value = self.convert_percentage_to_integer(servo_position)
        
        
    def turnOffServo(self):
        sleep(2)
        self.servo.close()
        
    def set_led_status(self, led_status=0):
        
        if(led_status==0):
            self.led.off()
        elif (led_status==1):
            self.led.on()
        else:
            self.led.blink()
    
    def convert_percentage_to_integer(self, percentage_amount):
        #adjust for servos that turn counter clockwise by default
        adjusted_percentage_amount = 100 - percentage_amount
        return (adjusted_percentage_amount*0.02)-1
    
if __name__=="__main__":
    
    weather_data = WeatherData('Toronto')
    weather_dashboard = WeatherDashboard(
                        weather_data.getServoValue(),
                        weather_data.getLEDValue())
    weather_dashboard.turnOffServo()
    
    

    
    
    
    
        
        