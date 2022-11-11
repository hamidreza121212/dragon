from typing import Tuple
import os


def create_grid(grid: int, person_location: Tuple, door_location: Tuple):
    matrix = []
    os.system('cls||clear')

    for i in range(grid):
        a = []

        if person_location == door_location:
            for j in range(grid):
                a.append("+")
            matrix.append(a)

        else:
            for j in range(grid):
                if i == person_location[0] and j == person_location[1]:
                    a.append("\u32E1")
                if i == door_location[0] and j == door_location[1]:
                    a.append("\u2FF4")
                else:
                    a.append("\u4DC0")
            matrix.append(a)

    for i in range(grid):
        for j in range(grid):
            print(matrix[i][j], end=" ")
        print()
