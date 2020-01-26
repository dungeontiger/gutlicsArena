from game_engine.types.entity_state import EntityState
"""This represents the arena or the environment.  Mostly it will be the participants"""


class Arena:
    def __init__(self, factions):
        # there must be at least two factions or there is no point in fighting
        self.factions = factions
        self.init_order = []

    def play_turn(self):
        self.determine_initiative_order()
        for e in self.init_order:
            e.take_turn(self)

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
        # if there are only zero or one factions with alive entites the arena is over
        alive_factions = 0
        for f in self.factions:
            for e in f.get_entities():
                if e.get_state() is not EntityState.DEAD:
                    alive_factions = alive_factions + 1
                    break
        return alive_factions <= 1

    def get_opposing_factions(self, faction):
        factions = []
        for f in self.factions:
            if f != faction:
                factions.append(f)
        return factions

    def get_winning_faction(self):
        if self.is_over():
            # return the first (and only) faction with someone not dead
            for f in self.factions:
                for e in f.get_entities():
                    if e.get_state() is not EntityState.DEAD:
                        return f
        return None
