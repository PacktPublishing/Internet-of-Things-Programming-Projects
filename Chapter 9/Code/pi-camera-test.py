from picamera import PiCamera
from time import sleep

pi_cam = PiCamera()

pi_cam.start_preview()
sleep(5)
pi_cam.capture('/home/pi/myimage.png')
pi_cam.stop_preview()


