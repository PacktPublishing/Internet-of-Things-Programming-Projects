import urllib.request
import json

class WeatherData:
    
    api_key = '<<your api code>>'
    temperature = ''
    weather_conditions = ''
    wind_speed = ''
    city = ''
    icon  = ''
    time = ''
      
    url_data={
        'Toronto':['zmw:00000.176.71508.json'],
        'Montreal':['canada/Montreal.json'],
        'Vancouver':['canada/Vancouver.json'],
        'New York':['CA/New_York.json'],
        'Los Angeles':['/CA/Los_Angeles.json'],
        'London':['UK/London.json'],
        'Mumbai':['india/Mumbai.json'],
        'Paris':['fr/paris.json']
    }
    
    def __init__(self, city):
        self.city = city
        request = urllib.request.urlopen("http://api.wunderground.com/api/" +
                                    self.api_key +
                                   "/conditions/q/" +
                                   self.url_data[self.city][0])
        json_string = request.read()
        parse_json = json.loads(json_string.decode('utf-8'))
        self.temperature = parse_json['current_observation']['temperature_string']
        self.weather_conditions = parse_json['current_observation']['weather']
        self.wind_speed = parse_json['current_observation']['wind_string']
        self.icon = parse_json['current_observation']['icon_url']
        self.time = parse_json['current_observation']['observation_time']
    
    
    def getTemperature(self):
        return self.temperature
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return self.wind_speed
    
    def getCity(self):
        return self.city
    
    def getIcon(self):
        return self.icon
    
    def getTime(self):
        return self.time
    
    
if __name__ == "__main__":
    
    current_weather = WeatherData('London')
    print(current_weather.getIcon())
    print(current_weather.getTemperature())
    


    

    