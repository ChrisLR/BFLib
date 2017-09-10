import units
from items.components.base import ItemComponent


class Climbing(ItemComponent):
    NAME = "climbing"
    __slots__ = ["height"]

    def __init__(self, height):
        self.height = height  # type: units.Feet
