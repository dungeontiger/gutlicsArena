from .types.roll_type import RollType


class Armor:
    def __init__(self, _name, _id, _type, cost, ac, max_dex_mod, str_required, stealth, weight):
        self._name = _name
        self._id = _id
        self._type = _type
        self.cost = cost
        self.ac = ac
        self.max_dex_mod = max_dex_mod
        self.str_required = str_required
        if stealth == 'disadvantage':
            self.stealth = RollType.DISADVANTAGE
        else:
            self.stealth = RollType.NORMAL
        self.weight = weight

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_type(self):
        return self._type

    def get_cost(self):
        return self.cost

    def get_ac(self):
        return self.ac

    def get_max_dex_mod(self):
        return self.max_dex_mod

    def get_str_required(self):
        return self.str_required

    def get_stealth(self):
        return self.stealth

    def get_weight(self):
        return self.weight
