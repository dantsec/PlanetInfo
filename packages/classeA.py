class Astronomy():
  def __init__(self, args):
    self.args         = args
    self.planet       = args.planet

  def planet_info(self):
    url = f'https://api.le-systeme-solaire.net/rest/bodies/{self.planet}'
    return url

  @staticmethod
  def request(url):
    import urllib3
    import json
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    code = json.loads(r.data.decode('utf-8'))
  
    return code

  @staticmethod
  def filter(code):
    for key, value in code.items():
      if value == '':
        pass
      else:
        print(key, ':', value)
        print(" ") 
