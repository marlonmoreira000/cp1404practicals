sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = 0.1 * sales
    else:
        bonus = 0.15 * sales
    print("bonus =", bonus)
    sales = float(input("Enter sales: $"))
