from bflib.restrictions.base import Restriction


class AbilityScoreRestrictionSet(Restriction):
    __slots__ = ["minimum_set", "maximum_set"]

    def __init__(self, minimum_set=None, maximum_set=None):
        self.minimum_set = minimum_set
        self.maximum_set = maximum_set
