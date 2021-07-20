class Astronomy():
  def __init__(self, args):
    self.args = args


  def write_file(self, data) -> None:
    """Write the out of the program in a file
    """
    with open(self.args.file, "w+") as _file:
      _file.write(data)
      _file.close()


  def request(self) -> str:
    """Make the request to api
    """
    import urllib3
    import json
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    r = http.request("GET", f'https://api.le-systeme-solaire.net/rest/bodies/{self.args.planet}')
    code = json.loads(r.data.decode('utf-8'))
    return code


  @staticmethod
  def _filter(code) -> list:
    """Filter the output of the program
    """
    data = []
    for key, value in code.items():
      if value == '':
        pass
      else:
        print('[*]', key, ':', value)
        print(" ")
        data.append(f"{key} : {value}")
    return data 


  @staticmethod
  def curiosity() -> str:
    """Return a random curiosity about our solar system
    """
    from random import choice
    facts = [
      "Only on Earth is it possible to see a total solar eclipse.",
      "The coldest planet in the Solar System is Uranus, where temperatures reach -224 ºC.",
      "There are space volcanoes that don't spew lava, but water. In some moons, for example, where the driving force is ice, water comes from the craters.",
      "Pluto has a smaller diameter than Brazil",
      "There are Mars rocks on Earth",
      "Even very small bodies can have moons",
      "We are nowhere near the center of the galaxy",
      "The solar system doesn't end on Pluto",
      "The strongest winds in the Solar System happen on Neptune, reaching up to 2,100 km / h!"
      ] 

    return f"[+] {choice(facts)}.\n"
