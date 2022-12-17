import os
from painless.game_rnmd import get_random_position
from typing import List
from painless.messages import *
from painless.enums import ColorEnum, list_exit_order
from .display import draw_grid  
from painless.move_set import *


def get_map_size():
    while True:
        try:
            size = int(input('Please choice map size : '))
            break
        except ValueError as e:
            print('\n**Please print valid integer**\n')
    print(f'Your map size will be {size} * {size}')

    return size


def set_show_dragon(player_location: List, dragon_location: List, dragon_status: bool) -> bool:
    dragon_status = False 
    if dragon_location:
        dragon_status = True
    else:
        if abs(player_location[0] - dragon_location[0]) <= 1 and abs(player_location[1] - dragon_location[1]) <= 1:
            dragon_status = True
        else:
            dragon_status = False
    return dragon_status


def get_victory_status(position_list: list) -> int:
    v_status = 0
    if position_list[0] == position_list[1]:
        v_status = 1
    elif position_list[0] == position_list[2]:
        v_status = 2
    return v_status


def get_continue_status(victory_status: int) -> bool:
    continue_status = True
    if victory_status == 1:
        print("***I'm sorry you lost!!***")
        while True:
            repeat_request = input("\nDo you want to play again?[Yes/No]")
            if repeat_request == "Yes":
                os.system('clear')
                run_game()
                break
            elif repeat_request == "No":
                continue_status = False
                get_near_message()
                break
            else:
                get_error()
    elif victory_status == 2:
        print("***Congratulations, you won!!***")
        repeat_request = input("\nDo you want to play again?[Yes/No]")
        if repeat_request == "Yes":
            os.system('clear')
            run_game()
        elif repeat_request == "No":
            continue_status = False
            god_bay_message()
        else:
            get_error()
    return continue_status


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


def start_game(map_dimension: int, mode_status_check: bool):
    position_list = get_random_position(map_dimension)
    play_status = True
    dragon_status = False

    while play_status:
        dragon_status = set_show_dragon(position_list[0], position_list[1], dragon_status)
        draw_grid(map_dimension, position_list[0], position_list[1], dragon_status)

        if mode_status_check == 'test':
            test_rol_message(position_list[0], position_list[1], position_list[2])
        elif mode_status_check == 'play':
            play_rol_message(position_list[0])
        else:
            pass

        move_order = input("> ")

        if move_order or list_exit_order:
            if move_order == 'r' and permissin_right(position_list[0], map_dimension):
                out = [position_list[0][0] + 1, position_list[0][1]]
            elif move_order == 'l' and permissin_left(position_list[0]):
                out = [position_list[0][0] - 1, position_list[0][1]]
            elif move_order == 't' and permissin_top(position_list[0]):
                out = [position_list[0][0], position_list[0][1] - 1]
            elif move_order == 'b' and permissin_bottom(position_list[0], map_dimension):
                out = [position_list[0][0], position_list[0][1] + 1]
            elif move_order in list_exit_order:
                play_status = False
                god_bay_message()
                break
        else:
            get_error()
            out = [position_list[0][0], position_list[0][1]]
        position_list[0] = out
        victoryStatus = get_continue_status(get_victory_status(position_list))
        if victoryStatus:
            os.system('clear')
        else:
            break