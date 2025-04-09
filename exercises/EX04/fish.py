"""File to define Fish class."""

__author__: str = "730519187"


class Fish:
    """Creates a Fish class that represents the fish living in the river."""

    age: int

    def __init__(self):
        """Initializes the attributes of age."""
        self.age: int = 0
        return None

    def one_day(self):
        """Stimulates how the population of fish changes day-to-day."""
        self.age += 1
        return None
