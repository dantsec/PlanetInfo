def curiosity():
  from random import choice

  facts =[
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

  text = f"[+] {choice(facts)}."
  return text
  