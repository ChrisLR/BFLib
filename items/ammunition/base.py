import dice
import units
from items import coins
from items.base import Item


class Ammunition(Item):
    damage = dice.Dice
    price = coins.Copper
    weight = units.Pound
