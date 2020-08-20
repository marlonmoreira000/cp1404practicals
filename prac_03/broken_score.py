def main():
    """ Rate university scores """

    score = float(input("Enter score: "))
    category = categorise_score(score)
    print(category)


def categorise_score(score):
    """ Categorise scores from 0 to 100 """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
