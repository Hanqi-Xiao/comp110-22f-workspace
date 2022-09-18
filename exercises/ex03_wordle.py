"""Budget wordle for the programmer. Does not produce a wordle block and incorrectly identifies the double yellow square edge case, cool for learning though."""

__author__ = "730295059"


def contains_char(text: str, chr: str) -> bool:
    """Obtains if the character exists in the secret word."""
    assert len(chr) == 1
    length = len(text)
    index = 0
    while index < length:
        if chr == text[index]:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Identify the color of each character in and produce the wordle color string."""
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
        index += 1
    return out_string


def input_guess(length: int) -> str:
    """Ensures input is equal in length with secret."""
    guess = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """Entry point for the game main loop."""
    lives: int = 6
    secret: str = "codes"
    length = len(secret)
    while lives > 0:
        turn = 7 - lives
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(length)
        out = emojified(guess, secret)
        if secret == guess:  # handles the winning edge case.
            print(out)
            print(f"You won in {turn}/6 turns!")
            return
        else:
            print(out)
        lives -= 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()

    
