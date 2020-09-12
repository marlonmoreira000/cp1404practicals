"""This program is used to do simple tests on the Guitar class we created"""
from prac_06.guitar import Guitar


def main():
    # create 2 Guitar classes. Class(name, year, cost)
    guitar1 = Guitar("Gibson 1000", 1937, 13500)
    guitar2 = Guitar("Fender 450", 2001, 6500)

    # print test results for get_age() and is_vintage() methods
    print("{} get_age() - Expected 83. Got {}".format(guitar1.name, guitar1.get_age()))
    print("{} get_age() - Expected 19. Got {}".format(guitar2.name, guitar2.get_age()))
    print("{} is_vintage - Expected True. Got {}".format(guitar1.name, guitar1.is_vintage()))
    print("{} is_vintage - Expected True. Got {}".format(guitar2.name, guitar2.is_vintage()))


main()