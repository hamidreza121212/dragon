from random import randrange
from grid.run import create_grid, mega_banner

left_right_val: int = 0
up_down_val: int = 0

action_list = ['left', 'right', 'up', 'down', 'end']

mega_banner('SEGA \n GAME', 'red')


def get_random_position(size: int):
    master_list = []
    while len(master_list) < 3:
        my_random = (randrange(0, size - 1), randrange(0, size - 1))
        if my_random not in master_list:
            master_list.append(my_random)
    return master_list


def grid_size():
    while True:
        try:
            size = int(input('please select grid size : '))
            break
        except ValueError as e:
            print(f'{e}')
    return size


