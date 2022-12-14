import os
from typing import List
from termcolor import colored
from painless.enums import ColorEnum
from pyfiglet import Figlet


def show_mega_banner(text: str, color: str):
    os.system('clear')
    font = Figlet(font='banner3-D')
    print(colored(font.renderText(text), color))


def set_game_message(player_location: List[int], player_move: List[str]):  # type: ignore
    print(f"\n Your currently in location {player_location}")
    print(f"Your can move to {player_move}")
    print("Enter ['END' OR 'Q'] to quit")


def get_near_message(player_list: List, dragon_list: List):
    near_message = "\n \n \n"

    if (player_list[0] - dragon_list[0] <= 2) and (player_list[1] - dragon_list[1] <= 2):
        near_message = "\t ** Be Careful ** \n \t ** Dragon is near you **"

    print(colored(near_message, str(ColorEnum.yellow.value)))


def god_bay():
    print(colored('\t\t **Bay** \n\t **Have a Nice Day**', str(ColorEnum.green.value)))


def get_error():
    print(colored('\t Invalid input Please enter the correct input : \n', str(ColorEnum.red.value)))
    input(' To Continue please press enter ...')


