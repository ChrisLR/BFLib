class RestrictionSet(object):
    __slots__ = ["ability_score", "armor", "classes", "hit_dice_max_size", "weapons", "weapon_size"]

    def __init__(self, ability_score=None, armor=None, classes=None, hit_dice_max_size=None,
                 weapons=None, weapon_size=None):
        self.ability_score = ability_score
        self.armor = armor
        self.classes = classes
        self.hit_dice_max_size = hit_dice_max_size
        self.weapons = weapons
        self.weapon_size = weapon_size
