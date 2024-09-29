"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """score to result converter"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    score = random.randint(0, 100)
    result = determine_result(score)
    print(result)


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


main()
