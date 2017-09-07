from restrictions.base import Restriction


class ClassRestrictionSet(Restriction):
    __slots__ = ["access_combined", "included", "excluded"]

    def __init__(self, included=None, excluded=None, access_combined=False):
        """
        :param included: Iterable, If Set, this restricts class selection to those defined.
        :param excluded: Iterable, If Set, this prevents defined classes to be selected.
        :param access_combined: Bool, If True, this allows the character to use combined classes.
        """
        self.included = included
        self.excluded = excluded
        self.access_combined = access_combined
