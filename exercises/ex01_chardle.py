"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730295059"

# takes player input
word: str = input("Enter a 5-character word: ").lower()
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ").lower()
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print(f"Searching for {character} in {word}")

# matches character to each letter in word
match_count: int = 0
for x, i in enumerate(word):
    if i == character:
        match_count += 1
        print(f"{character} found at index {x}")

# expressions handel the edge case where you do not detect any instances of character in word, 
# and word plurality when only one instance is found
detection_count = (match_count if match_count > 0 else "No")
detection_count_plurality = ("instance" if match_count == 1 else "instances")
print(f"{detection_count} {detection_count_plurality} of {character} found in {word}")
