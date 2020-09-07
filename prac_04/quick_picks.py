"""This program prints a user-defined number of lottery picks"""

import random

NUMBERS_PER_PICK = 6


def main():
    number_of_picks = int(input("Number of quick picks: "))

    while number_of_picks < 0:
        print("Number must be > 0")
        number_of_picks = int(input("Number of quick picks: "))

    for pick in range(1, number_of_picks + 1):
        lst = []  # create empty list to put number into
        for number in range(1, NUMBERS_PER_PICK + 1):
            random_number = random.randint(1, 45)
            while random_number in lst:
                random_number = random.randint(1, 45)
            lst.append(random_number)
        lst.sort()
        print("{} {} {} {} {} {}".format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5]))


main()
