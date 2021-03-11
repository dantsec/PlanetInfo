def sargs():
  import argparse

  parser = argparse.ArgumentParser(description='Planet and moons information', usage="python3 main.py [-h] [-p] [--planet] PLANET_NAME")
  parser.add_argument(
    "-p", 
    "--planet", 
    type=str,
    required=True, 
    help="Planet or star for consultation."
    )
  
  return parser.parse_args()
