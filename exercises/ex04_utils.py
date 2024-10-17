"""EX04 Assignment"""

__author__ = "730641729"


def all(list_ints: list[int], num: int) -> bool:
    if len(list_ints) == 0:  # If list is empty it should return false
        return False
    for elem in list_ints:
        if elem != num:
            return False
    return True  # Bool returns true if all list numbers match num


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    large_num = input[0]  # Assume first element is largest untill proven otherwise
    for elem in input[1:]:
        if elem > large_num:
            large_num = elem

    return large_num  # Returns largest number out of elems


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):  # Checks if two lists are same length
        return False  # If not same length return false
    for index in range(len(list1)):  # Checks index of each element of lists
        if list1[index] != list2[index]:
            return False  # If elements at each index are not equal it returns false
    return True  # If elements are all equal it will return true instead


def extend(list1: list[int], list2: list[int]) -> None:
    # Mutate list1 by appending list2 values to end of list1
    for elem in list2:
        list1.append(elem)
