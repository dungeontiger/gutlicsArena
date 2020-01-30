from .action import Action


class BuiltInCmds:
    cmds = { 'D': Action.DEBUG,
             'd': Action.DEBUG,
             'debug': Action.DEBUG,
             'Debug': Action.DEBUG,
             'DEBUG': Action.DEBUG,
             'x': Action.EXIT,
             'X': Action.EXIT,
             'q': Action.EXIT,
             'Q': Action.EXIT,
             '?': Action.HELP,
             'h': Action.HELP,
             'H': Action.HELP}
