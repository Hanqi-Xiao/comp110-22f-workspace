"""Wordle where you only get one change to guess correctly."""
__author__: str = "730295059"
secret: str = "python"
length: int = len(secret)
guess: str = input(f"What is your {length}-letter guess? ")
while len(guess) != length:
    guess = input(f"That was not {length} letters! Try again: ")

# check if guess matches length, and how much it matches length.
if guess == secret:
    print("\U0001F7E9" * length)
    print("Woo! You got it!")
else:
    index: int = 0
    
    # loops through matching indexes in guess and secret for green matches. 
    while index < length:
        if guess[index] == secret[index]:
            print("\U0001F7E9", end='')
        else: 
            is_exist: bool = False
            is_exist_index: int = 0
            # only loops through all letters in secret to check for existence if no green matches.
            while is_exist_index < length: 
                if guess[index] == secret[is_exist_index]:
                    is_exist = True
                is_exist_index += 1
            if is_exist: 
                print("\U0001F7E8", end='')
            else:
                print("\U00002B1C", end='')
        index += 1
    print("\nNot quite. Play again soon!")