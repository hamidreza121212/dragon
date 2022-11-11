from typing import Tuple
from grid.run import create_grid


def activity(new_location: Tuple, dragon_location: Tuple, door: Tuple, grid_siz: int):

    def move():

        if new_location == door:
            create_grid(grid_siz, new_location, door)

        if new_location == dragon_location:
            create_grid(grid_siz, new_location, door)

        else:
            create_grid(grid_siz, new_location, door)

    move()
