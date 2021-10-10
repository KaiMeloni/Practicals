from random import randint
from prac_08.car import Car

class UnrealibleCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_num = randint(1, 100)
        if random_num >= self.reliability:
            distance = 0
        distance_travelled = super().drive(distance)
        return distance_travelled