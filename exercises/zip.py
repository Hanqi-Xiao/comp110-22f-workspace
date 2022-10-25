"""Simulation of the zip function."""

from binascii import b2a_hex


def my_zip(a: list[int], b: list[int]) -> dict[int, int]:
    if len(a) != len(b):
        print("Lists of unequal size.")
        return {}
    result: dict[int, int] = {}
    i: int = 0
    while i < len(b):
        result[a[i]] = b[i]
        i += 1
    return result

def my_zip_2(a: list[int], b: list[int]) -> dict[int, int]:
    if len(a) != len(b):
        print("Lists of unequal size.")
        return {}
    return {a[i]: b[i] for i in range(len(b))}

print(my_zip([1,4], [1,2]))