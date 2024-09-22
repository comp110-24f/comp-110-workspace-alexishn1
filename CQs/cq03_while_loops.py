"""CQ03 Assignment"""

__auhtor__ = "730641729"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # count has initial value of 0
    i: int = 0  # tracks index
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1  # add 1 to count each time character is found
        i += 1  # increase index by 1 everytime
    return count


print(num_instances("hello", "o"))
