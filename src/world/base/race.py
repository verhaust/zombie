from dataclasses import dataclass
from . import stats

@dataclass
class Dimension:
    """Dimension of the object on one axes. It has 3 values:

      min - The smallest space necessary for this object to exist on this axis
      mid - The space needed for this object to be comfortable on this axis.  (ie. enough space to comfortably move your arms)
      max - The largest space this object can take up on this axis

      units are *roughly* centimeters
    """
    min: int = 1
    mid: int = 1
    max: int = 1
    
@dataclass
class Dimensions:
    """Describes the x,y,z dimensions of the object. The axes are described as if the object is facing you.

      x - horizontal plane
      y - vertical plane
      z - depth plane
    """
    x: Dimension
    y: Dimension
    z: Dimension


class BodyPart(object):
    def __init__(self, name=None, dimensions=None, equip_slots=[]):
        self.id = id
        self.name = name
        self.description = description
        self.dimensions = dimensions
        self.equip_slots = equip_slots
        self.equipped = equipped
        self.stats = stats

class Arm(BodyPart):
    def __init__(self):
        id = 'arm'
        name='Arm'
        description='An arm'
        x = Dimension('min'=4, 'mid'=10, 'max'=20)
        y = Dimension('min'=4, 'mid'=20, 'max'=20)
        z = Dimension('min'=4, 'mid'=10, 'max'=20)
        dimensions=Dimensions(x=x,y=y,z=z)
        equip_slots=['arm'])
        stats = stat.Stats()
        super().__init__(id=id, name=name, description=description, dimensions=dimensions, equip_slots=equip_slots, stats=stats)

class Leg(BodyPart):
    def __init__(self):
        id = 'leg'
        name='Leg'
        description='A leg'
        x = Dimension('min'=4, 'mid'=10, 'max'=20)
        y = Dimension('min'=4, 'mid'=20, 'max'=20)
        z = Dimension('min'=4, 'mid'=10, 'max'=20)
        dimensions=Dimensions(x=x,y=y,z=z)
        equip_slots=['leg'])
        stats = stat.Stats()
        super().__init__(id=id, name=name, description=description, dimensions=dimensions, equip_slots=equip_slots, stats=stats)

class Torso(BodyPart):
    def __init__(self):
        id = 'torso'
        name='Torso'
        description='A torso'
        x = Dimension('min'=4, 'mid'=10, 'max'=20)
        y = Dimension('min'=4, 'mid'=20, 'max'=20)
        z = Dimension('min'=4, 'mid'=10, 'max'=20)
        dimensions=Dimensions(x=x,y=y,z=z)
        equip_slots=['torso'])
        stats = stat.Stats()
        super().__init__(id=id, name=name, description=description, dimensions=dimensions, equip_slots=equip_slots, stats=stats)

class Being(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.body = None
        self.stats = None
