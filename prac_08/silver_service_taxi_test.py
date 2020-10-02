"""
This program is a small test program used
to understand how the SilverServiceTaxi class works
"""
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """ Small tests with SilverServiceTaxi class """
    my_taxi = SilverServiceTaxi("Mercedes", 100, 2)
    print(my_taxi.__str__())
    my_taxi.drive(18)
    print(my_taxi.__str__())
    print(my_taxi.get_fare())


main()

