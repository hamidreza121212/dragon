import values
# from action.move import activity
from grid.run import create_grid, mega_banner


# create_grid(values.grid_siz, values.my_location, values.door, values.dragon_location)


# def update_location(x: int, y: int):
#     return values.my_location[0] + x, values.my_location[1] + y


def game():
    number_of_size = values.grid_size()
    point_list = values.get_random_position(number_of_size)

    while True:

        action = input("please select actions : ")

        if action == 'left':
            output = point_list[0][0] - 1, point_list[0][0]

            # create_grid(number_of_size, output, point_list[1], point_list[2])
            print(output)

        elif action == 'right':
            output = point_list[0][0] + 1, point_list[0][0]

            # create_grid(number_of_size, output, point_list[1], point_list[2])
        elif action == 'u':
            output = point_list[0][0], point_list[0][0] - 1
            print(output)

            # create_grid(number_of_size, output, point_list[1], point_list[2])

        elif action == 'down':
            output = point_list[0][0], point_list[0][0] + 1

            # create_grid(number_of_size, output, point_list[1], point_list[2])

        elif action == 'end':
            print('tank you for good play')
            break

        else:
            print('your select not true')


game()


