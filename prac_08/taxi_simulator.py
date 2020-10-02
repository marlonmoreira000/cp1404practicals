"""
This program is a taxi simulator which uses the
Taxi and SilverServiceTaxi classes.
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q - quit\nc - choose taxi\nd - drive"


def main():
    """Create the taxi simulator program."""
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()

    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            list_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            drive_distance = float(input("Drive how far? "))
            current_taxi.drive(drive_distance)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            total_bill = total_bill + current_taxi.get_fare()
        else:
            print("Invalid input")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    list_taxis(taxis)


def list_taxis(taxis):
    """List all available taxis."""
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


main()
