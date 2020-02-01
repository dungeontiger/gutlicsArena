"""Handles UI to create a character and a new game."""
from cli_client.menu import Menu


class NewGameHandler:
    def __init__(self, new_game):
        self.new_game = new_game

    def draw_menu(self, menu_portion, parent_menu):
        menu = Menu(menu_portion)
        choice = menu.draw()
