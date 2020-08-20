""" This program checks if a password is valid length """

MIN_LENGTH = 8
# minimum number of characters in password

password = str(input("Enter password: "))
# user inputs their password

while len(password) < MIN_LENGTH:
    print("Password must be", MIN_LENGTH, "characters long.")
    password = str(input("Enter password: "))
# check if password is MIN_LENGTH characters long.

for character in password:
    print("*", end="")
    # prints MIN_LENGTH asterisks to signify password is valid.
