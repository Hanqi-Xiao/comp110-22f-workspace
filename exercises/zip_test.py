"""Test file for zip.py."""
from zip import my_zip_2 as my_zip

def test_zip_standard() -> None:
    assert my_zip([1, 4, 9, 16], [1, 2, 3, 4]) == {1: 1, 4: 2, 9: 3, 16: 4}
    print("Hello there.")

def test_empty() -> None:
    assert my_zip([], []) == {}

def test_unequal() -> None:
    assert my_zip([1, 4], [1]) == {}