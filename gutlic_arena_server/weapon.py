from gutlic_arena_server.types.weapon_type import WeaponType
from .actions.damage_type import DamageType


class Weapon:
    def __init__(self, name, _type, cost, damage, damage_type, weight, light, finesse, thrown, two_handed,
                 versatile, ammo, reach, heavy, loading, special, _range, long_range):
        self.name = name
        if _type == 'simple_melee':
            self.type = WeaponType.SIMPLE_MELEE
        elif _type == 'simple_ranged':
            self.type = WeaponType.SIMPLE_RANGED
        elif _type == 'martial_ranged':
            self.type = WeaponType.MARTIAL_RANGED
        elif _type == 'martial_melee':
            self.type = WeaponType.MARTIAL_MELEE
        else:
            self.type = WeaponType.UNKNOWN
        self.cost = cost
        self.damage = damage
        if damage_type == 'bludgeoning':
            self.damage_type = DamageType.BLUDGEONING
        elif damage_type == 'piercing':
            self.damage_type = DamageType.PIERCING
        elif damage_type == 'slashing':
            self.damage_type = DamageType.SLASHING
        else:
            self.damage_type = DamageType.UNKNOWN
        self.weight = weight
        self.light = light
        self.finesse = finesse
        self.thrown = thrown
        self.two_handed = two_handed
        self.versatile = versatile
        self.ammo = ammo
        self.reach = reach
        self.heavy = heavy
        self.loading = loading
        self.special = special
        self.range = _range
        self.long_range = long_range

    def is_melee(self):
        return self.type is WeaponType.MARTIAL_MELEE or self.type is WeaponType.SIMPLE_MELEE

    def is_ranged(self):
        return self.type is WeaponType.SIMPLE_RANGED or self.type is WeaponType.MARTIAL_RANGED

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_cost(self):
        return self.cost

    def get_damage(self):
        return self.damage

    def get_damage_type(self):
        return self.damage_type

    def get_weight(self):
        return self.weight

    def get_light(self):
        return self.light

    def get_finesse(self):
        return self.finesse

    def get_thrown(self):
        return self.thrown

    def get_two_handed(self):
        return self.two_handed

    def get_versatile(self):
        return self.versatile

    def get_ammo(self):
        return self.ammo

    def get_reach(self):
        return self.reach

    def get_heavy(self):
        return self.heavy

    def get_loading(self):
        return self.loading

    def get_special(self):
        return self.special

    def get_range(self):
        return self.range

    def get_long_range(self):
        return self.long_range

    def __str__(self):
        return self.name
