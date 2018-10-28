from sense_emu import SenseHat
from CurrentWeather import CurrentWeather

class DisplayWeather:
    current_weather = ''
    
    def __init__(self, current_weather):
        self.current_weather = current_weather
        
    def display(self):
        sense_hat_emulator = SenseHat()
        
        message = ("%s %sC %s wind speed %s km/h"
           %(self.current_weather.getCity(),
           self.current_weather.getTemperature(),
           self.current_weather.getWeatherConditions(),
           self.current_weather.getWindSpeed()))
           
        sense_hat_emulator.show_message(message)
        
if __name__ == "__main__":
    current_weather = CurrentWeather('Toronto')
    display_weather = DisplayWeather(current_weather)
    display_weather.display()
    

