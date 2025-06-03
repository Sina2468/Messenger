from os import system
from sys import platform


def Cleaner():
    if platform == "win32":
        system("cls")
    else:
        system("clean")


Cleaner()
