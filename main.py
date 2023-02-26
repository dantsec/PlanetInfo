from sys import stdout
from time import sleep

def set_args() -> str:
    """Seting arguments to make the program functionally
    """
    import argparse

    parser = argparse.ArgumentParser(description='Planet and moons information', usage="python3 main.py [-h HELP] [-c CURIOSITY] [-f FILE] [-p PLANET_NAME] [-a ANIMATION]")
    parser.add_argument("-p", "--planet", type=str,help="Planet or star for consultation.")
    parser.add_argument("-f", "--file", type=str, help="Save data to a file")
    parser.add_argument("-c", "--curiosity", action='count', help="Want to know some curiosities?")
    parser.add_argument("-a", "--animation", action="store_true", help="Turn on the typing animation")

    return parser.parse_args()

def typeAnim(text: str, isOn: bool = set_args().animation, speed: int = 50):
    """Function for the typing animation.
    """
    if isOn:
        seconds = 1 / speed
        for char in str(text):
            sleep(seconds)
            stdout.write(char)
            stdout.flush()
    else:
        print(text)

if __name__ == '__main__':
  from src.packages.run import App
  args = set_args()
  App.run(args)