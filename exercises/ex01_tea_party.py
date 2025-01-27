"""Calculating the total tea bags and treats and cost of the tea party based on the guest number"""

__author__: str = "730519187"


def main_planner(guests: int) -> None:
    """Main planner for the whole event"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculating the total tea bags needed for all the guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculate the total number of treats needed for all the guests."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost for the tea bags and treats."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
