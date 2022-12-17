from random import randint
from typing import List

def get_random_position(size: int) -> List[List[int]]:
    random_list: List[List[int]] = list()
    while len(random_list) < 3:
        rdm: List = list()
        rdm.append(randint(1, size - 1))
        rdm.append(randint(1, size - 1))
        if rdm not in random_list:
            random_list.append(rdm)
    return random_list