"""Guess = 30mins, Actual = ???mins"""
from prac_06.guitar import Guitar


def main():
    """Guitar program"""

    guitars = []

    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

        name = input("Name: ")

    if guitars:
        print("These are my guitars:")

        for i, guitar in enumerate(guitars, 1):

            vintage = "(Vintage)" if guitar.is_vintage() else ""
            print("Guitar {0}: {1.name:>15} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage))
        else:
            print("No guitars")

main()