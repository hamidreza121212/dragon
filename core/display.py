from typing import List
from painless.messages import get_near_message
from painless.enums import ColorEnum
from termcolor import colored


def draw_grid(
        map_dimension: int,
        player_location: List[int],
        dragon_location: List[int],
        dragon_status: bool) -> None:

    get_near_message(player_location, dragon_location)

    for col in range(map_dimension):
        for row in range(map_dimension):
            if row == player_location[0] and col == player_location[1]:
                symbol = "P"
                color = ColorEnum.green.value
            elif row == dragon_location[0] and col == dragon_location[1] and dragon_status:
                symbol = "D"
                color = ColorEnum.red.value
            else:
                symbol = "*"
                color = ColorEnum.white.value
            print(colored("%%-%ds" % 2 % symbol, color), end="")
        print()
