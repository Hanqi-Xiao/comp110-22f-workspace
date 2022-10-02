"""Choose your own adventure game with a hyper sensitive narrator."""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from os import system, name
from time import sleep
import itertools
from threading import Thread
import sys

points = int()
player = ""
processing = False

class CyoaHelper():
    def __init__():
        pass

def main():
    """Main loop."""
    global points 
    points = 0
    greet()
    process()
    print("""You are currently interacting with me through a mental command line interface. 
    What makes a mental command line interface different from a physical one you ask?
    There isn't a difference.""")
    print("l")


def greet() -> None:
    """Greets the player"""
    global player 
    global processing
    msg = "Welcome to the world of Egi-gogi-boli, here you have only one goal: SKOOL. Who am I? Why, I am you! I am your nicemost hyperbest sentiment machine a.k.a. your subconcious. I will guide you in the entrance exam to the pretigous Egi-gogi-boli Megagreat Skool... follow me and welcome your destiny.\nFirst stop, the ritual of naming."
    print(msg)
    player = input("Your name determines your fate, it's time to pick yours, what is your name today? ")
    # The next four lines prints a fun command line animation that simulates the milkman machine thinking. Also tests out threading for fun.
    process()
    print(f"Identity registered, you are now {player}.")


def question(input: int, question: str) -> tuple[int, int]:
    pass


def processing_animation_retired(animate_speed: float = 0.15) -> None:
    """Obsolete: used to produce milkman animation via threading."""
    for c in itertools.cycle(["*  ", "** ", "***"]):
        if not processing:
            break
        print('\rloading ' + c, end="")
        sleep(animate_speed)
    print("\rloaded    ", end="\n")


def process_retired(processing_time: float = 1, function: object = sleep, arguments: list = None) -> None:
    """Obsolete: A function that produces an animation when the milkman is processing something, whether it be a real function, or nothing at all. The default behavior is to produce a 1 second processing animation."""
    global processing
    processing = True
    Thread(target=processing_animation_retired, daemon=True).start()
    if repr(function) == "<built-in function sleep>":
        function(processing_time)
    else:
        function(*arguments)
    processing = False


def process(process_time: float = 1.0, animate_speed: float = 0.15) -> None:
    """A toy function that generates a fun animation which simulates the character Milkman's processing speed."""
    timer = 0
    for c in itertools.cycle(["*  ", "** ", "***"]):
        if timer >= process_time:
            break
        print('\rprocessing ' + c, end="")
        sleep(animate_speed)
        timer += animate_speed
    print("\rprocessed  ***")
    sleep(.5)



if __name__ == "__main__":
    main()


