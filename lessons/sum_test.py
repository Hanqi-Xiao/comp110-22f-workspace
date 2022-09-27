"""Tests the sum function."""
from lessons import sum
print(sum.sum_list([1.3,2.2,3.2]))

def test_sum_empty() -> None:
    assert sum.sum_list([]) == 0


def test_sum_negative() -> None:
    assert sum.sum_list([-1.0]) == -1.0


def test_sum_multiple() -> None:
    assert sum.sum_list([1.0, 2.0, 5.0]) == 8.0


def test_sum_pos_neg_multiple() -> None:
    assert sum.sum_list([-1.0, 2.0, 5.0]) == 6.0