import os
from typing import List
from .messages import get_near_message


def draw_grid(
        map_dimension: int,
        player_location: List[int, int],
        dragon_location: List[int, int],
        dragon_status: bool) -> None:
    matrix = []
    os.system('cls||clear')
    get_near_message(player_location, dragon_location)

    for i in range(map_dimension):
        a = []

        if person_location == door_location:
            for j in range(grid):
                a.append(colored("+", 'green'))
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