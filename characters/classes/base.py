from characters.classes import LevelTable
from characters.classes.abilities import ClassAbilitySet
import restrictions


class CharacterClass(object):
    name = ""
    class_abilities = ClassAbilitySet()
    level_experience_table = LevelTable()
    restriction_set = restrictions.RestrictionSet()
