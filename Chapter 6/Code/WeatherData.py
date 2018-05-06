import urllib.request
import json

class WeatherData:
    
    api_key = '7e95614bcf837210'
    temperature = ''
    weather_conditions = ''
    wind_speed = ''
    city = ''
      
    url_data={
        'Toronto':['zmw:00000.176.71508.json'],
        'Montreal':['canada/Montreal.json'],
        'Vancouver':['canada/Vancouver.json'],
        'New York':['NY/New_York.json'],
        'Los Angeles':['CA/Los_Angeles.json'],
        'London':['UK/London.json'],
        'Mumbai':['india/Mumbai.json'],
        'Paris':['fr/paris.json'],
        'test':['cd/kinshasa.json']
    }
    
    def __init__(self, city):
        self.city = city
        request = urllib.request.urlopen("http://api.wunderground.com/api/" +
                                    self.api_key +
                                   "/conditions/q/" +
                                   self.url_data[self.city][0])
        
        json_string = request.read()
        
        parse_json = json.loads(json_string.decode('utf-8'))
        self.temperature = parse_json['current_observation']['temp_c']
        self.weather_conditions = parse_json['current_observation']['weather']
        self.wind_speed = parse_json['current_observation']['wind_kph']
    
    
    def getServoValue(self):
        temp_factor = (self.temperature*100)/30
        wind_factor = (self.temperature*100)/20
        servo_value = temp_factor-(wind_factor/20)
        
        if(servo_value >= 100):
            return 100
        elif (servo_value <= 0):
            return 0
        else:
            return servo_value
    
    def getLEDValue(self):
        if (self.weather_conditions=='Thunderstorm'):
            return 2;
        elif(self.weather_conditions=='Raining'):
            return 1
        else:
            return 0
    
if __name__=="__main__":
    
    weather = WeatherData('Paris')
    print(weather.getServoValue())
    print(weather.getLEDValue())

    
    
    
    
    


    

    