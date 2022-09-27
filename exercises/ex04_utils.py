"""replication of classic list type utilities."""

__author__ = 730295059


def all(match: list[int], template: int) -> bool:
    """Checks if list values match template."""
    i = 0
    if len(match) == 0:  # handles the edgecase of empty list
        return False
    while i < len(match):
        if match[i] != template:
            return False
        i += 1
    return True
    # return False if sum([1 if i != template for i in match]) > 1 else True.


def max(max_list: list[int]) -> int:
    """Max function for all integers."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    my_max = max_list[0]  # does not assume the max is above 0
    i = 0
    while i < len(max_list):
        if max_list[i] > my_max:
            my_max = max_list[i]  # updates max if higher number found
        i += 1  # iterates through max_list
    return my_max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines if the two lists numerically indistinguishable."""
    if len(list_1) != len(list_2):  # checks if lists are equal length
        return False
    i = 0
    while i < len(list_1):  # uses list_i to provide lists length
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


def main() -> None:
    """Main function."""
    assert all([1, 2, 1], 1) is False, "should be true"
    assert max([1, 2, 123, 3]) == 123, "should be 123"
    assert is_equal([1, 2, 3], [1, 2, 3]) is True, "should be false"
    assert is_equal([1, 2, 2], [1, 2, 3]) is False, "should be true"


if __name__ == "__main__":
    main()