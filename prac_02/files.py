# code for section 1
name = str(input("Enter your name: "))
out_file = open("name.txt", 'w')
out_file.write("{}".format(name))
out_file.close()

# code for section 2
in_file = open("name.txt", 'r')
file_contents = in_file.read()
print("Your name is {}.".format(name))
in_file.close()

# code for section 3
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

# code for section 4
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    total += int(line)
print(total)
