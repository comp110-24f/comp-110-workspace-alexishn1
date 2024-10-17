"""Utils EX05 assignment"""

__author__ = "730641729"


def only_evens(list1: list[int]) -> list[int]:
    result = []
    for num in list1:  # Loops through all numbers in list
        if num % 2 == 0:  # If num is even
            result.append(num)  # Add even numbers to empty list
    return result


def sub(list1: list[int], start_index: int, end_index: int) -> list[int]:
    result = []
    if len(list1) == 0 or start_index >= len(list1) or end_index <= 0:
        # Takes empty or invalid list into account
        return result
    if start_index < 0:  # Makes sure start index is not negative
        start_index = 0
    if end_index > len(list1):
        # Makes sure end index is not greater than length of list
        end_index = len(list1)
    for index in range(start_index, end_index):  # Builds list with correct numbers
        result.append(list1[index])
    return result


def add_at_index(list1: list[int], element: int, indx: int) -> None:
    if indx < 0 or indx > len(list1):  # If index is invalid raise error
        raise IndexError("Index is out of bounds for the input list")
    list1.append(0)
    index = len(list1) - 1
    while index > indx:  # Shift elements to right
        list1[index] = list1[index - 1]
        index -= 1
    list1[index] = element  # Insert element
