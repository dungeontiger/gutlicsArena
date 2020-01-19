from enum import Enum
"""State for monsters and such."""


class EntityState(Enum):
    UNKNOWN = 0
    """Entity is alive, fighting and not hiding or anything like that.."""
    NORMAL = 1
    """Entity is dead.  HP were lower than 1"""
    DEAD = 2
