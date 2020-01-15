from enum import Enum
"""Hit, Miss or Crit"""


class HitType(Enum):
    """Modified roll less than target's AC"""
    MISS = 0
    """Modified roll >= target's AC"""
    HIT = 1
    """Normally this means a natural 20 was rolled."""
    CRITICAL_HIT = 2
    """Normally this means a natural 1 was rolled."""
    CRITICAL_MISS = 3
