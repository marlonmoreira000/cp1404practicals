"""This program allows users to input a list of guitars and
print a summary of their list at the end."""
from prac_06.guitar import Guitar


def main():
    guitars = []  # create list to store guitar info

    # input guitar information
    while True:
        name = str(input("Name: "))
        if name == "":
            break  # exit loop when name is empty
        else:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            lst = [guitar.name, guitar.year, guitar.cost, guitar.is_vintage()]
            guitars.append(lst)
            print("{} ({}): ${} added.".format(guitar.name, guitar.year, guitar.cost))

    # print list of guitars
    print("These are my guitars:")
    for index, guitar in enumerate(guitars):
        if guitar[3] == True:
            print("Guitar {}: {} ({}), worth ${:,.2f} (vintage)".format(index+1, guitar[0], guitar[1], guitar[2]))
        else:
            print("Guitar {}: {} ({}), worth ${:,.2f}".format(index + 1, guitar[0], guitar[1], guitar[2]))

main()
