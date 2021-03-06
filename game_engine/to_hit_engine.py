"""Handle the complex logic of rolling to hit and accounting for all circumstances."""
from game_engine.types.hit_type import HitType
from game_engine import dice
from game_engine.types.trait import Trait
from game_engine.types.roll_type import RollType
from game_engine.weapon import Weapon


def roll_to_hit(attacker, target, attack, arena):
    # defaults
    hit = HitType.MISS

    # differences between weapons and monster attacks
    is_weapon = isinstance(attack, Weapon)

    if is_weapon:
        # get proficiency bonus for this weapon
        to_hit_mod = attacker.get_proficiency_bonus(attack)

        # pick either str or dex modifier as appropriate
        if attack.get_finesse():
            to_hit_mod += max(attacker.get_dex_mod(), attacker.get_str_mod())
        elif attack.is_melee():
            to_hit_mod += attacker.get_str_mod()
        elif attack.is_ranged():
            to_hit_mod += attacker.get_dex_mod()
    else:
        to_hit_mod = attack.get_to_hit()

    # TODO: determine advantage / disadvantage; flanking, etc.

    roll_type = RollType.NORMAL
    if is_weapon and attacker.wearing_unproficient_armor():
        roll_type = RollType.DISADVANTAGE

    # make the roll
    roll = dice.d20(roll_type)

    # if lucky can re-roll ones
    if roll == 1 and attacker.has_trait(Trait.LUCKY):
        roll = dice.d20()

    # natural rolls checked before applying modifiers
    if roll == 20:
        return HitType.CRITICAL_HIT
    elif roll == 1:
        return HitType.CRITICAL_MISS

    # fighting style modifications
    if attacker.has_trait(Trait.FIGHTING_STYLE_ARCHERY) and attack.is_ranged():
        roll += 2

    # defense fighting style applies to the defender
    ac_mod = 0
    if target.has_trait(Trait.FIGHTING_STYLE_DEFENCE) and target.get_armor() is not None:
        ac_mod += 1

    # determine outcome
    elif roll + to_hit_mod >= target.get_ac() + ac_mod:
        hit = HitType.HIT

    return hit
