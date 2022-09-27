"""Basic functions implementation for practice in python."""
__author__ = "730295059"


def only_evens(input: list[int]) -> list[int]:
    """Returns a new list with only even integers."""
    i = 0
    new_list = list()
    while i < len(input):
        if input[i]%2 == 0:
            new_list.append(input[i])
        i += 1
    return new_list

def concat(input: list[int], input_2: list[int]) -> list[int]:
    """Returns the combined list, one appended onto the other."""
    i = 0
    new_list = list()
    while i < len(input_2)+len(input):
        if i < len(input):
            new_list.append(input[i])
        else:
            new_list.append(input_2[i-len(input)])
        i += 1
    return new_list

def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns an subsection of the input list."""
    if start < 0: start = 0
    if end > len(input): end = len(input)
    new_list = list()
    i = start
    while i < end:
        new_list.append(input[i])
        i += 1
    return new_list
