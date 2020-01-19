"""Handle the complex logic of rolling to hit and accounting for all circumstances."""
from gutlic_arena_server.types.hit_type import HitType
from gutlic_arena_server import dice
from gutlic_arena_server.types.trait import Trait


def roll_to_hit(attacker, target, attack, arena):

    # get proficiency bonus for this weapon
    to_hit_mod = attacker.get_proficiency_bonus(attack)

    # pick either str or dex modifier as appropriate
    if attack.get_finesse():
        to_hit_mod += max(attacker.get_dex_mod(), attacker.get_str_mod())
    elif attack.is_melee():
        to_hit_mod += attacker.get_str_mod()
    elif attack.is_ranged():
        to_hit_mod += attacker.get_dex_mod()

    # TODO: determine advantage / disadvantage; flanking, etc.

    # TODO: fighting style archer bonus

    roll = dice.d20()

    # if lucky can reroll ones
    if roll == 1 and attacker.has_trait(Trait.LUCKY):
        roll = dice.d20()

    # determine outcome
    if roll == 20:
        hit = HitType.CRITICAL_HIT
    elif roll == 1:
        hit = HitType.CRITICAL_MISS
    elif roll + to_hit_mod >= target.get_ac():
        hit = HitType.HIT
    else:
        hit = HitType.MISS

    return hit
