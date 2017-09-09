import units
from items import coins
from items.containers.base import SpecialContainer
from keywords.items import WearLocation
from sizes import Size
from items import writing


class ScrollCase(SpecialContainer):
    name = "Scroll Case"

    containable_items = writing.Scroll, writing.Map
    max_quantity = 10
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.5)
    wear_locations = WearLocation.Belt, WearLocation.Bandolier


class Quiver(SpecialContainer):
    name = "Quiver"

    containable_items = writing.Scroll, writing.Map
    max_quantity = 20
    price = coins.Gold(1)
    size = Size.Medium
    weight = units.Pound(1)
    wear_locations = WearLocation.Back
