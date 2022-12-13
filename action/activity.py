import os
from random import randrange
from pyfiglet import Figlet
from termcolor import colored


def cls_terminal():
    os.system('clear')


def get_random_position(size: int):
    master_list = []
    while len(master_list) < 3:
        my_random = (randrange(0, size - 1), randrange(0, size - 1))
        if my_random not in master_list:
            master_list.append(my_random)
    return master_list


def show_mega_banner(text: str, color: str):
    cls_terminal()
    font = Figlet(font='banner3-D')
    print(colored(font.renderText(text), color))


def get_map_size():
    while True:
        try:
            size = int(input('please select map size in this game : '))
            break
        except ValueError as e:
            print(colored('\n**Please print valid integer**\n', 'red'))
    print(f'your map size will be {size} * {size}')

    return size
