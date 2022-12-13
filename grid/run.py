from typing import Tuple
import os


def status(message: str):
    return message


def create_grid(grid: int, person_location: Tuple, door_location: Tuple, dragon_location: Tuple):
    matrix = []
    os.system('cls||clear')

    print(status('good move'))

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
                elif i == dragon_location[0] and j == dragon_location[1]:
                    a.append("\u2FF3")
                else:
                    a.append("\u4DC0")
            matrix.append(a)

    for i in range(grid):
        for j in range(grid):
            print(matrix[i][j], end=" ")
        print()
