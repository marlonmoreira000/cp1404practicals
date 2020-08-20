name = str(input("Enter name: "))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = str(input("Enter choice: "))

while choice != "Q":
    if choice == "H":
        print("Hello,", name)
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = str(input("Enter choice: "))
    elif choice == "G":
        print("Goodbye,", name)
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = str(input("Enter choice: "))
    else:
        print("Invalid input")
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = str(input("Enter choice: "))
print("Goodbye!")