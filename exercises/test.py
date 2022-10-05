with open("exercises\positive_words.txt", "r") as f:
    print ([i.strip() for i in f.readlines()])