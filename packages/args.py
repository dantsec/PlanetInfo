def args():
  import argparse

  parser = argparse.ArgumentParser(description='Planet and moons information', usage="python3 main.py [-h] [-p PLANET_NAME] [-f FILE_TO_SAVE_DATA]")
  parser.add_argument(
    "-p", 
    "--planet", 
    type=str,
    help="Planet or star for consultation."
    )
  parser.add_argument(
    "-f",
    "--file",
    type=str,
    help="Save data to a file"
  )
  parser.add_argument(
    "-c",
    "--curiosity",
    action='count',
    help="Want to know some curiosities?"
  )
  
  return parser.parse_args()
