from typing import Tuple
from grid.run import create_grid


def activity(new_location: Tuple, dragon_location: Tuple, door: Tuple, grid_siz: int):
    def move():
        create_grid(grid_siz, new_location, door, dragon_location)

    move()
