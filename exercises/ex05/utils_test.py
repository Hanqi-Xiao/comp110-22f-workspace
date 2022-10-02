"""Tests for the utils.py functions."""
__author__ = "730295059"

from utils import only_evens, sub, concat


def test_only_evens_use_duplicates() -> None:
    """Check if list works with duplicates."""
    assert only_evens([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 7, 4]) == [2, 4, 6, 4, 2, 4]


def test_only_evens_use_short() -> None:
    """Inner thoughts: This docstring is really redundent."""
    assert only_evens([4, 3, 2, 1]) == [4, 2]


def test_only_evens_mutability() -> None:
    """9 whole docstrings? Most tests are self explainatory. This one declares a variable to test whether inputs have been mutated."""
    my_list = [1, 2, 3, 4]
    assert only_evens(my_list) == [2, 4]
    assert my_list == [1, 2, 3, 4]


def test_sub_normal() -> None:
    """I get that this might be fullfilling a standard."""
    assert sub([1, 2, 3, 4, 5, 6], 1, 3) == [2, 3]


def test_sub_negative() -> None:
    """But this lintcode is seriously inflexible."""
    assert sub([1, 2, 3, 4, 5, 6], -1, 3) == [1, 2, 3]


def test_sub_positive() -> None:
    """For example, disallowing if i > len(input): start = 1."""
    assert sub([1, 2, 3, 4, 5], 3, 6) == [4, 5]


def test_concat_normal() -> None:
    """It is much easier to read when on one line."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concat_descend() -> None:
    """To force two lines makes the code ugly and long."""
    assert concat([4, 3], [2, 1]) == [4, 3, 2, 1]


def test_concat_empty() -> None:
    """Although I get its usaged in other times."""
    assert concat([1, 2], []) == [1, 2]
