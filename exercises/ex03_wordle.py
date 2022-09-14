"""Budget wordle"""

def contains_char(text: str, chr: str) -> bool:
    assert len(chr) == 1
    length = len(text)
    index = 0
    while index < length:
        if chr == text[index]:
            return True
        index += 1
    return False

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    out_string = ""
    index = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            out_string += "\U0001F7E9"
        elif contains_char(secret, guess[index]):
            out_string += "\U0001F7E8"
        else:
            out_string += "\U00002B1C"
        index == 1
    return out_string

def input_guess(guess: str, length: int) -> str:
    while len(guess) != length:
        guess = input(f"That was not {length} letters! Try again: ")


    
