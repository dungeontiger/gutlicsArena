import requests
from colorama import init, Fore, Style
from cli_client.action import Action
from cli_client.menu import Menu
from cli_client.utils import draw_header, clear_screen


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
    # TODO: need global debug
    _debug = False
    connected = False
    new_game = None

    def __init__(self):
        # initialize the colorama library
        init()

    def run(self):
        action = Action.MAIN_MENU
        self.connect()
        # loop until the user exists the game
        while action is not Action.EXIT:
            # clear the screen each time we want to draw the main menu
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
                else:
                    # action = self.new_game_handler()
                    action = self.new_game()
        # outside the loop and about to exit
        clear_screen()
        print(Fore.GREEN + Style.BRIGHT +'Gutlic\'s Arena is over.' + Fore.RESET + Style.NORMAL)

    def main_menu(self):
        menu = Menu([{'label': 'New game', 'action': Action.NEW_GAME},
                     # TODO: Continue if there is a local JSON file with the details...or on the server?
                     # {'label': 'Continue game', 'action': Action.CONTINUE_GAME},
                     {'label': 'Help', 'action': Action.HELP},
                     {'label': 'Exit', 'action': Action.EXIT}])
        return menu.draw()

    def connect(self):
        try:
            server = requests.get(self.server_url + '/ping')
            if server.status_code == 200:
                self.connected = True
            else:
                self.connected = False
        # TODO: I'm annoying with this generic exception but nothing specific seemed to work
        except Exception as e:
            self.connected = False

    def draw_help(self, help_text):
        clear_screen()
        draw_header()
        for t in help_text:
            print(t)
        print('')
        input('Press ENTER to continue...')
        return

    def draw_error(self, error_text):
        clear_screen()
        draw_header()
        print(Fore.RED + Style.BRIGHT + error_text + Fore.RESET + Style.NORMAL)
        print('')
        input('Press ENTER to continue...')
        return

    def new_game_handler(self):
        if self.new_game is None:
            # get a basic game from the server
            response = requests.get(self.server_url + '/new_game')
            if self._debug:
                print(response.json())
            self.new_game = response.json()
        # now we want to build a menu based on what is missing from the character
        menu = []
        # list of attributes, name, race, etc...
        for attrib in self.new_game:
            menu.append({'label':attrib['empty_label'], 'action': None})
        menu.append({'label': 'Back', 'action': None})
        self.draw_menu(menu)
        return Action.EXIT


# singleton application
app = App()
app.run()
