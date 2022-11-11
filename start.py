import values
from action.move import activity
from grid.run import create_grid

create_grid(values.grid_siz, values.my_location, values.door, values.dragon_location)


def update_location(x: int, y: int):
    return values.my_location[0] + x, values.my_location[1] + y


while True:

    action = input("please select actions : ")

    if action not in values.action_list:
        print('your select not true')

    if action == 'left':
        if not values.left_right_val + values.my_location[1] == 0:
            values.left_right_val = values.left_right_val - 1

        activity(update_location(values.up_down_val, values.left_right_val), values.dragon_location, values.door,
                 values.grid_siz)

    if action == 'right':
        if not values.left_right_val + values.my_location[1] >= values.grid_siz - 1:
            values.left_right_val = values.left_right_val + 1

        activity(update_location(values.up_down_val, values.left_right_val), values.dragon_location, values.door,
                 values.grid_siz)

    if action == 'up':
        if not values.up_down_val + values.my_location[0] <= 0:
            values.up_down_val = values.up_down_val - 1

        activity(update_location(values.up_down_val, values.left_right_val), values.dragon_location, values.door,
                 values.grid_siz)

    if action == 'down':
        if not values.up_down_val + values.my_location[0] >= values.grid_siz - 1:
            values.up_down_val = values.up_down_val + 1

        activity(update_location(values.up_down_val, values.left_right_val), values.dragon_location, values.door,
                 values.grid_siz)

    if action == 'end':
        print('tank you for good play')
        break
