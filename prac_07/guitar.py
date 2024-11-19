CURRENT_YEAR = 2024
VINTAGE_AGE = 50

class Guitar:
    """Stores details about a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        """Return guitar details."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        """Define the 'less than' operator to compare guitars by year."""
        return self.year < other.year
