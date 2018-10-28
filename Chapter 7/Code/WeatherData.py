from weather import Weather, Unit
import time

class WeatherData:
    
    temperature = 0
    weather_conditions = ''
    wind_speed = 0
    city = ''
      
    
    def __init__(self, city):
        self.city = city
        weather = Weather(unit = Unit.CELSIUS)
        lookup = weather.lookup_by_location(self.city)
        self.temperature = lookup.condition.temp
        self.weather_conditions = lookup.condition.text
        self.wind_speed = lookup.wind.speed
    
    
    def getTemperature(self):
        return self.temperature + " C"
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return self.wind_speed + " kph"
    
    def getCity(self):
        return self.city
    
    def getTime(self):
        return time.ctime()
    
    
if __name__ == "__main__":
    
    current_weather = WeatherData('London')
    print(current_weather.getTemperature())
    print(current_weather.getWeatherConditions())
    print(current_weather.getTime())

    


    

    