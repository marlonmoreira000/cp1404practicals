"""
This is the code for SilverServiceTaxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ Create SilverServiceTaxi class """
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """ Initialise a SilverServiceTaxi instance. """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """ Print details about SilverServiceTaxi instance. """
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """ Get fare of taxi ride. """
        return super().get_fare() + self.flagfall
