"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Temperature converter program"""
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_to_fahrenheit()
        elif choice == "F":
            convert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius():
    """Converts fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = ((fahrenheit - 32) * 5 / 9)
    print(f"Result: {celsius:.2f} C")


def convert_celsius_to_fahrenheit():
    """Converts celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
