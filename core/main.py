import os
from random import randint
from typing import List
from termcolor import colored
from painless.messages import show_mega_banner
from painless.enums import ColorEnum  
from .display import grid  


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
    status = input("Do you want to play again : ")
    if status == 'play':
        os.system('clear')
        start_game(dimension)
        print('asdkjh')
    else:
        get_mode_play(dimension)


def run_game():
    show_mega_banner('sega game', color=ColorEnum.green.value)
    get_mode_play(get_map_size())



def start_game(map_dimension: int, tset_status: bool):
    position_list = get_random_position(map_dimension)
    play_status = True
    dragon_status = False
    while play_status:
        dragon_status = set_show_dragon(position_list[0], position_list[1], dragon_status)
        grid(map_dimension, position_list[0], position_list[1], dragon_status)
        possible_moves = getPossibleMoves(position_list[0], map_dimension)
        if tset_status:
            setTestMessage(position_list[0], position_list[1],
                           position_list[2], possible_moves)
        else:
            setPlayMessage(position_list[0], possible_moves)
        move_order = input("> ")
        if move_order in possible_moves or move_order in list_exit_order:
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
                getByeMessage()
                break
        else:
            getInputError()
            out = [position_list[0][0], position_list[0][1]]
        position_list[0] = out
        victoryStatus = getContinueStatus(getVictoryStatus(position_list))
        if victoryStatus:
            clearTerminal()
        else:
            break