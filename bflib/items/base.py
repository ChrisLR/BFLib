from bflib import units
from bflib.items import coins
from bflib.sizes import Size


class Item(object):
    name = ""

    price = coins.Copper
    size = Size.Medium
    wear_locations = tuple()
    weight = units.Pound
