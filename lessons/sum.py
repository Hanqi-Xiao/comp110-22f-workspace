"""Simple nonfunctional sum function."""

def sum_list(input: list[float]) -> float:
    """A toy function that always returns 1."""
    sum: float = 0
    i: int = 0
    while i < len(input):
        sum += input[i]
        i += 1
    return sum