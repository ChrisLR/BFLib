from keywords.weapons import WeaponWieldKeyword
from restrictions.base import Restriction


class WeaponRestrictionSet(Restriction):
    __slots__ = ["included", "excluded"]

    def __init__(self, included=None, excluded=None):
        self.included = included
        self.excluded = excluded


class WeaponSizeRestrictionSet(Restriction):
    __slots__ = ["large", "medium", "small"]
    keywords = WeaponWieldKeyword

    def __init__(self, large=keywords.CanWield, medium=keywords.CanWield, small=keywords.CanWield):
        self.large = large
        self.medium = medium
        self.small = small
