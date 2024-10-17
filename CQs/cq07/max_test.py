"""Max tests"""

__author__ = "730641729"


from CQs.cq07.find_max import find_and_remove_max


def test_return_value():
    """Test if returns the expected value."""
    data = [3, 5, 2, 5]
    result = find_and_remove_max(data)
    assert result == 5


def test_mutation():
    """Test if mutates the input list as expected."""
    data = [1, 2, 3, 3, 3]
    find_and_remove_max(data)
    assert data == [1, 2]


def test_edge_case():
    """Test edge case with unconventional input"""
    data = [10, 10, 10]
    result = find_and_remove_max(data)
    assert result == 10
    assert data == []


if __name__ == "__main__":
    test_return_value()
    test_mutation()
    test_edge_case()
