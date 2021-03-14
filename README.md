# PlanetInfo

### Planets / moons information display
This is a simple program made in python3 to consult information about a planet or moon is in our solar system.

## How to install:
- Clone this repository: ```git https://github.com/Dantalion-dev/PlanetInfo.git```

- Install python3 
  - Linux
    - ```apt-get install python3```
    - ```chmod +x *```
    - ```python -m pip install -r requirements.txt```
    - Finished!

  - Windows
    - [Python 3, download and install](https://www.python.org/downloads/)
    - ```python3 -m pip install -r requirements.txt```
    - Finished!


## How to use:
```python
#using
python3 main.py [-h] [-c] [-f FILE] [-p PLANET_NAME]

examples:

# search for planet earth + curiosity + save the exit in a file
python3 main.py -c -p earth -f file.txt

# search for planet earth + save the output in a file
python3 main.py -p earth -f file.txt

# search only for planet earth
python3 main.py -p earth

# brings a random curiosity
python3 main.py -c

```
## License
This project is under the [MIT License](LICENSE).
