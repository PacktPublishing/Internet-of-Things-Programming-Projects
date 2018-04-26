from MorseCodeGenerator import MorseCodeGenerator

class CurrentWeather:
      
    weather_data={
        'Toronto':['13','partly sunny','8 NW'],
        'Montreal':['16','mostly sunny','22 W'],
        'Vancouver':['18','thunder showers','10 NE'],
        'New York':['17','mostly cloudy','5 SE'],
        'Los Angeles':['28','sunny','4 SW'],
        'London':['12','mostly cloudy','8 NW'],
        'Mumbai':['33','humid and foggy','2 S']
    }
    
    def __init__(self, city):
        self.city = city       
    
    def getTemperature(self):
        return self.weather_data[self.city][0]
    
    def getWeatherConditions(self):
        return self.weather_data[self.city][1]
    
    def getWindSpeed(self):
        return self.weather_data[self.city][2]
    
    def getCity(self):
        return self.city
    
    
if __name__ == "__main__":
    
    current_weather = CurrentWeather('Toronto')
    morse_code_generator = MorseCodeGenerator()
    
    morse_code_generator.transmit_message(current_weather.getWeatherConditions())
    
    
    
    


    

    