import dice
import movement
from characters import specialabilities


class Monster(object):
    name = ""
    attack_bonus = 0
    attack_sets = []
    base_armor_class = 0
    hit_dice = dice.Dice
    movement = movement.MovementSet
    special_abilities = specialabilities.SpecialAbilitySet
