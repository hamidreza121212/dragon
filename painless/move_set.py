def permissin_right(player_location: list, map_size: int) -> bool:
    return False if player_location[0] == map_size - 1 else True

def permissin_left(player_location: list) -> bool:
    return False if player_location[0] == 0 else True


def permissin_top(player_location: list) -> bool:
    return False if player_location[1] == 0 else True


def permissin_bottom(player_location: list, map_size: int) -> bool:
    return False if player_location[1] == map_size - 1 else True