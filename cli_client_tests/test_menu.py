from unittest import TestCase
from unittest.mock import patch
from cli_client.menu import Menu
from cli_client_tests.input_side_effects import set_input, get_input
from cli_client_tests.print_side_effects import capture_print, lines
from cli_client.debug import set_debug, is_debug
from cli_client.utils import get_header
"""Mocking input to simulate user data.  Also mocking print so that I can capture output and verify it."""


class TestMenu(TestCase):

    @patch('cli_client.menu.get_input')
    def test_draw_simple_menu(self, mock_input):
        mock_input.side_effect = get_input
        items = [{"id": "new_game", "label": "New Game"}, {"id": "exit", "label": "Exit"}]
        menu = Menu(items, get_header())
        set_input([2])
        self.assertEqual("exit", menu.draw())

    @patch('cli_client.menu.do_print')
    @patch('cli_client.menu.get_input')
    def test_draw_menu_output(self, mock_input, mock_print):
        mock_input.side_effect = get_input
        mock_print.side_effect = capture_print
        set_input([2])
        items = [{"id":"new", "label": "New Game"}, {"id":"exit", "label": "Exit"}]
        menu = Menu(items, get_header())
        self.assertEqual("exit", menu.draw())
        self.assertEqual(9, len(lines))

    @patch('cli_client.menu.do_print')
    @patch('cli_client.menu.get_input')
    def test_debug(self, mock_input, mock_print):
        mock_input.side_effect = get_input
        mock_print.side_effect = capture_print
        set_input([2])
        items = [{"id": 'new', "label": "New Game"}, {"id": "exit", "label": "Exit"}]
        set_debug()
        menu = Menu(items, get_header())
        menu.draw()
        set_debug(on=False)
        dump_output(lines)

# TODO: test debug and connected
# TODO: Test errors, test back, test built in commands at any level


def dump_output(output_array):
    for s in output_array:
        print(s.rstrip('\n'))
