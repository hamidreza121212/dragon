import os
from typing import List
from typ
from .messages import get_near_message
from painless.enums import ColorEnum


def grid(
        map_dimension: int,
        player_location: List[int],
        dragon_location: List[int],
        dragon_status: bool) -> None:
    matrix = []
    get_near_message(player_location, dragon_location)

    for col in range(map_dimension):
        for row in range(map_dimension):
            if row == person_location[0] and col == person_location[1]:
                symbol = "\u32E1"
                color = ColorEnum.red.value
            elif row == door_location[0] and col == door_location[1]:
                a.append("\u2FF4")
            else:





        else:
            for j in range(grid):

                elif i == door_location[0] and j == door_location[1]:
                    a.append("\u2FF4")
                else:
                    a.append("\u4DC0")
            matrix.append(a)

    for i in range(grid):
        for j in range(grid):
            print(matrix[i][j], end=" ")
        print()