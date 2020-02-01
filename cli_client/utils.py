from colorama import Fore, Style

# TODO: need global
_debug = False
_connected = False
version = 'Command Line Interface (CLI) Client 0.1'


def draw_header():
    title = version
    if _debug:
        if _connected is True:
            title += ' (connected)'
        else:
            title += ' (not connected)'
        title += Fore.RED + ' (debug)' + Fore.RESET + Style.NORMAL
    print(Fore.GREEN + Style.BRIGHT + "Gutlic's Arena" + Fore.RESET + Style.NORMAL)
    print(title)
    print('===================================================')
    print('')


def clear_screen():
    print('\033[2J')


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
