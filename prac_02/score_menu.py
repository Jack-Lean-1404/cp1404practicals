def main():
    """Score menu program"""
    menu = """(G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""

    score = get_valid_score()
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            convert_score_to_stars(score)
        else:
            print("Invalid option")

        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_score():
    """Gets a valid score"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """determines result from the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score >= 90:
        return "Excellent"
    else:
        return "Passable"


def convert_score_to_stars(score):
    """Print the score as stars'"""
    print("*" * score)


main()
