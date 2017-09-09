import units
from keywords.items import WearLocation
from sizes import Size
from items import coins


class Item(object):
    name = ""

    price = coins.Copper
    size = Size.Medium
    wear_location = WearLocation.none
    weight = units.Pound
