"""Some exercising on dictionaries."""

__author__ = 730295059


def inside(value: str, alist: list[str]) -> bool:
    """Replacement for the python keyword 'in'."""
    for i in alist:
        if value == i:
            return True
    return False


def invert(a: dict[str, str]) -> dict[str, str]:
    """O(n**2) I think. This invert function only correctly type hints for UNIFORM dicts. This is kind of sad."""
    return_dict: dict[str, str] = {}
    exists: list[str] = []
    y: str = ""
    for x in a:
        y = a[x]  # value of 'a' at key 'x'.
        if not inside(y, exists):
            return_dict[y] = x
            exists.append(y)
        else:
            raise KeyError("Duplicated keys in inverted list.")
    return return_dict


def favorite_color_2(a: dict[str, str]) -> str:
    """Yes, python lists are ordered, and no I will not take advantage of that fact. Outputs the mode of some categorical values."""
    ordered_dict = dict[str, list[int]]  # Orders the dict with the second int in values being the order of the mapping pair's initiation to the dict.
    tracking_dict: ordered_dict = {}
    order: int = 0
    for x in a:
        y = a[x]
        if inside(y, list(tracking_dict.keys())):
            tracking_dict[y][0] += 1
        else:
            tracking_dict[y] = [0, order]
            order += 1
    max: int = 0
    max_name: str = ""
    max_order: int = order
    for j in tracking_dict:
        i = tracking_dict[j]
        if i[0] > max or (i[0] == max and i[1] < max_order):
            max = i[0]
            max_name = j
            max_order = i[1]
    return max_name


def favorite_color(color_dict: dict[str, str]) -> str:
    color_frequency: dict[str, int] = {}
    for key in color_dict:
        value = color_dict[key]
        if value in color_frequency:
            color_frequency[value] += 1
        else:
            color_frequency[value] = 1
    # Cycle through color frequency and determine max color frequency.
    frequency: int = 0
    max_frequency: int = 0
    max_key: str = ""
    for color in color_frequency:
        frequency = color_frequency[color]
        if frequency > max_frequency:
            max_key = color
            max_frequency = frequency
    return max_key

def count(a: list[str]) -> dict[str, int]:
    """Count mode of a list of strings."""
    return_dict: dict[str, int] = {}
    for i in a:  # iterates through all a.
        if i not in return_dict:
            return_dict[i] = 1
        else:
            return_dict[i] += 1
    return return_dict
