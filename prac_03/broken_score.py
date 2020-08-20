import random

def main():
    """ Rate university scores """

    score = int(input("Enter score: "))
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

def generate_random_score():
    print(random.randint(0, 100))
    # TODO: I'm not sure how you want me to integrate this function into the main function? Not exactly sure what you are asking for.

main()
