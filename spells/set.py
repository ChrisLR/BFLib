class SpellSlotSet(object):
    __slots__ = ["spell_slots"]

    def __init__(self, spell_slots=None):
        self.spell_slots = spell_slots


class SpellSet(object):
    __slots__ = ["spells"]

    def __init__(self, spells):
        self.spells = {spell.level: spell for spell in spells}
