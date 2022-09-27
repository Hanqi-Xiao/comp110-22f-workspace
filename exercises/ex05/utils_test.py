"""Tests for the utils.py functions."""
__author__ = "730295059"

from utils import *

def test_only_evens_use_duplicates() -> None:
    assert only_evens([1,2,3,4,5,6,5,4,3,2,7,4]) == [2,4,6,4,2,4]


def test_only_evens_use_short() -> None:
    assert only_evens([4,3,2,1]) == [4,2]


def test_only_evens_mutability() -> None:
    my_list = [1,2,3,4]
    assert only_evens(my_list) == [2,4]
    assert my_list == [1,2,3,4]


def test_sub_normal() -> None:
    assert sub([1,2,3,4,5,6], 1, 3) == [2,3]


def test_sub_negative() -> None:
    assert sub([1,2,3,4,5,6], -1, 3) == [1,2,3]


def test_sub_positive() -> None:
    assert sub([1,2,3,4,5], 3, 6) == [4,5]


def test_concat_normal() -> None:
    assert concat([1,2], [3,4]) == [1,2,3,4]

def test_concat_descend() -> None:
    assert concat([4,3], [2,1]) == [4,3,2,1]

def test_concat_empty() -> None:
    assert concat([1,2], []) == [1,2]