"""EX06 Dictionaries Assignment"""

__author__ = "730641729"


def invert(dict_strings: dict[str, str]) -> dict[str, str]:
    invert_dict = {}  # start with empty dict for inverted dict
    for key in dict_strings:  # go through each key
        value = dict_strings[key]
        if value in invert_dict:  # if value is already found in inverted dict
            raise KeyError("Error: Duplicate key")  # error message
        invert_dict[value] = key  # switch key and value
    return invert_dict


def favorite_color(names_colors: dict[str, str]) -> str:
    if not names_colors:
        return ""  # Handles empty dictionary
    color_count: dict[str, int] = {}  # start with empty dict for color count
    most_popular: str = ""  # start with empty string
    max_count = 0  # start with max count as 0
    for name in names_colors:
        color = names_colors[name]  # name is key and color is value
        if color in color_count:  # if color is found
            color_count[color] += 1  # add one
        else:
            color_count[color] = 1  # only 1 of color
        if color_count[color] > max_count:  # if color count is greater than max count
            max_count = color_count[color]  # color count becomes max count
            most_popular = color
    return most_popular  # return most popular color


def count(dict_inputs: dict[str, int]) -> dict[str, int]:
    result: dict[str, int] = {}  # Start with empty dict for results
    for elem in dict_inputs:  # loop through each element in dict_inputs
        if elem in result:
            result[elem] += 1  # increase count by 1
        else:
            result[elem] = 1
    return result  # return result dict


def alphabetizer(list_words: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}  # start with empty dictionary for results
    for word in list_words:  # loop through each word in list_words
        first_letter = word[0].lower()  # find out first letter in lowercase
        if first_letter in result:
            result[first_letter].append(word)  # add word to result list
        else:
            result[first_letter] = [word]
    return result  # return result dict


def update_attendance(
    dict_inputs: dict[str, list[str]], day: str, student: str
) -> None:
    if day in dict_inputs:  # check if day is in dict already
        if student not in dict_inputs[day]:  # check if student is already in list
            dict_inputs[day].append(student)  # add student to list
    else:
        dict_inputs[day] = [student]  # create new list with student
    return None
