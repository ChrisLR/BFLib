from restrictions.base import Restriction


class HitDiceMaxSizeRestriction(Restriction):
    __slots__ = ["hit_dice_max_size"]

    def __init__(self, hit_dice_max_size):
        self.hit_dice_max_size = hit_dice_max_size
