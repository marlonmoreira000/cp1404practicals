def main():
    """ Rate university scores """

    score = float(input("Enter score: "))
    categorise_score(score)


def categorise_score(score):
    """ Categorise scores from 0 to 100 """
    if score < 0 or score > 100:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print("Excellent")


main()
