# a.
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
stars = ""
number_of_stars = int(input("Please enter number of stars: "))
for i in range(number_of_stars):
    stars = (stars + "*")
print(stars)

# d.
stars = ""
number_of_stars = int(input("Please enter number of stars: "))
for i in range(number_of_stars):
    stars = (stars + "*")
    print(stars)
print()
