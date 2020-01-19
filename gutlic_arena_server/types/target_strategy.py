from enum import Enum
"""Strategies for how the monster will select a target."""


class TargetStrategy(Enum):
    UNKNOWN = 0
    """If no target, randomly select one. Otherwise stay with the current target."""
    STICKY_RANDOM = 1
    """Select a new random target each turn."""
    RANDOM = 2
