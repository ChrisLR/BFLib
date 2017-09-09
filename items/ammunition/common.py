import dice
import units
from items import coins
from items.ammunition.base import Ammunition


class Arrow(Ammunition):
    pass


class Bolt(Ammunition):
    pass


class OilFlask(Ammunition):
    name = "Oil Flask"

    price = coins.Gold(1)
    weight = units.Pound(1)


class ShortbowArrow(Arrow):
    name = "Shortbow Arrow"

    damage = dice.D6(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)
