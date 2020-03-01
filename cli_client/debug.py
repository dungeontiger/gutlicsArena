_debug = False
_connected = False


def set_debug(on=True):
    global _debug
    _debug = on


def is_debug():
    global _debug
    return _debug


def set_connected(connected=True):
    global _connected
    _connected = connected


def is_connected():
    global _connected
    return _connected
