"""Testing file for dictionary functions."""
from dictionary import invert, favorite_color, count
import pytest


def test_count_1() -> None:
    """Testing usecase for count."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_2() -> None:
    """Testing usecase for count."""
    assert count(["a", "a"]) == {"a": 2}


def test_count_3() -> None:
    """Testing border case for count."""
    assert count([]) == {}


def test_favorite_color() -> None:
    """Test use case."""
    assert favorite_color({"Mknm": "blue", "KILIER": "red", "Sdsda": "blue", "KLKSD": "red"}) == "blue"


def test_favorite_color_2() -> None:
    """Test use case."""
    assert favorite_color({"Mknm": "red", "KILIER": "blue", "Sdsda": "red", "KLKSD": "blue"}) == "red"


def test_favorite_color_3() -> None:
    """Border use case."""
    assert favorite_color({"Mknm": "blue"}) == "blue"


def test_invert_1() -> None:
    """Test use case."""
    assert invert({"a": "b"}) == {"b": "a"}


def test_invert_2() -> None:
    """Test use case long."""
    assert invert({"a": "b", "c": "e"}) == {"b": "a", "e": "c"}


def test_invert_3() -> None:
    """Border case."""
    with pytest.raises(KeyError):
        invert({"a": "b", "c": "b"})