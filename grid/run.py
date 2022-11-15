from typing import Tuple
import os
from pyfiglet import Figlet
from termcolor import colored


def cls_terminal():
    os.system('clear')


def mega_banner(text: str, color: str):
    cls_terminal()
    font = Figlet(font='banner3-D')
    print(colored(font.renderText(text), color))


def create_grid(grid: int, person_location: Tuple, door_location: Tuple, dragon_location: Tuple):
    matrix = []
    cls_terminal()

    print(person_location)
    print(door_location)
    print(dragon_location)

    for i in range(grid):
        a = []

        if person_location == door_location:
            for j in range(grid):
                a.append("+")
            matrix.append(a)

        if person_location == dragon_location:
            for j in range(grid):
                a.append("-")
            matrix.append(a)

        else:
            for j in range(grid):
                if i == person_location[0] and j == person_location[1]:
                    a.append("\u32E1")
                elif i == door_location[0] and j == door_location[1]:
                    a.append("\u2FF4")
                else:
                    a.append("\u4DC0")
            matrix.append(a)

    for i in range(grid):
        for j in range(grid):
            print(matrix[i][j], end=" ")
        print()
