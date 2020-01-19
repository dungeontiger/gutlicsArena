import json, os
from .weapon import Weapon

# all the weapons are basically the same - no special behavior
# so they can all be defined in JSON and loaded
"""Global to hold all the weapon definitions"""

weapons = {}

# this should only be run once when this module is actually loaded
with open(os.path.join(os.path.dirname(__file__), 'resources/weapons.json')) as json_file:
    data = json.load(json_file)
    for w in data:
        weapons[w["name"]] = Weapon(w["name"], w["type"], w["cost"], w["damage"], w["damage_type"], w["weight"],
                                 w["light"], w["finesse"], w["thrown"], w["two-handed"], w["versatile"], w["ammo"],
                                 w["reach"], w["heavy"], w["loading"], w["special"], w["range"], w["long_range"])
