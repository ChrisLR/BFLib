from items.components.base import ItemComponent
from enum import Enum


class WearLocation(Enum):
    Any = "Any"
    Back = "back"
    Bandolier = "bandolier"
    Belt = "belt"
    Feet = "feet"
    Torso = "torso"
    Arms = "Arms"
    Legs = "Legs"
    Waist = "waist"
    none = None


class WearableSet(object):
    __slots__ = ["wear_on_slots", "covers_slots"]

    def __init__(self, wear_on_slots, covers_slots=None):
        """
        :param wear_on_slots: Slots this object occupies
        :param covers_slots:  Slots this object may cover
        """
        self.wear_on_slots = wear_on_slots
        self.covers_slots = covers_slots


class Wearable(ItemComponent):
    NAME = "wearable"
    __slots__ = ["wearable_slots_sets"]

    def __init__(self, wearable_slots_sets):
        self.wearable_slots_sets = wearable_slots_sets
