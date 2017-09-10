import units
from items.base import Item
from items import coins
from items import components
from items.components.wearable import WearableSet, WearLocation


class Cloak(Item):
    name = "Cloak"

    price = coins.Gold(2)
    wearable = components.Wearable(WearableSet(WearLocation.Neck, WearLocation.Back))
    weight = units.Pound(1)


class CommonOutfit(Item):
    name = "Common Outfit"

    wearable = components.Wearable(WearableSet(WearLocation.Neck, WearLocation.Back))
    price = coins.Gold(4)
    weight = units.Pound(1)
