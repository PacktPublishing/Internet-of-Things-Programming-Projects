from sense_emu import SenseHat

class DisplayWeather:
    city=''
    temperature=''
    weather_conditions=''
    wind_speed=''
    
    def __init__(self, weather_info=['No City','0','no conditions','0']):
        self.city=weather_info[0]
        self.temperature=weather_info[1]
        self.weather_conditions=weather_info[2]
        self.wind_speed=weather_info[3]
        
    def display_weather(self):
        sense_emulator = SenseHat()        
        message="%s %sC %s wind speed %s km/h" %(self.city, self.temperature, self.weather_conditions, self.wind_speed)
        
        sense_emulator.show_message(message)
         
if __name__ == "__main__":
    
    weather_info=['Toronto','12.3','clear','12']
    display_weather=DisplayWeather(weather_info)
    display_weather.display_weather()
    
    
        