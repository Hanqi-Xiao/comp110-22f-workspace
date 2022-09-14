"""number guessing game"""
from random import randint
import re


used_operators: list = []
num: int = randint(0,100)
for i in range(6,0,-1):
    print('questions left =', i)
    try:
        question: str = input("evaluate an expression to find what num is, e.g. (num > 50):")
        _answer: bool = eval(question)
    except:
        print('invalid python expression')
        continue

    valid: bool = True
    operators: list = re.findall(r"\+|-|\*|\/|=|>|<|>=|<=|&|\||%|!|\^|\(|\)", question)
    print(operators, used_operators)
    for i in operators:
        if i in used_operators:
            transgression = i
            valid = False
        else:
            used_operators.append(i)

    if not valid:
        print(f"You've already used the {transgression} operator.") #the only correct way to aggress user input errors
    elif type(_answer) != bool:
        print("cheater cheater pumpkin eater, the answer to your question was not a True/False!")
    else:
        print(_answer)
    # if input("wanna_guess_now? Y/N").lower() == 'y' and i != 1:
    #     break

my_guess = int(input('Guess between 0-100:'))
if num == my_guess:
    print('hooray you win, my secret number was indeed', num)
else:
    print('you guessed wrong! The my secret number was', num)