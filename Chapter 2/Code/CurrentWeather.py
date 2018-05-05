class CurrentWeather:
      
    weather_data={
        'Toronto':['13','partly sunny','8 km/h NW'],
        'Montreal':['16','mostly sunny','22 km/h W'],
        'Vancouver':['18','thunder showers','10 km/h NE'],
        'New York':['17','mostly cloudy','5 km/h SE'],
        'Los Angeles':['28','sunny','4 km/h SW'],
        'London':['12','mostly cloudy','8 km/h NW'],
        'Mumbai':['33','humid and foggy','2 km/h S']
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
    
    currentWeather = CurrentWeather('New York')
    wind_dir_str_len = 2
    
    if currentWeather.getWindSpeed()[-2:-1] == ' ':
        wind_dir_str_len = 1
        
    print("The current temperature in", currentWeather.getCity(),"is",
          currentWeather.getTemperature(), "degrees Celsius,",
          "the weather conditions are",
          currentWeather.getWeatherConditions(),
          "and the wind is coming out of the",
          currentWeather.getWindSpeed()[-(wind_dir_str_len):],
          "direction with a speed of",
          currentWeather.getWindSpeed()
          [0:len(currentWeather.getWindSpeed())-(wind_dir_str_len)]
          )
