

MIN_LENGTH = 8  # minimum number of characters in password


def main():
    """ Get and print password using functions """
    password = get_password()
    prints_asterisks(password)


def get_password():
    """ Get password from user """
    password = str(input("Enter password: "))
    # user inputs their password
    while len(password) < MIN_LENGTH:
        print("Password must be", MIN_LENGTH, "characters long.")
        password = str(input("Enter password: "))
        # check if password is MIN_LENGTH characters long.
    return password


def prints_asterisks(password):
    """ Print as many asterisks as there are character in password """
    for character in password:
        print("*", end="")
        # prints MIN_LENGTH asterisks to signify password is valid.


main()
