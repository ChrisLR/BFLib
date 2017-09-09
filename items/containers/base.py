import units
from items.base import Item


class Container(Item):
    volume_limit = units.CubicFeet
    weight_limit = units.Pound
