import urllib.request
import json
from DisplayWeather import DisplayWeather

class CurrentWeather:
    
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
        'Mumbai':['india/Mumbai.json']
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
    
    def getTemperature(self):
        return self.temperature
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return self.wind_speed
    
    def getCity(self):
        return self.city
    
    
if __name__ == "__main__":
    
    current_weather = CurrentWeather('London')
    weather_data=[current_weather.getCity(),
                  current_weather.getTemperature(),
                  current_weather.getWeatherConditions(),
                  current_weather.getWindSpeed()]
    
    display_weather=DisplayWeather(weather_data)
    display_weather.display_weather()
    


    

    
