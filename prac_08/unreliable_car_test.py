"""
This program is a small test program used
to understand how the UnreliableCar class works
"""
from prac_08.unreliable_car import UnreliableCar


def main():
    """ Small tests with Taxi class """
    my_car = UnreliableCar("Ferrari", 100, 50)
    my_car.drive(40)
    print(my_car)


main()
