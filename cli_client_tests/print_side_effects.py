lines = []
"""Lines of text there were printed."""


def capture_print(t, end='\n'):
    """Side effect method to capture what was printed to the console so it can be validated."""
    lines.append(t + end)


def clear():
    """Mocks clear screen.  Clears the lines of text"""
    # TODO: this should actually create a stack of output so I can test each screen
    lines.clear()
