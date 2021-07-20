from dataclasses import dataclass

@dataclass
class Stats:
    """Contains all statistics for an object"""
    strength: int = 0
    agility: int = 0
    fortitude: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0
    luck: int = 0
    accuracy: int = 0
    avoidance: int = 0
    damage: int = 0
    reduction: int = 0
    penetration: int = 0
    resistance: int = 0
