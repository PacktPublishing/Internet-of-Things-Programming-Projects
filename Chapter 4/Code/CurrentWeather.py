from weather import Weather, Unit

class CurrentWeather:
    temperature = ''
    weather_conditions = ''
    wind_speed = ''
    city = ''
    
    def __init__(self, city):
        self.city = city
        weather = Weather(unit = Unit.CELSIUS)
        lookup = weather.lookup_by_location(self.city)
        self.temperature = lookup.condition.temp
        self.weather_conditions = lookup.condition.text
        self.wind_speed = lookup.wind.speed
        
    def getTemperature(self):
        return self.temperature
    
    def getWeatherConditions(self):
        return self.weather_conditions
    
    def getWindSpeed(self):
        return self.wind_speed
    
    def getCity(self):
        return self.city
    
if __name__=="__main__":
    current_weather = CurrentWeather('Montreal')
    print("%s %sC %s wind speed %s km/h"
           %(current_weather.getCity(),
           current_weather.getTemperature(),
           current_weather.getWeatherConditions(),
           current_weather.getWindSpeed()))
    



        
    