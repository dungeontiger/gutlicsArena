from enum import Enum, auto


class Action(Enum):
    UNKNOWN = auto()
    ERROR = auto()
    EXIT = auto()
    CONTINUE = auto()
    DEBUG = auto()
    HELP = auto()
    MAIN_MENU = auto()
    NEW_GAME = auto()
    CONTINUE_GAME = auto()

