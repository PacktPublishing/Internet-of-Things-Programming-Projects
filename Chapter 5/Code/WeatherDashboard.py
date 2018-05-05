from gpiozero import Servo
from gpiozero import LED

class WeatherDashboard:
    
    servo_pin = 17
    led_pin = 14
    
    def __init__(self, servo_position=0, led_status=0):
        
        self.servo = Servo(self.servo_pin)
        self.led = LED(self.led_pin)
        
        self.move_servo(servo_position)
        self.set_led_status(led_status)
        
        
    def move_servo(self, servo_position=0): 
        self.servo.value = self.convert_percentage_to_integer(servo_position)
        
    def set_led_status(self, led_status=0):
        
        if(led_status==0):
            self.led.off()
        elif (led_status==1):
            self.led.on()
        else:
            self.led.blink()
    
    def convert_percentage_to_integer(self, percentage_amount):
        return (percentage_amount*0.02)-1
    
if __name__=="__main__":
    weather_dashboard = WeatherDashboard(50, 1)
    
    

    
    
    
    
        
        