"""
Handles all the menu clicks in the client and returns what it should do next.
Three things need to be passed: menu id, item and state.
Menu id is used to determine which function to process the request.  Item is which choice the user made.
State is changed to indicate the user's choice as well as used to create specific UI.
In all cases a JSON object with menu and state is returned.
"""
import json
import random

strings = json.load(open('rest_server/resources/strings.json'))


def process_menu(menu_id, item, state):
    """Top level public method"""
    response = {'state': state}
    return handler_functions[menu_id](item, response)


def new_game(item, response):
    # check the state to see if a character has been started yet
    if 'character' not in response['state']:
        response['state']['character'] = {}

    if item == '':
        # just draw the main new game menu
        response['menu'] = json.load((open('rest_server/resources/new_game.json')))
    elif item == 'choose_name':
        response['menu'] = json.load((open('rest_server/resources/choose_name.json')))
    elif item == 'choose_sex':
        response['menu'] = json.load((open('rest_server/resources/choose_sex.json')))
    apply_state_to_menu(response['menu'], response['state'])
    return response


def choose_name(item, response):
    if item == 'generate_name':
        # for now just pick from a list
        names = list(open('rest_server/resources/names.txt'))
        # pick 5 random names
        menu = { 'id': 'pick_generated_name',
                 'title': ['Choose a Generated Name'], 'items':[
                {
                    'id': 'generate_name',
                    'label': 'Generate Other Names'
                },
                {
                    'id': 'back',
                    'label': 'Back'
                }
        ]}
        for _ in range(5):
            name = random.choice(names).rstrip('\n')
            menu['items'].insert(0, { 'id': name, 'label': name})
            response['menu'] = menu
        return response
    elif item == 'back':
        return new_game('', response)
    else:
        # they picked a name, write it into the state
        response['state']['character']['name'] = item
        return new_game('', response)


def choose_sex(item, response):
    if item != 'back':
        # we need to set the state to the sex that was chosen, then go back to the top level menu
        response['state']['character']['sex'] = item
    return new_game('', response)


def apply_state_to_menu(menu, state):
    """Menu labels will be modified based on values set in the state."""
    if menu['id'] == 'new_game':
        character = state['character']
        # top level menu
        if 'sex' in character:
            get_item(menu, 'choose_sex')['label'] = 'Choose Sex ({})'.format(strings[character['sex']])
        if 'name' in character:
            get_item(menu, 'choose_name')['label'] = 'Choose Name ({})'.format(character['name'])


def get_item(menu, item):
    """Returns the menu item with the id of item"""
    for i in menu['items']:
        if i['id'] == item:
            return i


# map of menu id to function which handles that menu
handler_functions = {
    "new_game": new_game,
    "choose_name": choose_name,
    "choose_sex": choose_sex,
    "pick_generated_name": choose_name
}
