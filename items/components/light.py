import units
from items.components.base import ItemComponent
from items.base import Item
import dice
import shapes


class Light(ItemComponent):
    NAME = "light"
    __slots__ = ["bright_light_radius", "dim_light_radius", "fuel", "fuel_duration", "last_life_dice", "light_shape"]

    def __init__(self, bright_light_radius, dim_light_radius, fuel, fuel_duration, last_life_dice, light_shape):
        self.bright_light_radius = bright_light_radius  # type: units.Feet
        self.dim_light_radius = dim_light_radius  # type: units.Pound
        self.fuel = fuel  # type: Item
        self.fuel_duration = fuel_duration  # type: units.GameTurn
        self.last_life_dice = last_life_dice  # type: dice.Dice
        self.light_shape = light_shape  # type: shapes.Shape
