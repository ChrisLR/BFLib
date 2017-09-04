import abc
import units
from datetime import timedelta


class Race(object):
    __metaclass__ = abc.ABCMeta

    name = ""
    average_height = units.Feet(0)
    average_weight = units.Pound(0)
    average_lifespan = timedelta(days=36500)
    ability_score_restriction_set
    body_keyword_set
    class_restriction_set
    personality_keyword_set
    special_ability_set
    saving_throw_set
    weapon_restriction_set
