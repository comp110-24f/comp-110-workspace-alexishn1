"""Practice with lists"""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

print(my_numbers)

# String analogy
my_name: str = ""  # literal
my_name: str = str()  # constructor


# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)

# Creating an already populated list/subscription notation/indexing
game_points: list[int] = [102, 86, 94]
print(game_points[2])

# Modifying by index
game_points: list[int] = [102, 86, 94]
game_points[1] = 72
print(game_points)

# Length of list
print(len(game_points))

# Remove item from list
game_points.pop(1)
print(game_points)


# Practice
def display(int_list: list[int]) -> None:
    """Displays all elements of int list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1
    display(int_list=game_points)
