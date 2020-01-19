from gutlic_arena_server import dice
from gutlic_arena_server.types.hit_type import HitType


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

    def roll_to_hit(self, target):
        # a natural 20 is always a hit, a critical hit
        # a natural 1 is always a miss
        # if modified roll >= AC its a hit
        roll = dice.d20()
        if roll == 20:
            return HitType.CRITICAL_HIT
        elif roll == 1:
            return HitType.CRITICAL_MISS
        else:
            if roll + self.to_hit >= target.get_ac():
                return HitType.HIT
        return HitType.MISS

    def roll_damage(self, target, hit_type=HitType.HIT):
        # roll damage and apply to target
        if hit_type is HitType.CRITICAL_HIT or hit_type is HitType.HIT:
            dmg = dice.roll_damage(self.dmg, hit_type)
            target.apply_damage(dmg, self.dmg_type)


