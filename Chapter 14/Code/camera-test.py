from picamera import PiCamera
import time

camera = PiCamera()
camera.capture("/home/pi/image-" + time.ctime() + ".png")

    
    


    
