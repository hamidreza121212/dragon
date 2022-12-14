import os
from random import randint
from typing import List
from pyfiglet import Figlet
from termcolor import colored
from .messages import get_near_message

def cls_terminal():
    os.system('clear')


def get_random_position(size: int) -> List[List[int]]:
    random_list: List[List[int]] = list()
    while len(random_list) < 3:
        rdm: List = list()
        rdm.append(randint(1, size - 1))
        rdm.append(randint(1, size - 1))
        if rdm not in random_list:
            random_list.append(rdm)
    return random_list


def get_map_size():
    while True:
        try:
            size = int(input('Please choice map size : '))
            break
        except ValueError as e:
            print(colored('\n**Please print valid integer**\n', 'red'))
    print(f'Your map size will be {size} * {size}')

    return size


def get_mode_play(dimension: int):
    status = input("Do you want to play again : ")
    if status == 'play':
        cls_terminal()
        start_game(dimension)
    else:
        get_mode_play(dimension)


def set_show_dragon(player_location: List, dragon_location: List, dragon_status: bool) -> bool:
    dragon_status = False
    # if dragon_location
    pass


def start_play(map_dimension: int, status: bool):
    position_list = get_random_position(map_dimension)
    play_status = True
    dragon_status = False

    while play_status:
        dragon_status = set_show_dragon(position_list[0], position_list[1], dragon_status)
