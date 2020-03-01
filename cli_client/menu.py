"""Class to draw a menu and handle the user's choice."""
from colorama import Fore, Style
from cli_client.action import Action
from cli_client.built_in_cmd import BuiltInCmds
from cli_client.utils import is_int, clear_screen, do_print, get_input
from cli_client.debug import is_debug, is_connected


"""
This accepts a single level menu definition (for now)
{
    "menu": {
        "id": "id_of_this_menu",
        "title": "title is optional"
        "items": [
            {
                "id": "menu_item_id",
                "label": "display text for this menu item",
                "help:" "Help text for this menu item
            }
        ]
    }
}

When a menu selection is made, the client tells the server which menu and which item and recieves a new menu to display
"""


class Menu:
    def __init__(self, menu, header=None):
        self.menu = menu
        if header:
            self.header = header
        else:
            self.header = menu['title']

    """
    Draw the menu and wait for a valid choice to be made
    """
    def draw(self, msg=None):
        _error = ''
        while True:
            # clear the screen
            clear_screen()
            # draw the header
            self.draw_header(msg)
            for i, m in enumerate(self.menu['items']):
                do_print('{}. {}'.format(i + 1, m['label']))
            do_print('')
            do_print(_error)
            # get the output and see if its valid, if valid return the action
            cmd = get_input(Fore.RED + '> ' + Fore.RESET + Style.NORMAL)
            # check first for a built in command, then check if one of the numbered options
            action = get_built_in_action(cmd)
            if action != Action.UNKNOWN:
                return action
            elif is_int(cmd) and 1 <= int(cmd) <= len(self.menu['items']):
                return self.menu['items'][int(cmd) - 1]['id']
            # return error action and notice
            _error = Fore.RED + 'Invalid command or option.' + Fore.RESET + Style.NORMAL

    def draw_header(self, msg):
        """Draw the header that was passed to the menu."""
        for h in self.header:
            do_print(h)
        if msg:
            do_print(msg)
        if is_debug():
            if is_connected():
                c = 'connected'
            else:
                c = 'not connected'
            do_print(Fore.CYAN + 'DEBUG: ' + Fore.RESET + c)
        do_print('')


def get_built_in_action(cmd):
    if cmd in BuiltInCmds.cmds:
        return BuiltInCmds.cmds[cmd]
    return Action.UNKNOWN

