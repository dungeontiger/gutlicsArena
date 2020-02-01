"""Class to draw a menu and handle the user's choice."""
from colorama import Fore, Style
from cli_client.action import Action
from cli_client.built_in_cmd import BuiltInCmds
from cli_client.utils import draw_header, is_int, clear_screen


class Menu:
    def __init__(self, menu):
        self.menu = menu

    def draw(self):
        _error = ''
        while True:
            # clear the screen
            clear_screen()
            # draws the header
            draw_header()
            for i, m in enumerate(self.menu):
                do_print('{}. {}'.format(i + 1, m['label']))
            do_print('')
            do_print(_error)
            # get the output and see if its valid, if valid return the action
            do_print(Fore.RED + '> ' + Fore.RESET + Style.NORMAL, end='')      # don't want a new line before the input
            cmd = get_input()
            # check first for a built in command, then check if one of the numbered options
            action = get_built_in_action(cmd)
            if action != Action.UNKNOWN:
                return action
            elif is_int(cmd) and 1 <= int(cmd) <= len(self.menu):
                # if there is a sub menu draw that, otherwise return the choice
                if 'menu' in  self.menu[int(cmd) - 1]:
                    submenu = Menu(self.menu[int(cmd) - 1]['menu'])
                    return submenu.draw()
                return self.menu[int(cmd) - 1]['id']
            # return error action and notice
            _error = Fore.RED + 'Invalid command or option.' + Fore.RESET + Style.NORMAL


def get_built_in_action(cmd):
    if cmd in BuiltInCmds.cmds:
        return BuiltInCmds.cmds[cmd]
    return Action.UNKNOWN


def get_input():
    """This function can be mocked out during testing."""
    return input()


def do_print(t, end='\n'):
    """This function can be mocked out during testing."""
    print(t, end)


"""
Menus are defined as a JSON array of menu items.
Each item has a label and an id and an optional menu.
If an item is selected and no sub menu is present, the id is returned
If a submenu is present for this id, the sub menu is rendered
[
    {
        "id": MenuItem.ITEM1,
        "label": "Item 1",
        "menu": [
            "id": MenuItem.SUBITEM1,
            "label": "Sub Item 1",
        ]
    }
]
"""