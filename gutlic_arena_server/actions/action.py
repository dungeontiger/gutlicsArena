from gutlic_arena_server import dice


class Action:
    def __init__(self, _name, _type, to_hit, dmg, dmg_type, reach, targets):
        self.name = _name
        self.type = _type
        self.to_hit = to_hit
        self.dmg = dmg
        self.dmg_type = dmg_type
        self.reach = reach
        self.targets = targets

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_to_hit(self):
        return self.to_hit

    def get_dmg(self):
        return dice.roll(self.dmg)

    def get_dmg_str(self):
        return self.dmg

    def get_dmg_type(self):
        return self.dmg_type

    def get_reach(self):
        # reach is always measured in feet
        return self.reach

    def get_targets(self):
        return self.targets
