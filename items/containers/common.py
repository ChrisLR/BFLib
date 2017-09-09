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
    wear_locations = WearLocation.Back,
    weight = units.Pound(0.1)
    weight_limit = units.Pound(40)


class BeltPouch(Container):
    name = "Belt Pouch"

    price = coins.Gold(1)
    size = Size.Small
    volume_limit = units.CubicFeet(1)
    wear_locations = WearLocation.Belt,
    weight = units.Pound(0.1)
    weight_limit = units.Pound(10)


class LargeSack(Container):
    name = "Large Sack"

    price = coins.Gold(1)
    size = Size.Medium
    volume_limit = units.CubicFeet(4)
    weight = units.Pound(0.1)
    weight_limit = units.Pound(40)


class Saddlebags(Container):
    name = "Saddlebags"

    price = coins.Gold(4)
    size = Size.Small
    volume_limit = units.CubicFeet(1)
    weight = units.Pound(7)
    weight_limit = units.Pound(10)


class SmallBackpack(Container):
    name = "Small Backpack"

    price = coins.Gold(4)
    size = Size.Small
    volume_limit = units.CubicFeet(1.5)
    wear_locations = WearLocation.Back,
    weight = units.Pound(0.1)
    weight_limit = units.Pound(30)


class SmallSack(Container):
    name = "Small Sack"

    price = coins.Silver(5)
    size = Size.Small
    volume_limit = units.CubicFeet(2)
    weight = units.Pound(0.1)
    weight_limit = units.Pound(20)
