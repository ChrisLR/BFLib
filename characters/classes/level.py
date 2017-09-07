class Level(object):
    __slots__ = ["value", "experience_required", "hit_dice", "spell_slots_set"]

    def __init__(self, value, experience_required, hit_dice, spell_slots_set):
        self.value = value
        self.experience_required = experience_required
        self.hit_dice = hit_dice
        self.spell_slots_set = spell_slots_set


class LevelTable(object):
    __slots__ = ["levels"]

    def __init__(self, levels=None):
        self.levels = {level.value: level for level in levels} if levels else {}
