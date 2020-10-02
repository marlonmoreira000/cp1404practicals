"""
This is the code for UnreliableCar class
"""
from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """ Create UnreliableCar class """

    def __init__(self, name, fuel, reliability):
        """ Initialise a UnreliableCar instance. """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Drive the car, if it's reliable enough """
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

