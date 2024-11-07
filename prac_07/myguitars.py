from guitar import Guitar

def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

        name = input("Name: ")

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    save_guitars(filename, guitars)



def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
main()