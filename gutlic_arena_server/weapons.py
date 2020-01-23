import json, os
from .weapon import Weapon
from .types.weapon_type import WeaponType
from .types.damage_type import DamageType
from .types.weapon_id import WeaponId

# all the weapons are basically the same - no special behavior
# so they can all be defined in JSON and loaded
"""Global to hold all the weapon definitions"""

weapons = {}

weapon_type = {'simple_melee': WeaponType.SIMPLE_MELEE,
               'simple_ranged': WeaponType.SIMPLE_RANGED,
               'martial_ranged': WeaponType.MARTIAL_RANGED,
               'martial_melee': WeaponType.MARTIAL_MELEE}

damage_type = {'bludgeoning': DamageType.BLUDGEONING,
               'piercing': DamageType.PIERCING,
               'slashing':  DamageType.SLASHING}

weapon_id = { 'Club': WeaponId.CLUB,
              'Dagger': WeaponId.DAGGER ,
              'Greatclub': WeaponId.GREATCLUB,
              'Handaxe': WeaponId.HANDAXE,
              'Javelin': WeaponId.JAVELIN,
              'Light hammer': WeaponId.LIGHT_HAMMER,
              'Mace': WeaponId.MACE,
              'Quarterstaff': WeaponId.QUARTERSTAFF,
              'Sickle': WeaponId.SICKLE,
              'Spear': WeaponId.SPEAR,
              'Light crossbow': WeaponId.LIGHT_CROSSBOW,
              'Dart': WeaponId.DART,
              'Shortbow': WeaponId.SHORTBOW,
              'Sling': WeaponId.SLING,
              'Battleaxe': WeaponId.BATTLEAXE,
              'Flail': WeaponId.FLAIL,
              'Glaive': WeaponId.GLAIVE,
              'Greataxe': WeaponId.GREATAXE,
              'Halberd': WeaponId.HALBERD,
              'Lance': WeaponId.LANCE,
              'Longsword': WeaponId.LONGSWORD,
              'Maul': WeaponId.MAUL,
              'Morningstar': WeaponId.MORNINGSTAR,
              'Pike': WeaponId.PIKE,
              'Rapier': WeaponId.RAPIER,
              'Scimitar': WeaponId.SCIMITAR,
              'Shortsword': WeaponId.SHORTSWORD,
              'Trident': WeaponId.TRIDENT,
              'War pick': WeaponId.WAR_PICK,
              'Warhammer': WeaponId.WARHAMMER,
              'Whip': WeaponId.WHIP,
              'Blowgun': WeaponId.BLOWGUN,
              'Hand crossbow': WeaponId.HAND_CROSSBOW,
              'Heavy crossbow': WeaponId.HEAVY_CROSSBOW,
              'Longbow': WeaponId.LONGBOW,
              'Net': WeaponId.NET,
              'Unarmed': WeaponId.UNARMED,
              'Greatsword': WeaponId.GREATSWORD}

# this should only be run once when this module is actually loaded
with open(os.path.join(os.path.dirname(__file__), 'resources/weapons.json')) as json_file:
    data = json.load(json_file)
    for w in data:
        _id = weapon_id[w["name"]]
        weapons[_id] = Weapon(w["name"], _id, weapon_type[w["type"]], w["cost"], w["damage"],
                              damage_type[w["damage_type"]], w["weight"], w["light"], w["finesse"], w["thrown"],
                              w["two-handed"], w["versatile"], w["ammo"], w["reach"], w["heavy"], w["loading"],
                              w["special"], w["range"], w["long_range"])
