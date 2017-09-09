from enum import Enum


class GenericItemKeyword(Enum):
    WearLocation = "WearLocation"


class WearLocation(Enum):
    Any = "Any"
    Back = "back"
    Waist = "waist"
    none = None
