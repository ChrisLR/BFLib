from items.base import Item
from keywords.items import WearLocation


class Armor(Item):
    wear_locations = WearLocation,


class Clothing(Armor):
    pass


class LightArmor(Armor):
    pass


class HeavyArmor(Armor):
    pass
