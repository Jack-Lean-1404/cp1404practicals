from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        """Initialise a reliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car until the reliability runs out"""
        distance_driven = super().drive(distance)
        reliability_percentage = random.randint(0, 100)
        if self.reliability >= reliability_percentage:
            return 0
        else:
            return distance_driven
