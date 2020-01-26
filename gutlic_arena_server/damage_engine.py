"""Calculates and applies damage to target handling all the complex situations."""
from gutlic_arena_server import dice
from gutlic_arena_server.types.hit_type import HitType
from gutlic_arena_server.types.trait import Trait
from gutlic_arena_server.weapon import Weapon


def roll_damage(attacker, target, attack, hit, arena):
    damage = 0
    is_weapon = isinstance(attack, Weapon)
    if hit is HitType.HIT or hit is HitType.CRITICAL_HIT:
        dmg_mod = 0
        if is_weapon:
            if attack.get_finesse():
                dmg_mod += max(attacker.get_dex_mod(), attacker.get_str_mod())
            elif attack.is_melee():
                dmg_mod += attacker.get_str_mod()
            elif attack.is_ranged():
                dmg_mod += attacker.get_dex_mod()

        damage_roll = attack.get_damage()
        if is_weapon and attack.get_versatile() is not None and attacker.get_two_hands() == attack:
            damage_roll = attack.get_versatile()

        # TODO, this assumes the attack is the same as what is a hand
        if attacker.has_trait(Trait.FIGHTING_STYLE_DUELING) and attacker.get_two_hands() is None:
            # can only have one weapon, check each hand
            right = isinstance(attacker.get_right_hand(), Weapon)
            left = isinstance(attacker.get_left_hand(), Weapon)
            if (right is True and left is True) is False:
                dmg_mod += 2

        reroll_1_2 = False
        # TODO: this assumes the attack is the same as what is held two handed
        if attacker.has_trait(Trait.FIGHTING_STYLE_GREAT_WEAPON_FIGHTING) and attacker.get_two_hands() is not None:
            reroll_1_2 = True

        damage = dice.roll_damage(damage_roll, hit, dmg_mod, reroll_1_2)

    # damage can never be less than 0
    if damage < 0:
        return 0
    return damage
