FILENAME = "wimbledon.csv"


def main():
    """Read  and print details about Wimbledon."""
    records = get_data(FILENAME)
    champion, countries = process_records(records)
    display_results(champion, countries)


def process_records(records):
    """Create dictionary of champions and countries"""
    champion = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion[record[2]] += 1
        except KeyError:
            champion[record[2]] = 1
    return champion, countries


def display_results(champion, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_data(filename):
    """Get records from file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()
        for line in file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()