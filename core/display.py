from typing import List
from painless.messages import get_near_message
from painless.enums import ColorEnum
from termcolor import colored


def grid(
        map_dimension: int,
        player_location: List[int],
        dragon_location: List[int],
        dragon_status: bool) -> None:
    get_near_message(player_location, dragon_location)

    for col in range(map_dimension):
        for row in range(map_dimension):
            if row == player_location[0] and col == player_location[1]:
                symbol = "\u32E1"
                color = ColorEnum.green.value
            elif row == dragon_location[0] and col == dragon_location[1] and dragon_status:
                symbol = "\u2FF4"
                color = ColorEnum.red.value
            else:
                symbol = "\u4DC0"
                color = ColorEnum.white.value
            print(colored("%%-%ds" % 2 % symbol, color))
