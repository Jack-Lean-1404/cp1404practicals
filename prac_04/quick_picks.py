import random # I SPENT TO LONG ON THIS!!!!!!!!!!!!!!! AGHHHHHHHH!!!!!!

NUMBER_OF_COLUMNS = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("How many quick picks? "))

for pick in range(number_of_quick_picks):
    quick_pick_row = []
    for number in range(NUMBER_OF_COLUMNS):
        value = random.randint(MINIMUM, MAXIMUM)
        while value in quick_pick_row:
            value = random.randint(MINIMUM, MAXIMUM)
        quick_pick_row.append(value)
    quick_pick_row.sort()
    print(" ".join(f"{number:2}" for number in quick_pick_row))