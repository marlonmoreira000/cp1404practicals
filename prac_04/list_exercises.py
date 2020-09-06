"""This program takes in 5 numbers and puts them in a list.
It then prints various properties of this set of numbers"""

# number_of_numbers = 5
# numbers = []
#
# for i in range(1, number_of_numbers + 1):
#     number = int(input("Number: "))
#     numbers.append(number)
#
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[-1]))
# print("The smallest number is {}".format(min(numbers)))
# print("The largest number is {}".format(max(numbers)))
# print("The average of numbers is {}".format(sum(numbers) / len(numbers)))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("Enter username: "))

if username in usernames:
    print("Access granted.")
else:
    print("Access denied.")