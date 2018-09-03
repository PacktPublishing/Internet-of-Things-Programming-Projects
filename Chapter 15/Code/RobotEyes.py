from gpiozero import DistanceSensor
from time import sleep


class RobotEyes:
    distance_sensor = DistanceSensor(echo=18, trigger=17)

    def get_distance(self):
        return self.distance_sensor.distance * 100


if __name__ == "__main__":

    robot_eyes = RobotEyes()

    while True:
        print('Distance: ', robot_eyes.get_distance())
        sleep(1)
