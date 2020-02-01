from unittest import TestCase
from unittest.mock import patch
from cli_client.menu import Menu
from cli_client.menu_item import MenuItem
from cli_client_tests.input_side_effects import set_input, get_input
from cli_client_tests.print_side_effects import capture_print, lines
"""Mocking input to simulate user data.  Also mocking print so that I can capture output and verify it."""


class TestMenu(TestCase):
    @patch('cli_client.menu.get_input')
    def test_draw_simple_menu(self, mock_input):
        mock_input.side_effect = get_input
        items = [{"id": MenuItem.NEW_GAME, "label": "New Game"}, {"id": MenuItem.EXIT, "label": "Exit"}]
        menu = Menu(items)
        set_input([2])
        self.assertEqual(MenuItem.EXIT, menu.draw())

    @patch('cli_client.menu.do_print')
    @patch('cli_client.menu.get_input')
    def test_draw_menu_output(self, mock_input, mock_print):
        mock_input.side_effect = get_input
        mock_print.side_effect = capture_print
        set_input([2])
        items = [{"id": MenuItem.NEW_GAME, "label": "New Game"}, {"id": MenuItem.EXIT, "label": "Exit"}]
        menu = Menu(items)
        self.assertEqual(MenuItem.EXIT, menu.draw())
        self.assertEqual(5, len(lines))
