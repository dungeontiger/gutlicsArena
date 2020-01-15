"""Singleton type pattern"""

values = []


def set_values(v):
    global values
    values = v
    values.reverse()


def value(lower, upper):
    global values
    return values.pop()
