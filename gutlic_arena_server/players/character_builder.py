from gutlic_arena_server import dice
from gutlic_arena_server.players.classes.fighter import Fighter
from gutlic_arena_server.players.classes.rogue import Rogue
from gutlic_arena_server.players.races.human import Human
from gutlic_arena_server.players.races.halfling import Halfling
"""Class to help with building characters"""


class CharacterBuilder:
    def __init__(self):
        pass

    @staticmethod
    def roll_stats():
        stats = []
        for _ in range(6):
            stats.append(CharacterBuilder._roll_stat())
        # the formula for calculating the perfect percentage is like this:
        # the sum of each stat - 3 divided by (18 - 3) * 6
        # 100% means all 18's, while 0% means all 3's
        return stats, (sum(stats) - 3 * 6) / (15 * 6)

    @staticmethod
    def available_classes():
        return [Fighter(), Rogue()]

    @staticmethod
    def available_races():
        return [Human(), Halfling()]

    @staticmethod
    def generate_name(race, full=False):
        # names are generated based on race
        # full means first and last, full = False means just first
        if isinstance(race, Human):
            if full:
                return 'Name Less'
            else:
                return 'Nameless'
        elif isinstance(race, Halfling):
            if full:
                return 'Nameless Halfling'
            else:
                return 'Halflingnoname'
        # should cause exception, means no names for this race yet
        return None

    @staticmethod
    def _roll_stat():
        # roll 4d6 and drop the lowest
        rolls = []
        for _ in range(4):
            rolls.append(dice.roll_dice(1, 6))
        rolls.sort(reverse=True)
        rolls.pop()
        return sum(rolls)
