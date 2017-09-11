import dice
import movement
import units
from carrycapacity import CarryCapacity
from characters.classes.fighter import Fighter
from monsters import attacks
from monsters.animals.base import Animal
from monsters.appearingset import AppearingSet
from tables.attackbonus import AttackBonusTable


class Camel(Animal):
    name = "Camel"
    attack_bonus = AttackBonusTable.get_by_hit_dice(2)
    attack_sets = [attacks.AttackSet(attacks.Bite(dice.D1(1))), attacks.AttackSet(attacks.Hoof(dice.D4(1)))]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(400), units.Pound(800))
    hit_dice = dice.D8(2)
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(50), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D4(2))
    save_as = Fighter.level_table.levels[2].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 75


class Donkey(Animal):
    name = "Donkey"
    attack_bonus = AttackBonusTable.get_by_hit_dice(2)
    attack_sets = [attacks.AttackSet(attacks.Bite(dice.D2(1)))]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(400), units.Pound(800))
    hit_dice = dice.D8(2)
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D4(2))
    save_as = Fighter.level_table.levels[2].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 75
