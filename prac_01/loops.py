for i in range(1, 21, 2):
    print(i, end=' ')
print()

x = range(0, 101, 10)
for i in x:
    print(i, end=' ')
print()

number_of_stars1 = int(input("How many stars do you want to see? "))
for i in range(1, number_of_stars1 + 1):
    print('*', end=' ')
print()

number_of_stars2 = int(input("How many stars do you want to see? "))
for i in range(1, number_of_stars2 + 1):
    print(i * '*', end=' ')
    print()