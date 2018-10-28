from twilio.rest import Client
from gpiozero import RGBLED
from gpiozero import Buzzer
from bluedot import BlueDot
from signal import pause
from time import sleep

class Doorbell:
    account_sid = ''
    auth_token = ''
    from_phonenumber=''
    test_env =  True
    led = RGBLED(red=17, green=22, blue=27)
    buzzer = Buzzer(26)
    num_of_rings = 0
    ring_delay = 0
    msg = ''
    
    def __init__(self, num_of_rings = 1, ring_delay = 1, message = 'ring', test_env = True):
        self.num_of_rings = num_of_rings
        self.ring_delay = ring_delay
        self.message = message
        self.test_env = self.setEnvironment(test_env)
        
    def setEnvironment(self, test_env):
        if test_env:
            self.account_sid = '<<test account_sid>>'
            self.auth_token = '<<test auth_token>>'
            return True
        else:
            self.account_sid = '<<live account_sid>>'
            self.auth_token = '<<live auth_token>>'
            return False
        
    def doorbell_sequence(self):
        num = 0
        while num < self.num_of_rings:
            self.buzzer.on()
            self.light_show()
            sleep(self.ring_delay)
            self.buzzer.off()
            sleep(self.ring_delay)
            num += 1
        return self.sendTextMessage()
    
    
    def sendTextMessage(self):
        twilio_client = Client(self.account_sid, self.auth_token)
        if self.test_env:
            message = twilio_client.messages.create(
                        body=self.message,
                        from_= '+15005550006',
                        to='<<your phone number>>'
            )
        else:
            message = twilio_client.messages.create(
                        body=self.message,
                        from_= '<<your twilio number>>',
                        to='<<your phone number>>'
            )               
        return 'Doorbell text message sent - ' + message.sid
       
            
    def light_show(self):
        self.led.color=(1,0,0)
        sleep(0.5)
        self.led.color=(0,1,0)
        sleep(0.5)
        self.led.color=(0,0,1)
        sleep(0.5)
        self.led.off()
        
    
def pressed():
    doorbell = Doorbell(2, 0.5, 'There is someone at the door')
    print(doorbell.doorbell_sequence())
        

blue_dot = BlueDot()
blue_dot.when_pressed = pressed
        
    
if __name__=="__main__":
    pause()
    

    
    