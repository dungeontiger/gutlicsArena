# TODO: will require a special subclass for the player faction I think; unless PCs are monster sub classes too


class Faction:
    """
    A faction represents one side in the arena.
    Typically there will only be two factions, the players and the monsters.
    """
    def __init__(self, _name, entities):
        self.name = _name
        self.entities = entities
        # set the faction for each entity so we know who is who
        for e in entities:
            e.set_faction(self)

    def get_entities(self):
        return self.entities

    def get_name(self):
        return self.name
