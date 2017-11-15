from bflib.restrictions.base import Restriction


class ArmorRestrictionSet(Restriction):
    __slots__ = ["included", "excluded", "shields"]

    def __init__(self, included=None, excluded=None, shields=True):
        self.included = included
        self.excluded = excluded
        self.shields = shields
