from random import randrange

left_right_val: int = 0
up_down_val: int = 0

action_list = ['left', 'right', 'up', 'down', 'end']

grid_siz = int(input("please select grid : "))

grid_rend = grid_siz - 1

my_location = (randrange(0, grid_rend), randrange(0, grid_rend))

dragon_location = (1, 1)

door = (randrange(0, grid_rend), randrange(0, grid_rend))
