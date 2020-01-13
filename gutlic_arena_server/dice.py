import random, re


def roll(dice_str):
    # dice string is in the format 2d6 + 3, spaces and case of the d not relevant
    m = re.search(r'(\d*)[dD](\d*)\s*([+-]\s*\d*)?', dice_str)
    # these two are required, so 1d6 is valid, d6 is not
    a = int(m.group(1))
    d = int(m.group(2))
    # the modifier maybe missing
    mod = 0
    if m.group(3) is not None:
        mod = int(m.group(3).replace(' ', ''))
    return roll_dice(a, d, mod)


def roll_dice(amount, dice, plus):
    total = plus
    for i in range(0, amount):
        total += _random_int(1, dice)
    return total


def roll_hp(hd):
    return 5


def d20():
    return _random_int(1, 20)


def _random_int(lower, upper):
    # so the random behavior in dice can be easily mocked out during testing
    return random.randint(lower, upper)
