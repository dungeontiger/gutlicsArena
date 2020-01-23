import json, os
from .armor import Armor
from .types.armor_type import ArmorType
from .types.armor_id import ArmorId

# all the armor are basically the same - no special behavior
# so they can all be defined in JSON and loaded
"""Global to hold all the armor definitions"""

armors = {}

armor_type = {'light_armor': ArmorType.LIGHT_ARMOR,
              'medium_armor': ArmorType.MEDIUM_ARMOR,
              'heavy_armor': ArmorType.HEAVY_ARMOR,
              'shield': ArmorType.SHIELD}

armor_id = {'Padded': ArmorId.PADDED,
            'Leather': ArmorId.LEATHER,
            'Studded leather': ArmorId.STUDDED_LEATHER,
            'Hide': ArmorId.HIDE,
            'Chain shirt': ArmorId.CHAIN_SHIRT,
            'Scale mail': ArmorId.SCALE_MAIL,
            'Breastplate': ArmorId.BREASTPLATE,
            'Half plate': ArmorId.HALF_PLATE,
            'Ring mail': ArmorId.RING_MAIL,
            'Chain mail': ArmorId.CHAIN_MAIL,
            'Splint': ArmorId.SPLINT,
            'Plate': ArmorId.PLATE,
            'Shield': ArmorId.SHIELD}

# this should only be run once when this module is actually loaded
with open(os.path.join(os.path.dirname(__file__), 'resources/armor.json')) as json_file:
    data = json.load(json_file)
    for w in data:
        _id = armor_id[w["name"]]
        armors[_id] = Armor(w["name"], _id, armor_type[w["type"]], w["cost"], w["ac"], w["max_dex_mod"], w["str_required"],
                            w["stealth"], w["weight"])
