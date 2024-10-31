"""Guess = 25mins, Actual = 20"""

class ProgrammingLanguage:
    """Represent a Programming language object."""

    def __init__(self, language, typing, reflection, year):
        """Initialise a programming language instance."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def __str__(self):
        """Return language details."""
        return f"{self.language}, {self.typing}, Reflection = {self.is_dynamic()}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic."""
        return self.typing == "Dynamic"
