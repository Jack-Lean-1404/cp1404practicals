class Band:
    """Band class."""

    def __init__(self, name=""):
        """Initialise a Band with a name and a list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string of the Band."""
        musician_list = ", ".join([str(musician) for musician in self.musicians])
        return f"{self.name} ({musician_list})"

    def add(self, musician):
        """Add a musician to the band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Simulate the band playing."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)