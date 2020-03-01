import cli_client.utils as utils


def show_msg_box(msg):
    utils.clear_screen()
    utils.do_print(msg)
    utils.do_print('')
    utils.get_input('Press Enter to Continue...')
