"""number guessing game"""
from random import randint


num: int = randint(0,100)
for i in range(5,0,-1):
    print('questions left =', i)
    try:
        _answer: bool = eval(input("evaluate an expression to find what num is, e.g. (num > 50):"))
    except:
        print('invalid python expression')
        continue
    if type(_answer) == bool:
        print(_answer)
    else:
        print("cheater cheater pumpkin eater, the answer to your question was not a True/False!")
    # if input("wanna_guess_now? Y/N").lower() == 'y' and i != 1:
    #     break

my_guess = int(input('Guess between 0-100:'))
if num == my_guess:
    print('hooray you win, my secret number was indeed', num)
else:
    print('you guessed wrong! The my secret number was', num)