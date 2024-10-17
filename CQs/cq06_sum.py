"""Summing the elements of a list using different loops"""

__author__ = "730641729"


def w_sum(vals: list[float]) -> float:
    sum_num: float = 0.0
    index = 0
    while index < len(vals):
        sum_num += vals[index]
        index += 1
    return sum_num


def f_sum(vals: list[float]) -> float:
    sum_num: float = 0.0
    for elem in vals:
        sum_num += elem
    return sum_num


def f_range_sum(vals: list[float]) -> float:
    sum_num: float = 0.0
    for index in range(len(vals)):
        sum_num += vals[index]
    return sum_num
