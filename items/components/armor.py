from enum import Enum
from items.components.base import ItemComponent


class ArmorTypes(Enum):
    Light = "Light"
    Medium = "Medium"
    Heavy = "Heavy"


class Armor(ItemComponent):
    NAME = "armor"
    types = ArmorTypes

    def __init__(self, armor_class, armor_type):
        self.armor_class = armor_class
        self.armor_type = armor_type
