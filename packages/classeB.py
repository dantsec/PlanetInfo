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
  
  args = parser.parse_args()

  return args 

def request(url):
  import urllib3
  import json
  urllib3.disable_warnings()
  http = urllib3.PoolManager()
  r = http.request("GET", url)
  code = json.loads(r.data.decode('utf-8'))
  
  return code
