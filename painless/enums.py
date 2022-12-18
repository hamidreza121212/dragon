# from collections import namedtuple
from enum import Enum
from dataclasses import dataclass
from typing import NamedTuple
from decouple import config


class DatabaseConfig(Enum):
    Dialect = config('DB_DIALECT')
    Username = config('DB_USERNAME')
    Password = config('DB_PASSWORD')
    Host = config('DB_HOST')
    Port = config('DB_PORT')
    Database = config('DB_NAME')

list_exit_order: list = ["Q", "EXIT", "END", "QUIT"]

class ExistOrderEnum(Enum):
    Q = 'Q'
    EXIT = 'EXIT'
    END = 'END'
    QUIT = 'QUIT'


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
