"""Guess = 20mins, Actual = ??"""

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
        return f"{self.name} ({self.year}) : {self.cost}"

    # Gibson L-5 CES (1922) : $16,035.40

    def get_age(self):
        """Determine the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage based on age."""
        return self.get_age() >= VINTAGE_AGE