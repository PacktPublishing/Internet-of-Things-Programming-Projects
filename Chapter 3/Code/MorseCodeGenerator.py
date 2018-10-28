from gpiozero import LED
from time import sleep

class MorseCodeGenerator:
    
    led = LED(18)
    dot_duration = 0.3
    dash_duration = dot_duration * 3
    word_spacing_duration = dot_duration * 7
          
    MORSE_CODE = {
        'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   '0': '-----',
        '1': '.----',  '2': '..---',  '3': '...--',
        '4': '....-',  '5': '.....',  '6': '-....',
        '7': '--...',  '8': '---..',  '9': '----.',
        ' ': ' '
        }   
        
    def transmit_message(self, message):
        for letter in message: 
            morse_code_letter = self.MORSE_CODE[letter.upper()]
            
            for dash_dot in morse_code_letter:
                
                if dash_dot == '.':
                    self.dot()
                
                elif dash_dot == '-':
                    self.dash()
                    
                elif dash_dot == ' ':
                    self.word_spacing()
            
            self.letter_spacing()
                       
    def dot(self):
        self.led.blink(self.dot_duration,self.dot_duration,1,False)
            
    def dash(self):
        self.led.blink(self.dash_duration,self.dot_duration,1,False)
            
    def letter_spacing(self):
        sleep(self.dot_duration)
            
    def word_spacing(self):
        sleep(self.word_spacing_duration-self.dot_duration)
 
if __name__ == "__main__":
    
    morse_code_generator = MorseCodeGenerator()
    morse_code_generator.transmit_message('SOS')
    


            
        
 
        
    