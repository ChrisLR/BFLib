from enum import Enum


class GenericItemKeyword(Enum):
    WearLocation = "WearLocation"


class WearLocation(Enum):
    Any = "Any"
    Back = "back"
    Bandolier = "bandolier"
    Belt = "belt"
    Waist = "waist"
    none = None
