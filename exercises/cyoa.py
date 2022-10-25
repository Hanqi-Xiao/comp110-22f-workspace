"""Choose your own adventure game with a hyper sensitive narrator."""
# Woe, the parade of unused/unusable tools. 
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from os import system, name
# from threading import Thread
# import sys
from time import sleep
import itertools
from random import randint
import re

__author__ = "730295059"
points: int = 0  # Rq 0.0 fulfilled.
EMOJI: str = "\U0001F604"  # Rq 6.1 fulfilled. The victory face.
REQUIRED_POINTS: int = 30
ohno_points: int = 0
player: str = ""  # Rq 0.1 fulfilled.
processing: bool = False
event_id: int = 0
turns: int = 0
gaming: bool = True


def main() -> None:  # Rq 1.0 fulfilled.
    """Main loop, using some global variables. Curiously similar to instance variables. Is OOP the good?"""
    global points 
    global event_id
    global player
    global turns
    global gaming
    print("The following is an expression of romantic emotionalism and berserk expressionism. Engage with seriousness at your own risk.")
    input("[Press Enter to Begin]")
    while gaming:  # Rq 5.0 fulfilled.
        print(f"<Current points: {points}>")
        if event_id == 0:
            greet()
            initial_choice()  # Rq 1.1 fulfilled.
        elif event_id == 1:
            event_1()
        elif event_id == 2:
            # Event 2 has outputs which must be unified with global variables.
            result: tuple[int, int] = event_2(points)
            points = result[0]  # Rq 4.3 fulfilled.
            event_id = result[1]
        elif event_id == 3:
            # Gaming is a local variable to main(), so it must be updated here to end the game.
            event_3(ohno_points, points, turns)
        turns += 1


def greet() -> None:  # Rq 2.0 fulfilled.
    """Greets the player--and names the player too."""
    global player 
    global event_id
    global points
    print("""Welcome to the world of Egi-gogi-boli, 
    I am your nicemost hyperbest sentiment machine 'Milker'
    I will help you study for the entrance exam to the pretigous Egi-gogi-boli Megagreat Skool... to get in you must earn POINTS!
    follow me and welcome your destiny.""")  # Rq 2.1 fulfilled.
    input(">Press Enter<")
    print("""First stop, the ritual of naming.""")
    process()
    player = input("Your name determines your fate, it's time to pick yours, what is your name today? ")
    # The next four lines prints a fun command line animation that simulates the milker machine thinking. Also tests out threading for fun.
    process()
    print(f"Identity registered, you are now {player}.")  # Rq 2.2 fulfilled.
    process()
    print("""You are currently interacting with me through a mental command line interface. 
            It looks, feels, tastes, and audios just like a normal command line interface.""")
    points += event_speak(f"{player} comments: ")
    event_id = 1


def initial_choice() -> None:
    """Initial choice function to facilitate selection of player path."""
    global event_id
    global gaming
    print("But enough talk....")
    print("Choose a path: 1) Trust in me and prepare for the exam; 2) Take the exam without studying;\n 3) Walk away from me, Egi-gogi-boli, and everything meaningful in life.")
    choice: str = input(f"{player}'s Choice, 1 or 2 or 3: ")
    if choice == "3":
        print("You walk away from everything, and the Egi-gogi-boli ends...")
        process(2.0)
        print("GAME over.")
        gaming = False
    elif choice == "2":
        event_id = 3
    else:  # This intentionally funnels all incorrect inputs into the last option.
        event_id = 1


def event_1() -> None:  # Rq 3.1 fulfilled.
    """Event where milker asks the player to play a number guessing game to test the player's intelligence."""
    global player
    global points
    global event_id
    used_operators: list[str] = []
    num: int = randint(0, 100)  # Rq. 6.2 fulfilled.

    process()
    print(f"{player}, you will GET POINTS by evluating expressions to guess a number between randint 0-100!")
    print("evaluate any valid python expression to find what num is, the result of the expression must be a boolean. e.g. (num > 50)\nLimitations: You may only use one expression once. Expressions can include % // / > < + - = etc\nHint, python masters are unbounded and limitless.")
    input(">Press Enter<")
    for i in range(6, 0, -1):

        print('\nquestions left =', i)
        try:
            question: str = input("Your expression:")  # Rq 3.1 fulfilled.
            process()
            _answer: bool = eval(question)
        except NameError and SyntaxError:
            print('invalid python expression')
            continue

        valid: bool = True
        operators: list[str] = re.findall(r"\+|-|\*|\/|\\|=|>|<|&|\||%|!|\^", question)
        new_used_operators: list[str] = []
        op_count: int = 0
        for j in operators:
            if j in used_operators:
                transgression: str = j
                valid = False
            else:
                if not (j in new_used_operators):
                    new_used_operators.append(j)
                    op_count += 1
        used_operators += new_used_operators

        if not valid:
            print(f"You've already used the {transgression} operator.")  # the only correct way to address user input errors
            for k in range(op_count):
                used_operators.pop()
        elif type(_answer) != bool:
            print("cheater cheater pumpkin eater, the answer to your question was not True/False!")
        else:
            print(_answer)
        print("Used operators:", used_operators)
    my_guess: int = 0
    try:
        my_guess = int(input('Guess between 0-100:'))
    except ValueError:
        print("Bahh, your response isn't a real number!")
        my_guess = -1
    if num == my_guess:
        print(f'{player}, you win, my secret number was indeed', num, "You earn", 15 - len(used_operators), "POINTS.")
        points += 15 - len(used_operators)  # Rq 3.2 fulfilled.
        # not showing used operators
    else:
        print(f'{player}, you guessed wrong! My secret number was', num)
    print("Game Over.")
    event_id = 2


def event_2(current_points: int) -> tuple[int, int]:  # Rq 4.1 fulfilled.
    """Function fullfilling requirement 4 that judges whether it is ok for the player to not be nice."""
    print("Let me check how many points you have.")
    process()
    current_event_id: int = 2
    if current_points < 30:
        print(f"You do not have enough milker POINTS to succeed at Egi-gogi-boli Skool. You have only {points}/{REQUIRED_POINTS} of points. Is anything you want to say?")
        current_points += event_speak(f"{player} says: ")  # Rq 4.2 fulfilled.
        if input("Let's switch topics, do you want to get more points? Y/N: ").lower() == "n":
            print("Your resolve is inspiring, have 7 POINTS.")
            current_points += 7  # Rq 4.2 fulfilled.
            current_event_id = 3
        else:
            current_event_id = 1
    else:
        print("You've proven yourself to me. You have collected 30 POINTS. Congradulations, I deem you worthy of the Egi-gogi-boli Skool exam.")
        current_event_id = 3
    return (current_points, current_event_id)


def event_speak(msg: str) -> int:
    """Check if the player has said a nice thing. I initially planned to use sentimental analysis, but realized I couldn't use any libraries or read any txt files."""
    global ohno_points
    global player
    nice_words: list[str] = [r"Happy", r"HAHA", r"Love", r"Great", r"Good", r"MILKER", r"NICE"]
    used_word: str = ""
    bonus_points: int = 0
    response: str = input(msg)
    for word in nice_words:
        if word in response:
            bonus_points += 5
            ohno_points += 5
            used_word = word
            print(f"HAHAH, you are the NICE {player}, you used the word '{used_word}'! I will give you 5 'points'.")
            player = f"NICE-{player}"
            input(">Press Enter<")
            return bonus_points
    print("I like to heard nice things, like Happy, HAHA, Love, Great, and Good! You are not being NICE, you are not a milker suporter.")
    input(">Press Enter<")
    return bonus_points


def event_3(points: int, ohno_points: int, turns: int) -> None:
    """When the game ends this functin congradulates you!"""
    print(f"You have arrived at the exam room of the Egi-gogi-boli School! {EMOJI}")
    print(f"You have collected {points}/30 required POINTS in {turns} turns, but {ohno_points} are points instead of POINTS.")
    print("Your studying with Milker isn't just preparation, it IS the exam. The exam involved whether you would illegally bribe Milker with NICE words to get points.")
    input(">Press Enter<")
    if points >= 30:
        if ohno_points > 5:
            print("You tried BRIBING Milker more than once for his points, by using NICE words. You don't deserve Egi-gogi-boli.")
        else:
            process(3.0)
            print("...Oops, it looks like you don't have much monie, in this case, you must obtain 50 points to enter the MegaGreat Egi-gogi-boli school.")
            if points >= 50:
                print("Happy Birthday! You must be honored to join Egi-gogi-boli Megagreat Skool!")
                process(3.0)
                print("But something doesn't feel right...")
                if input("You are given a choice to restart and make a different choice, do you accept? Y/N: ").lower() != "n":
                    global event_id
                    event_id = 0
                    return

    print("'You have failed, Die.', said the spirit of Egi-gogi-boli.")
    process()
    print(f"{player} died.")
    if input("You are given a choice to restart and make a different choice, do you accept? Y/N: ").lower() != "n":
        event_id = 0
        return

    global gaming 
    gaming = False


def process(process_time: float = 1.0, animate_speed: float = 0.15) -> None:
    """A toy function that generates a fun animation which simulates the character milker's processing speed."""
    timer: float = 0.0
    for c in itertools.cycle(["*  ", "** ", "***"]):
        if timer >= process_time:
            break
        print('\r<processing ' + c, end="")
        sleep(animate_speed)
        timer += animate_speed
    print("\r<processed  ***>")
    sleep(.5)


if __name__ == "__main__":
    main()