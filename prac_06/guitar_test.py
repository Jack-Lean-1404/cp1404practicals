"""Guess = 20mins, Actual = 14mins"""
from prac_06.guitar import Guitar


def main():
    """Tests for Guitar class"""


guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print(guitar)
print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")

main()
