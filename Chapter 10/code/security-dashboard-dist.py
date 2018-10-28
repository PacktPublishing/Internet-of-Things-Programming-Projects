from twilio.rest import Client
from SensoryData import SensoryData
from SensoryDashboard import SensoryDashboard
from gpiozero import Button
from time import time, sleep

class SecurityDashboardDist:
    account_sid = ''
    auth_token = ''
    time_sent = 0
    from_phonenumber=''
    test_env =  True
    
    switch = Button(8)
    
    def __init__(self, test_env = True):
       
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
            
    def update_dashboard(self, sensoryDashboard):
        self.sensoryDashboard = sensoryDashboard
        motion_detected = self.sensoryDashboard.publishSensoryData()
        
        if motion_detected:
            return self.send_alert()
        else:
            return 'Alarm not triggered'
            
    def send_alert(self):
        if self.switch.is_pressed:
            return self.sendTextMessage()
        else:
            return "Alarm triggered but Not Armed"
    
    def sendTextMessage(self):
        message_interval = round(time() - self.time_sent)
                
        if message_interval > 600:
            twilio_client = Client(self.account_sid, self.auth_token)
            
            if self.test_env:
                message = twilio_client.messages.create(
                            body='Intruder Alert',
                            from_= '+15005550006',
                            to='<<your cell phone number>>'
                          )
            else:
                message = twilio_client.messages.create(
                            body='Intruder Alert',
                            from_= '<<your twilio number>>',
                            to='<<your cell phone number>>'
                          )
                
            self.time_sent=round(time())
            return 'Alarm triggered and text message sent - ' + message.sid
        else:
            return 'Alarm triggered and text message sent less than 10 minutes ago'
        
        
    
if __name__=="__main__":
    
    security_dashboard = SecurityDashboardDist()
    
    while True:
        sensory_data = SensoryData()
        sensory_dashboard = SensoryDashboard(sensory_data)
        print(security_dashboard.update_dashboard(sensory_dashboard))
        
        sleep(5)
    
    
    
    