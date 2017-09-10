import units
from items.components.base import ItemComponent
from enum import Enum


class Tool(ItemComponent):
    NAME = "tool"
    __slots__ = ["qualities"]

    def __init__(self, height):
        self.height = height  # type: units.Feet


class ToolQuality(Enum):
    pass
