from cli_client_tests.print_side_effects import capture_print

values = []
"""List of values that will be returned in order, simulating choices the user has made."""


def set_input(v):
    """Set the list of values."""
    global values
    values = v
    values.reverse()


def get_input(prompt):
    """User makes a choice."""
    global values
    capture_print(prompt)
    return values.pop()
