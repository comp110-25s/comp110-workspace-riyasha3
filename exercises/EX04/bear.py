"""File to define Bear class."""

__author__: str = "730519187"


class Bear:
    """Creates a Bear class that represents the bears living by the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the attributes of age and hunger_score."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Stimulates how the population of bears changes day-to-day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Updates the hunger_score of the bear by the number of fish it ate."""
        self.hunger_score += num_fish
