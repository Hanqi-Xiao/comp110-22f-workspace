def love(subject: str) -> str:
    """Returns a loving string"""
    return f"I love you {subject}!!"

def spread_love(to: str, n: int) -> str:
    # love_note = str()
    # counter_boi = 0
    # while counter_boi < n:
    #     love_note += love(to) + '\n'
    #     counter_boi += 1
    # return love_note
    return "\n".join([love(to) for i in range(n)])