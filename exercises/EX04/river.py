"""File to define River class."""

__author__: str = "730519187"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Creates a River class that represents the river ecosystem."""

    day: int  # tells what day of the river's lifecycle it is
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes bears or fish if they reach a certain age."""
        new_bears = []
        new_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)

        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.fish = new_fish
        self.bears = new_bears
        return None

    def bears_eating(self):
        """Allows bears to eat fish if enough is available lowering fish population."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                eat_fish: int = 3
                self.remove_fish(eat_fish)
                bear.eat(eat_fish)
        return None

    def check_hunger(self):
        """Checks if the bear has starved and removes from population if it did."""
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)
        self.bears = full_bears
        return None

    def repopulate_fish(self):
        """Repopulates the fish population when an offspring is born."""
        for _ in range(0, (len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Repopulates the bear population when an offspring is born."""
        for _ in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Allows the population of fish and bear to be seen in a particular day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Stimulates a week of life in the river."""
        x: int = 0
        while x < 8:
            self.one_river_day()
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes fish from the population."""
        for _ in range(0, amount):
            self.fish.pop(0)
