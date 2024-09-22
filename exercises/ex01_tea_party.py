"""EX01 Assignment"""

__author__ = "730641729"


def main_planner(guests: int) -> None:
    """Bring functions together"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # Guests needs to be converted to str (str+str)
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # Tea bag count needs to be converted to str
    print(
        "Treats: " + str(treats(people=guests))
    )  # Treat count needs to be converted to string
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=(tea_bags(people=guests)), treat_count=(treats(people=guests))
            )
        )
    )


def tea_bags(people: int) -> int:
    """Calculate amount of tea bags"""
    return 2 * people  # Return 2 tea bags per person


def treats(people: int) -> int:
    """Calculate amount of treats based on the number of tea bags"""
    return int(
        tea_bags(people=people) * 1.5
    )  # Call tea bag function because people want 1.5 treats per each tea


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea bags and treats"""
    return (
        tea_count * 0.50 + treat_count * 0.75
    )  # Total cost is tea and treat count times price added together


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
