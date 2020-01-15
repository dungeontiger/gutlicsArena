
"""This represents the arena or the environment.  Mostly it will be the participants"""


class Arena:
    def __init__(self, factions):
        # there must be at least two factions or there is no point in fighting
        self.factions = factions
        self.init_order = []
        self.is_over = False

    def take_turn(self):
        self.determine_initiative_order()
        for f in self.factions:
            for e in f.get_entities:
                e.take_action(self)

    def determine_initiative_order(self):
        # place all of the participants from all factions in initiative order
        self.init_order = []
        init_map = {}
        for f in self.factions:
            for e in f.get_entities():
                init_map[e.roll_initiative()] = e

        # iterate over the sorted keys to make an ordered list of initiative order
        for i in sorted(init_map.keys(), reverse=True):
            self.init_order.append(init_map[i])

    def get_init_order(self):
        return self.init_order

    def is_over(self):
        return self.is_over

    def get_opposing_factions(self, faction):
        factions = []
        for f in self.factions:
            if f != faction:
                factions.append(f)
        return factions
