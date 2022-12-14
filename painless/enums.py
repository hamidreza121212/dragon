# from collections import namedtuple
from enum import Enum
from dataclasses import dataclass
from typing import NamedTuple


class MapDimensionEnum(Enum):
    x: int
    y: int


class ColorEnum(Enum):
    white = 'white'
    red = 'red'
    green = 'green'
    yellow = 'yellow'


@dataclass
class ColorDataClass:
    white: str = 'white'
    blue: str = 'blue'
    red: str = 'red'


# ColorTuple = namedtuple('ColorTuple', ['name', 'hex'])
#
# white_color = ColorTuple('white', '#99ff14')
# blue_color = ColorTuple('blue', '#555323')
# red_color = ColorTuple('red', '#004499')


class ColorTuple(NamedTuple):
    name: str
    hex: str


white_color = ColorTuple('white', '#99ff14')
blue_color = ColorTuple('blue', '#555323')
red_color = ColorTuple('red', '#004499')
