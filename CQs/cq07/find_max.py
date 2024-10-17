"""Find max"""

__author__ = "730641729"


def find_and_remove_max(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return -1

    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num

    while max_value in numbers:
        numbers.pop(numbers.index(max_value))

    return max_value
