values = []
"""List of values that will be returned in order, simulating choices the user has made."""


def set_input(v):
    """Set the list of values."""
    global values
    values = v
    values.reverse()


def get_input():
    """User makes a choice."""
    global values
    return values.pop()