def set_args() -> str:
    """Seting arguments to make the program functionally
    """
    import argparse

    parser = argparse.ArgumentParser(description='Planet and moons information', usage="python3 main.py [-h HELP] [-c CURIOSITY] [-f FILE] [-p PLANET_NAME]")
    parser.add_argument("-p", "--planet", type=str,help="Planet or star for consultation.")
    parser.add_argument("-f", "--file", type=str, help="Save data to a file")
    parser.add_argument("-c", "--curiosity", action='count', help="Want to know some curiosities?")

    return parser.parse_args()


if __name__ == '__main__':
  from src.packages.run import App
  args = set_args()
  App.run(args)
