from weather import Weather, Unit

class WeatherData:
    
    temperature = 0
    weather_conditions = ''
    wind_speed = 0
    city = ''
      
    
    def __init__(self, city):
        self.city = city
        weather = Weather(unit = Unit.CELSIUS)
        lookup = weather.lookup_by_location(self.city)
        self.temperature = float(lookup.condition.temp)
        self.weather_conditions = lookup.condition.text
        self.wind_speed = float(lookup.wind.speed)
    
    
    def getServoValue(self):
        temp_factor = (self.temperature*100)/30
        wind_factor = (self.wind_speed*100)/20
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

    
    
    
    
    


    

    