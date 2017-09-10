import units
from items import coins
from sizes import Size


class Item(object):
    name = ""

    price = coins.Copper
    size = Size.Medium
    wear_locations = tuple()
    weight = units.Pound
