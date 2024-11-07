from guitar import Guitar

def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)
    for guitar in guitars:
        print(guitar)



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

main()