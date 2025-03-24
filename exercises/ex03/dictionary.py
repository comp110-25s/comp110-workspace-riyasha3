"""Using dictionaries."""

__author__: str = "730519187"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values."""
    new_inverted: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in new_inverted:
            raise KeyError("error: duplicated key")
        x: str = dictionary[key]
        new_inverted[x] = key
    return new_inverted


def count(old: list[str]) -> dict[str, int]:
    """Making a dictionary where the key is given in list and value is the number of times it appears."""
    new_dict: dict[str, int] = {}
    for value in old:
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1
    return new_dict


def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    my_list: list[str] = []
    max_color: str = ""
    for key in names_colors:
        my_list.append(names_colors[key])
    color_count = count(my_list)
    top_count: int = 0
    for key in color_count:
        value = color_count[key]
        if value > top_count:
            max_color = key
            top_count = value
    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Put a list of strings into its length."""

    new_dict: dict[int, set[str]] = {}
    for value in words:
        length = len(value)
        if length in new_dict:
            new_dict[key]

    return new_dict
