"""Implemting unit tests."""

__author__: str = "730519187"

import pytest
from dictionary import invert, count, favorite_color, bin_len


def test_invert() -> None:
    """Test use case for invert."""
    x: dict[str, str] = {"z": "a", "y": "a", "x": "c"}
    y: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(y) == x


def test_invert_2() -> None:
    """Tests the KeyError for this function."""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_invert_3() -> None:
    """Test edge case."""
    invert_dict: dict[str, str] = {}
    assert invert(invert_dict) == {}


def test_count() -> None:
    """Tests the use case of the function count."""
    frequencies: list[str] = ["pop", "rap", "indie", "pop"]
    assert count(frequencies) == {"pop": 2, "rap": 1, "indie": 1}


def test_count_1() -> None:
    """Tests the use case of the function count."""
    how_many: list[str] = ["cake", "candy"]
    assert count(how_many) == {"cake": 1, "candy": 1}


def test_count_2() -> None:
    """Tests an edge case of the function count."""
    frequencies: list[str] = []
    assert count(frequencies) == {}


def test_favorite_color() -> None:
    """Tests the use case of the function favorite_color."""
    max_favorite_color: dict[str, str] = {"RM": "red", "V": "blue", "JK": "blue"}
    assert favorite_color(max_favorite_color) == "blue"


def test_favorite_color_2() -> None:
    """Tests the use case of the function favorite_color."""
    testing: dict[str, str] = {
        "a": "green",
        "b": "green",
        "c": "red",
        "d": "blue",
        "e": "blue",
    }
    assert favorite_color(testing) == "green"


def test_favorite_color_3() -> None:
    """Testing edge case of the function favorite_color."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""


def test_bin_len() -> None:
    """Tests the use case of the function bin_len."""
    test: list[str] = ["the", "quick", "fox"]
    assert bin_len(test) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_2() -> None:
    """ "Tests the use case of the function bin_len."""
    test: list[str] = ["cat", "dog", "ant"]
    assert bin_len(test) == {3: {"cat", "dog", "ant"}}


def test_bin_len_3() -> None:
    """Tests the edge case of the function bin_len."""
    test: list[str] = []
    assert bin_len(test) == {}
