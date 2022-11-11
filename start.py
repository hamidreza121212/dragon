from typing import Tuple
from grid.run import create_grid
from random import randrange

left_right_val = 0
up_down_val = 0

action_list = ['left', 'right', 'up', 'down', 'end']

grid_siz = int(input("please select grid : "))

grid_rend = grid_siz - 1

my_location = (randrange(0, grid_rend), randrange(0, grid_rend))

dragon_location = (4, 6)

door = (randrange(0, grid_rend), randrange(0, grid_rend))

print(create_grid('game', grid_siz, my_location, door))


def activity(new_location: Tuple):

    def move():

        if new_location == door:
            create_grid('won', grid_siz, new_location, door)

        if new_location == dragon_location:
            create_grid('end', grid_siz, new_location, door)

        else:
            create_grid('game', grid_siz, new_location, door)

    move()


while True:

    action = input("please select actions : ")

    def update_location(x: int, y: int):
        return my_location[0] + x, my_location[1] + y


    if action not in action_list:
        print('your select not true')

    if action == 'left':
        if not left_right_val + my_location[1] == 0:
            left_right_val = left_right_val - 1

        activity(update_location(up_down_val, left_right_val))

    if action == 'right':
        if not left_right_val + my_location[1] >= grid_siz - 1:
            left_right_val = left_right_val + 1

        activity(update_location(up_down_val, left_right_val))

    if action == 'up':
        if not up_down_val + my_location[0] <= 0:
            up_down_val = up_down_val - 1

        activity(update_location(up_down_val, left_right_val))

    if action == 'down':
        if not up_down_val + my_location[0] >= grid_siz - 1:
            up_down_val = up_down_val + 1

        activity(update_location(up_down_val, left_right_val))

    if action == 'end':
        print('tank you for good play')
        break
