from colorama import Fore, Style

headers = [
    Fore.GREEN + Style.BRIGHT + 'Gutlic\'s Arena' + Fore.RESET + Style.NORMAL,
    'Command Line Interface (CLI) Client 0.1',
    '========================================================='
]


def get_input(prompt):
    """This function can be mocked out during testing."""
    return input(prompt)


def do_print(t):
    """This function can be mocked out during testing."""
    print(t)


def clear_screen():
    print('\033[2J')


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
