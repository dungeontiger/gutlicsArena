"""Calculates and applies damage to target handling all the complex situations."""
from gutlic_arena_server import dice
from gutlic_arena_server.types.hit_type import HitType


def roll_damage(attacker, target, attack, hit, arena):
    damage = 0
    if hit is HitType.HIT or hit is HitType.CRITICAL_HIT:
        dmg_mod = 0
        if attack.get_finesse():
            dmg_mod += max(attacker.get_dex_mod(), attacker.get_str_mod())
        elif attack.is_melee():
            dmg_mod += attacker.get_str_mod()
        elif attack.is_ranged():
            dmg_mod += attacker.get_dex_mod()
        damage = dice.roll_damage(attack.get_damage(), hit, dmg_mod)
    return damage
