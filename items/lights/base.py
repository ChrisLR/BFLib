import dice
import units
from items.base import Item
from shapes import Shape


class LightItem(Item):
    bright_light_radius = units.Feet
    dim_light_radius = units.Feet
    fuel = Item
    fuel_duration = units.GameTurn
    last_life_dice = dice.Dice
    light_shape = Shape
