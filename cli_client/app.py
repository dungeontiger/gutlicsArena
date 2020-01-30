import requests
from colorama import init, Fore, Back, Style
from cli_client.built_in_cmd import BuiltInCmds
from cli_client.action import Action


class App:
    server_url = "http://localhost:5000"
    main_help = \
        ['Gutlic\'s Arena is a fantasy adventure game. It mixes old school text based adventure games with modern rules and technology.',
         'You are currently using the command line interface (CLI). To be able to play the game you also need to be connected to a server.'
         'The main interface to the CLI is a menu system.  Each menu will present you with a list of options.',
         'Press the number of the menu option you want and ENTER.  Some commands are always available and are not displayed in the menu.',
         'These commands are all activated via a single letter or word at any menu:',
         '\t?, h, H: context sensitive help',
         '\tx, X, q, Q: exit the game (your game progress will be saved)',
         '\ti: see your current inventory',
         '\tc: see your current character']
    version = 'Command Line Interface (CLI) Client 0.1'
    _debug = False
    connected = False

    def __init__(self):
        # initialize the colorama library
        init()

    def run(self):
        action = Action.MAIN_MENU
        self.connect()
        # loop until the user exists the game
        while action is not Action.EXIT:
            if action is Action.MAIN_MENU:
                #
                # main menu
                #
                previous_action = action
                action = self.main_menu()
            elif action is Action.DEBUG:
                #
                # toggle the debug flag
                #
                self._debug = not self._debug
                action = previous_action
            elif action is Action.HELP:
                #
                # help
                #
                action = previous_action
                self.draw_help(self.main_help)
            elif action is Action.NEW_GAME:
                if self.connected is False:
                    self.connect()
                if self.connected is False:
                    self.draw_error('Not connected to the server.  Cannot create a new game.')
                    action = previous_action
        # outside the loop and about to exit
        print('Exiting Gutlic\'s Arena')

    def main_menu(self):
        menu = [{'label': 'New game', 'action': Action.NEW_GAME},
                #{'label': 'Continue game', 'action': Action.CONTINUE_GAME},
                {'label': 'Help', 'action': Action.HELP},
                {'label': 'Exit', 'action': Action.EXIT}]
        return self.draw_menu(menu)

    def draw_header(self):
        title = self.version
        if self._debug:
            if self.connected is True:
                title += ' (connected)'
            else:
                title += ' (not connected)'
            title += Fore.RED + ' (debug)' + Fore.RESET + Style.NORMAL
        # clears the screen
        print('\033[2J')
        print(Fore.GREEN + Style.BRIGHT + "Gutlic's Arena" + Fore.RESET + Style.NORMAL)
        print(title)
        print('===================================================')
        print('')

    def draw_menu(self, menu):
        action = Action.UNKNOWN
        _error = ''
        while action is Action.UNKNOWN:
            self.draw_header()
            i = 0
            for m in menu:
                i += 1
                print('{}. {}'.format(i, m['label']))
            print('')
            print(_error)
            # get the output and see if its valid, if valid return the action
            cmd = input(Fore.RED + '> ' + Fore.RESET + Style.NORMAL)
            action = self.get_built_in_action(cmd)
            if action != Action.UNKNOWN:
                return action
            elif self.is_int(cmd) and 1 <= int(cmd) <= len(menu):
                return menu[int(cmd) - 1]['action']
            _error = Fore.RED + 'Invalid command or option.' + Fore.RESET + Style.NORMAL

    @staticmethod
    def get_built_in_action(cmd):
        if cmd in BuiltInCmds.cmds:
            return BuiltInCmds.cmds[cmd]
        return Action.UNKNOWN

    def connect(self):
        try:
            server = requests.get(self.server_url + '/ping')
            if server.status_code == 200:
                self.connected = True
            else:
                self.connected = False
        except Exception:
            self.connected = False

    @staticmethod
    def is_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def draw_help(self, help_text):
        self.draw_header()
        for t in help_text:
            print(t)
        print('')
        input('Press ENTER to continue...')
        return

    def draw_error(self, error_text):
        self.draw_header()
        print(Fore.RED + Style.BRIGHT + error_text + Fore.RESET + Style.NORMAL)
        print('')
        input('Press ENTER to continue...')
        return


# singleton application
app = App()
app.run()
