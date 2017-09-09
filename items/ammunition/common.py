import dice
import units
from items import coins
from items.ammunition.base import Ammunition


class Arrow(Ammunition):
    pass


class ShortbowArrow(Arrow):
    name = "Shortbow Arrow"

    damage = dice.D6(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)
