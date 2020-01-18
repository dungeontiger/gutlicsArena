"""Class base class for players"""


class Class:
    def __init__(self, name, hd):
        self.name = name
        self.hd = hd

    def get_hd(self):
        return self.hd

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name
