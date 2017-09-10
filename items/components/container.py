import units
from items.components.base import ItemComponent


class Container(ItemComponent):
    NAME = "container"
    __slots__ = ["volume_limit", "weight_limit"]

    def __init__(self, volume_limit, weight_limit):
        self.volume_limit = volume_limit  # type: units.CubicFeet
        self.weight_limit = weight_limit  # type: units.Pound


class LiquidContainer(ItemComponent):
    NAME = "container"
    __slots__ = ["volume_limit"]

    def __init__(self, volume_limit):
        self.volume_limit = volume_limit  # type: units.Litre


class SpecialContainer(ItemComponent):
    NAME = "container"
    __slots__ = ["containable_items", "max_quantity"]

    def __init__(self, containable_items, max_quantity):
        self.containable_items = containable_items  # type: tuple
        self.max_quantity = max_quantity  # type: int
