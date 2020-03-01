import requests
import json
from pathlib import Path
from colorama import init, Fore, Style
from cli_client.menu import Menu
from cli_client.utils import clear_screen
from cli_client.utils import headers
from cli_client.msg_box import show_msg_box


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
    # TODO: need global debug
    _debug = False
    connected = False

    def __init__(self):
        # initialize the colorama library
        init()
        # read the game state is it exists and load it
        # TODO: deal with path Windows / Mac
        main_menu_json = json.load(open('cli_client/resources/main_menu.json', 'r'))
        p = Path('state.json')
        if p.exists():
            self.state = json.load(open(p, 'r'))
            # since there is state, add a continue menu option
            main_menu_json['items'].insert(1, {'id': 'continue_game', 'label': 'Continue Game'})
        else:
            self.state = {}
        self.main_menu = Menu(main_menu_json, headers)

    def run(self):
        choice = None
        # loop until the user exists the game
        while choice != "exit":
            # clear the screen each time we want to draw the main menu
            msg = ''
            self.connect()
            if not self.connected:
                msg = Fore.RED + Style.BRIGHT + 'Not Connected to Server' + Fore.RESET+ Style.NORMAL
            choice = self.main_menu.draw(msg)
            if choice == 'new_game':
                # delete any state
                # if not connected try again
                if not self.connected:
                    self.connect()
                self.new_game_handler()
            elif choice == 'continue_game':
                # use the existing state
                # if not connected try again
                if not self.connected:
                    self.connect()
                self.continue_game_handler()
            elif choice == 'help':
                self.draw_help(self.main_help)

        # outside the loop and about to exit
        clear_screen()
        print(Fore.GREEN + Style.BRIGHT +'Gutlic\'s Arena is over.' + Fore.RESET + Style.NORMAL)

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
        # draw_header()
        for t in help_text:
            print(t)
        print('')
        input('Press ENTER to continue...')
        return

    def new_game_handler(self):
        # don't try to create a new game if the server is not running
        if not self.connected:
            show_msg_box('Not connected to the server.  Either start the server or try again later.')
            return
        # tell the server we want to start a new game and erase any state because this is new
        # TODO: add a Y/N verification dialog
        self.state = {}
        # new is the same as continue except we wipe out the state first
        self.continue_game_handler()

    def continue_game_handler(self):
        # don't try to continue if the server is not running
        if not self.connected:
            show_msg_box('Not connected to the server.  Either start the server or try again later.')
            return
        choice = ''
        menu_id = ''
        while choice != 'go_to_main':
            request_data = {'state': self.state}
            if choice != '':
                request_data['menu_id'] = menu_id
                request_data['item'] = choice
            response = requests.post(self.server_url + '/new_game', json=request_data).json()
            # the response will contain a menu - draw it
            menu = Menu(response['menu'])
            menu_id = response['menu']['id']
            # get the state and save it
            self.state = response['state']
            self.save_state()
            choice = menu.draw()

    def save_state(self):
        # write this state to disk so the game is 'always saved'
        # TODO: save this in a different location
        json.dump(self.state, open('state.json', 'w'))


# singleton application
app = App()
app.run()
