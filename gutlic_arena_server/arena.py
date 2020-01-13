class Arena:
    """This represents the arena or the environment.  Mostly it will be the participants"""
    def __init__(self, factions):
        # there must be at least two factions or there is no point in fighting
        self.factions = factions
        self.init_order = []

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
