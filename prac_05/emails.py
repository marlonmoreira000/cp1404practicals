dict = {}
email = [] # initialise variable

while email != "":
    email = str(input("Email: "))
    name = email.split("@")[0]
    if name.count(".") > 0:
        name = "{} {}".format(name.split(".")[0].title(), name.split(".")[1].title())
        name_confirmation = str(input("Is your name {}? (Y/n) ".format(name)))
        if name_confirmation == "no" or name_confirmation == "n":
            name_clarification = str(input("Name: "))
            dict[name_clarification] = email
        elif name_confirmation == "y" or name_confirmation == "":
            dict[name] = email

    else:
        name_confirmation = str(input("Is your name {}? (Y/n) ".format(name)))
        if name_confirmation == "no" or name_confirmation == "n":
            name_clarification = str(input("Name: "))
            dict[name_clarification] = email
        elif name_confirmation == "y" or name_confirmation == "":
            dict[name] = email

for name in dict:
    print("{} ({})".format(name, dict[name]))