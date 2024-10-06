"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the user inputs something other than an Integer
2. When will a ZeroDivisionError occur?
    When the user inputs 0 ad the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes by adding a checking programming pattern
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("The denominator cannot be 0.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
