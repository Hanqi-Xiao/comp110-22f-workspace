"""Function definition basic tutorial"""

def my_max(a:int=0, b:int=1) -> int:
    """returns largest"""
    return a if a >= b else b

my_max(6+6,7)