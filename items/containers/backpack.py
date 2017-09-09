import units
from items import coins
from items.containers.base import Container
from keywords.items import WearLocation
from sizes import Size


class Backpack(Container):
    name = "Backpack"

    price = coins.Gold(4)
    size = Size.Medium
    volume_limit = units.CubicFeet(3)
    wear_location = WearLocation.Back
    weight = units.Pound(0.1)
    weight_limit = units.Pound(40)


class BeltPouch(Container):
    name = "Belt Pouch"

    price = coins.Gold(1)
    size = Size.Small
    volume_limit = units.CubicFeet(1)
    wear_location = WearLocation.Waist
    weight = units.Pound(0.1)
    weight_limit = units.Pound(10)


class SmallBackpack(Container):
    name = "Small Backpack"

    price = coins.Gold(4)
    size = Size.Small
    volume_limit = units.CubicFeet(1.5)
    wear_location = WearLocation.Back
    weight = units.Pound(0.1)
    weight_limit = units.Pound(30)
