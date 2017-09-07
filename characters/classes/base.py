import restrictions
from characters.classes import LevelTable
from characters.specialabilities import SpecialAbilitySet


class CharacterClass(object):
    name = ""
    restriction_set = restrictions.RestrictionSet()
    special_abilities = SpecialAbilitySet()
    level_table = LevelTable()

