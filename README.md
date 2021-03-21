<h1 align="center">
  🌑 Planet Information Display
</h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Dantalion-dev/PlanetInfo">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Dantalion-dev/PlanetInfo">
  
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Dantalion-dev/PlanetInfo">

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
</p>

<p align="center">
  <a href="#%F0%9F%9A%80-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%F0%9F%92%BB
-project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%E2%99%9F%EF%B8%8F-installation">Installing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%E2%9C%A8-features">Features</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%F0%9F%8D%80-how-to-use">How to use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%F0%9F%94%A8-contributing">Contributing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#%F0%9F%93%9D-license">License</a>


  
</p>

## 🚀 Technologies 
This project was developed with the following technologies:

- Python

## 💻 Project
This is a project that I developed for my physics class, which basically consisted of you studying a planet and showing information about it, I went further, I added some somewhat different features, like asking for some curiosity about our solar system and saving the data in a file

## ✨ Features
- Code review
- Save data on file
- Random curiosity about the solar system (Fun)

## ♟️ Installation
- Clone this repository: ```git clone https://github.com/Dantalion-dev/PlanetInfo.git```

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

## 🍀 How to use
```python
#using
python3 main.py [-h HELP] [-c CURIOSITY] [-f FILE] [-p PLANET_NAME]

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

## 🔨 Contributing

How can I contribute to the project?

```sh
1. Create a fork from PlanetInfo repository.
2. git clone https://github.com/your/PlanetInfo.git
3. cd PlanetInfo/
4. Make your changes.
5. Commit and make a git push.
6. Open a pull request.
```

## 📝 license

This project is under the [MIT License](LICENSE).
