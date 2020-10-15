
from random import randint
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        start_chance = randint(0, 100)
        if start_chance >= self.reliability:
            distance = 0
            print("Didnt start")
        distance_driven = super().drive(distance)
        return distance_driven
