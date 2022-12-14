import os
from random import randint
from typing import List
from termcolor import colored
from painless.messages import show_mega_banner, test_rol_message, play_message, god_bay
from painless.enums import ColorEnum, list_exit_order
from .display import draw_grid  


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


def get_mode_play(dimension: int):
    status = input("Do you want to play or test : ")

    if status == 'play':
        os.system('clear')
        start_game(dimension, 'play')

    elif status == 'test':
        os.system('clear')
        start_game(dimension, 'test')
    else:
        get_mode_play(dimension)


def run_game():
    show_mega_banner('sega game', color=ColorEnum.green.value)
    get_mode_play(get_map_size())


def get_permissin_action(player_posation: list, map_size: int) -> list:
    allow_move_list = List() 
    if player_posation[0] == 0 and player_posation[1] == 0:
        allow_move_list.append("bottom")
        allow_move_list.append("right")
    elif player_posation[0] == 0 and player_posation[1] != (map_size - 1):
        allow_move_list.append("bottom")
        allow_move_list.append("right")
        allow_move_list.append("top")
    elif player_posation[0] != (map_size - 1) and player_posation[1] == 0:
        allow_move_list.append("bottom")
        allow_move_list.append("left")
        allow_move_list.append("right")
    elif player_posation[0] == (map_size - 1) and player_posation[1] == (map_size - 1):
        allow_move_list.append("top")
        allow_move_list.append("left")
    elif player_posation[0] == (map_size - 1) and player_posation[1] == 0:
        allow_move_list.append("left")
        allow_move_list.append("bottom")
    elif player_posation[0] == 0 and player_posation[1] == (map_size - 1):
        allow_move_list.append("top")
        allow_move_list.append("right")
    elif player_posation[0] == (map_size - 1) and player_posation[1] != (map_size - 1):
        allow_move_list.append("top")
        allow_move_list.append("left")
        allow_move_list.append("bottom")
    elif player_posation[0] != (map_size - 1) and player_posation[1] == (map_size - 1):
        allow_move_list.append("top")
        allow_move_list.append("left")
        allow_move_list.append("right")
    else:
        allow_move_list.append("top")
        allow_move_list.append("left")
        allow_move_list.append("right")
        allow_move_list.append("bottom")
    return allow_move_list


def start_game(map_dimension: int, mode_status_check: bool):
    position_list = get_random_position(map_dimension)
    play_status = True
    dragon_status = False

    while play_status:
        dragon_status = set_show_dragon(position_list[0], position_list[1], dragon_status)
        draw_grid(map_dimension, position_list[0], position_list[1], dragon_status)
        allow_moves_list = get_permissin_action(position_list[0], map_dimension)

        if mode_status_check == 'test':
            test_rol_message(position_list[0], position_list[1], position_list[2], allow_moves_list)
        elif mode_status_check == 'play':
            play_message(position_list[0], allow_moves_list)
        else:
            pass

        move_order = input("> ")

        if move_order in allow_moves_list or list_exit_order:
            if move_order == 'right':
                out = [position_list[0][0] + 1, position_list[0][1]]
            elif move_order == 'left':
                out = [position_list[0][0] - 1, position_list[0][1]]
            elif move_order == 'top':
                out = [position_list[0][0], position_list[0][1] - 1]
            elif move_order == 'bottom':
                out = [position_list[0][0], position_list[0][1] + 1]
            elif move_order in list_exit_order:
                play_status = False
                god_bay()
                break
        # else:
        #     getInputError()
        #     out = [position_list[0][0], position_list[0][1]]
        # position_list[0] = out
        # victoryStatus = getContinueStatus(getVictoryStatus(position_list))
        # if victoryStatus:
        #     clearTerminal()
        # else:
        #     break