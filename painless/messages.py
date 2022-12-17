import os
from typing import List
from termcolor import colored
from painless.enums import ColorEnum
from pyfiglet import Figlet


def test_rol_message(person_location: list, dragon_location: list, door_location: list):
    print(f"\n-> You're currently in location {person_location}.")
    print(f"-> Dragon in location {dragon_location}.")
    print(f"-> Door in location {door_location}.")
    print("-> Enter['QUIT','EXIT','END','Q'] to quit.")


def play_rol_message(person_location: list):
    print(f"\n-> You're currently in location {person_location}.")
    print("-> Enter['QUIT','EXIT','END','Q'] to quit.")



def show_mega_banner(text: str, color: str):
    os.system('clear')
    font = Figlet(font='banner3-D')
    print(colored(font.renderText(text), color))



def get_near_message(player_location: List, dragon_location: List):

    dis = 0
    for i in range(len(player_location)):
        dis += abs(player_location[i] - dragon_location[i])
    
    near_message = "\t ** Be Careful ** \n \t ** Dragon is near you **" if dis <= 3 else "\n"

    print(colored(near_message, str(ColorEnum.yellow.value)))


def god_bay_message():
    print(colored('\t\t **Bay** \n\t **Have a Nice Day**', str(ColorEnum.green.value)))


def get_error():
    print(colored('\t Invalid input Please enter the correct input : \n', str(ColorEnum.red.value)))
    input(' To Continue please press enter ...')

