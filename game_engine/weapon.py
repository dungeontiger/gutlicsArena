from game_engine.types.weapon_type import WeaponType


class Weapon:
    def __init__(self, name, _id, _type, cost, damage, damage_type, weight, light, finesse, thrown, two_handed,
                 versatile, ammo, reach, heavy, loading, special, _range, long_range):
        self.name = name
        self._id = _id
        self._type = _type
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
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
        return self._type is WeaponType.MARTIAL_MELEE or self._type is WeaponType.SIMPLE_MELEE

    def is_ranged(self):
        return self._type is WeaponType.SIMPLE_RANGED or self._type is WeaponType.MARTIAL_RANGED

    def get_name(self):
        return self.name

    def get_type(self):
        return self._type

    # TODO: need to implement most of these features, reach, light, etc...
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

    # TODO: special means special rules for this weapon
    def get_special(self):
        return self.special

    def get_range(self):
        return self.range

    def get_long_range(self):
        return self.long_range

    def get_id(self):
        return self._id

    def __str__(self):
        return self.name
