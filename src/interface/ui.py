import os
from rich import print


def banner() -> None:
	""" Return an ascii art """
	with open("src/interface/art.txt", "r") as file:
		return print(f"[red]{file.read()}[/]")


def clear() -> None:
	""" Clear your terminal """
	os.system(['clear', 'cls'][os.name == 'nt'])
