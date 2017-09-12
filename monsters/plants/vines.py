import dice
import movement
import units
from attacks import AttackSet, Crush
from characters import specialabilities
from characters.classes.fighter import Fighter
from monsters.appearingset import AppearingSet
from monsters.plants.base import Plant
from tables.attackbonus import AttackBonusTable
from treasuretypes import TreasureType
from attacks.specialproperties import CrushingEntanglement


class AssassinVine(Plant):
    name = "Assassin Vine"
    hit_dice = dice.D8(6)

    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Crush(dice.D8(1)), special_properties=(CrushingEntanglement, ))]
    base_armor_class = 15
    morale = 12
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(5))
    no_appearing = AppearingSet(dice_dungeon=dice.D4(1, 1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    treasure_type = TreasureType.U
    xp = 500
