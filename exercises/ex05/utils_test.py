"""Utils Test EX05 assignment"""

__author__ = "730641729"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


# 3 tests for only evens
def test_only_evens_no_evens() -> None:  # Edge case
    """Test only_evens when all numbers are odd"""
    assert only_evens([1, 3, 5, 7]) == []


def test_only_evens_test() -> None:  # Use case
    """Test only_evens returns expected value"""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_no_mutates() -> None:  # Use case
    """Test only_evens modfiies input correctly(no mutates)"""
    nums = [1, 2, 3, 4]
    only_evens(nums)
    assert nums == [1, 2, 3, 4]


# 3 tests for sub
def test_sub_test() -> None:  # Use case
    """Test sub returns expected value"""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_no_mutates() -> None:  # Use case
    """Test sub modifies input correclty (no mutates)"""
    nums = [1, 2, 3, 4]
    sub(nums, 1, 3)
    assert nums == [1, 2, 3, 4]


def test_sub_invalid_range() -> None:  # Edge case
    """Test sub with invalid range"""
    assert sub([1, 2], 3, 6) == []


# 3 tests for add_at_index
def test_add_at_index_test() -> None:  # Use case
    """Tests add_at_index returns expected value"""
    nums = [1, 2, 4]
    add_at_index(nums, 3, 2)
    assert nums == [1, 2, 3, 4]


def test_add_at_index_mutates() -> None:  # Use case
    """Tests add_at_index mutates correctly"""
    nums = [1, 2]
    add_at_index(nums, 0, 0)
    assert nums == [0, 1, 2]


def test_add_at_index_invalid() -> None:  # Edge case
    """Tests add_at_index when index is invalid"""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 5, 4)


if __name__ == "__main__":
    pytest.main()
