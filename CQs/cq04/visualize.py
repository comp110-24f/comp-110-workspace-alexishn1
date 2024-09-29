"""Visualize file"""

__author__ = "730641729"

from CQs.cq04.concatenation import concat

from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

if __name__ == "__main__":
    print(concat(x, y))

    get_coords(x, y)
