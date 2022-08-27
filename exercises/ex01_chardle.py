"""Chardle Program a base simulation of wordle where the user inputs a 5 letter string.
They also input a character to match. The program determines how many times that character appears in 
the word.

A Character - Worlde or Chardle Game
"""

__author__ = "730295059"

# takes player input
word = input("Enter a 5-character word: ").lower()
character = input("Enter a single character: ").lower()
print("Searching for %s in hello" % (character))

# matches character to each letter in word
match_count = 0
for x, i in enumerate(word):
    if i == character:
        match_count += 1
        print(f"{character} found at index {x}")

# my expression handels the edge case where you do not detect any instances of character in word
my_expression = (match_count if match_count > 0 else "No")
print(f"{my_expression} instances of {character} found in {word}")

# if word[0] == character:
#     match_count += 1
#     print(f"{character} found at index {0}")

# if word[1] == character:
#     match_count += 1
#     print(f"{character} found at index {1}")