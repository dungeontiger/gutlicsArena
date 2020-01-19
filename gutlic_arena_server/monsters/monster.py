import random
from gutlic_arena_server.types.target_strategy import TargetStrategy
from gutlic_arena_server import dice
from gutlic_arena_server.types.entity_state import EntityState
from gutlic_arena_server.entity import Entity


class Monster(Entity):
    def __init__(self, name, _str, _dex, _con, _int, _wis, _cha, _ac, _hd):
        super(Monster, self).__init__(name, _str, _dex, _con, _int, _wis, _cha)
        self.hd = _hd
        self.ac = _ac
        self.hp = dice.roll(_hd)
        self.cur_hp = self.hp

        # not on constructor because it would be too long
        self.actions = []

        # game time attributes
        self.target = None
        self.state = EntityState.NORMAL

    def get_hd(self):
        return self.hd

    def set_actions(self, actions):
        self.actions = actions

    def get_actions(self):
        return self.actions

    def get_state(self):
        return self.state

    def take_turn(self, arena):
        """Must be overloaded in the child class."""
        pass

    def select_target(self, strategy):
        if strategy == TargetStrategy.STICKY_RANDOM:
            if self.target is None or self.target.is_dead():
                self.target = random.choice(self.get_all_targets())
        elif strategy == TargetStrategy.RANDOM:
            self.target = random.choice(self.get_all_targets())

    def get_all_targets(self):
        targets = []
        for faction in self.arena.get_opposing_factions(self.faction):
            for e in faction.get_entities():
                targets.append(e)
        return targets

    def select_action(self, target):
        # for now just pick the first action
        return self.actions[0]

    def apply_damage(self, damage, damage_type):
        # eventually damage type will be used for resistances etc
        self.cur_hp = self.cur_hp - damage
        if self.cur_hp <= 0:
            self.state = EntityState.DEAD

    def is_dead(self):
        return self.state is EntityState.DEAD

    def __str__(self):
        return self.name
