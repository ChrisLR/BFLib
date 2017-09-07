import restrictions
from characters import abilityscores
from characters.classes import Level, LevelTable
from characters.classes.base import CharacterClass
from characters import specialabilities
from characters.savingthrows import SavingThrowSet
from items import weapons
import dice
from spells import SpellSlotSet


class Cleric(CharacterClass):
    name = "Cleric"
    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(wisdom=9)
        ),
        weapons=restrictions.WeaponRestrictionSet(
            included=(
                weapons.types.Club,
                weapons.types.Mace,
                weapons.types.Maul,
                weapons.types.Quarterstaff,
                weapons.types.Sling,
                weapons.types.Warhammer
            )
        )
    )
    special_abilities = specialabilities.SpecialAbilitySet(
        special_abilities=(
            specialabilities.DivineCaster,
            specialabilities.TurnUndead
        )
    )
    level_table = LevelTable(
        levels=[
            Level(
                value=1,
                attack_bonus=1,
                experience_required=0,
                hit_dice=dice.D6(1),
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=16,
                    paralysis_stone=14,
                    spells=15,
                    wands=12
                )
            ),
            Level(
                value=2,
                attack_bonus=1,
                experience_required=1500,
                hit_dice=dice.D6(2),
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=15,
                    paralysis_stone=13,
                    spells=14,
                    wands=11
                ),
                spell_slots_set=SpellSlotSet(level_1=1)
            ),
            Level(
                value=3,
                attack_bonus=2,
                experience_required=3000,
                hit_dice=dice.D6(3),
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=15,
                    paralysis_stone=13,
                    spells=14,
                    wands=11
                ),
                spell_slots_set=SpellSlotSet(level_1=2)
            ),
            Level(
                value=4,
                attack_bonus=2,
                experience_required=6000,
                hit_dice=dice.D6(4),
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=15,
                    paralysis_stone=13,
                    spells=14,
                    wands=10
                ),
                spell_slots_set=SpellSlotSet(level_1=2, level_2=1)
            ),
        ]
    )
