import dice
import restrictions
from characters import abilityscores
from characters.classes import Level, LevelTable
from characters.classes.base import CharacterClass
from characters.savingthrows import SavingThrowSet


class Fighter(CharacterClass):
    name = "Fighter"
    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(strength=9)
        ),
    )
    level_table = LevelTable(
        levels=(
            Level(
                value=1,
                attack_bonus=1,
                experience_required=0,
                hit_dice=dice.D8(1),
                saving_throws_set=SavingThrowSet(
                    death_poison=12,
                    dragon_breath=15,
                    paralysis_stone=14,
                    spells=17,
                    wands=13
                )
            ),
            Level(
                value=2,
                attack_bonus=1,
                experience_required=2000,
                hit_dice=dice.D8(2),
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=15,
                    paralysis_stone=14,
                    spells=16,
                    wands=12
                ),
            ),
            Level(
                value=3,
                attack_bonus=1,
                experience_required=4000,
                hit_dice=dice.D8(3),
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=15,
                    paralysis_stone=14,
                    spells=16,
                    wands=12
                ),
            ),
            Level(
                value=4,
                attack_bonus=3,
                experience_required=8000,
                hit_dice=dice.D8(4),
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=14,
                    paralysis_stone=13,
                    spells=15,
                    wands=11
                ),
            ),
            Level(
                value=5,
                attack_bonus=4,
                experience_required=16000,
                hit_dice=dice.D8(5),
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=14,
                    paralysis_stone=13,
                    spells=15,
                    wands=11
                ),
            ),
            Level(
                value=6,
                attack_bonus=4,
                experience_required=32000,
                hit_dice=dice.D8(6),
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=14,
                    paralysis_stone=12,
                    spells=15,
                    wands=11
                ),
            ),
            Level(
                value=7,
                attack_bonus=5,
                experience_required=64000,
                hit_dice=dice.D8(7),
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=14,
                    paralysis_stone=12,
                    spells=15,
                    wands=11
                ),
            ),
            Level(
                value=8,
                attack_bonus=6,
                experience_required=120000,
                hit_dice=dice.D8(8),
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=13,
                    paralysis_stone=12,
                    spells=14,
                    wands=10
                ),
            ),
            Level(
                value=9,
                attack_bonus=6,
                experience_required=240000,
                hit_dice=dice.D8(9),
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=13,
                    paralysis_stone=12,
                    spells=14,
                    wands=10
                ),
            ),
            Level(
                value=10,
                attack_bonus=6,
                experience_required=360000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=2,
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=12,
                    paralysis_stone=11,
                    spells=13,
                    wands=9
                ),
            ),
            Level(
                value=11,
                attack_bonus=7,
                experience_required=480000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=4,
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=12,
                    paralysis_stone=11,
                    spells=13,
                    wands=9
                ),
            ),
            Level(
                value=12,
                attack_bonus=7,
                experience_required=600000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=6,
                saving_throws_set=SavingThrowSet(
                    death_poison=8,
                    dragon_breath=12,
                    paralysis_stone=10,
                    spells=13,
                    wands=9
                ),
            ),
            Level(
                value=13,
                attack_bonus=8,
                experience_required=720000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=8,
                saving_throws_set=SavingThrowSet(
                    death_poison=8,
                    dragon_breath=12,
                    paralysis_stone=10,
                    spells=13,
                    wands=9
                ),
            ),
            Level(
                value=14,
                attack_bonus=8,
                experience_required=840000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=10,
                saving_throws_set=SavingThrowSet(
                    death_poison=7,
                    dragon_breath=11,
                    paralysis_stone=10,
                    spells=12,
                    wands=8
                ),
            ),
            Level(
                value=15,
                attack_bonus=8,
                experience_required=960000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=12,
                saving_throws_set=SavingThrowSet(
                    death_poison=7,
                    dragon_breath=11,
                    paralysis_stone=10,
                    spells=12,
                    wands=8
                ),
            ),
            Level(
                value=16,
                attack_bonus=9,
                experience_required=1080000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=14,
                saving_throws_set=SavingThrowSet(
                    death_poison=7,
                    dragon_breath=10,
                    paralysis_stone=9,
                    spells=11,
                    wands=7
                ),
            ),
            Level(
                value=17,
                attack_bonus=9,
                experience_required=1200000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=16,
                saving_throws_set=SavingThrowSet(
                    death_poison=7,
                    dragon_breath=10,
                    paralysis_stone=9,
                    spells=11,
                    wands=7
                ),
            ),
            Level(
                value=18,
                attack_bonus=10,
                experience_required=1320000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=18,
                saving_throws_set=SavingThrowSet(
                    death_poison=6,
                    dragon_breath=10,
                    paralysis_stone=8,
                    spells=11,
                    wands=7
                ),
            ),
            Level(
                value=19,
                attack_bonus=10,
                experience_required=1440000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=20,
                saving_throws_set=SavingThrowSet(
                    death_poison=6,
                    dragon_breath=10,
                    paralysis_stone=8,
                    spells=11,
                    wands=7
                ),
            ),
            Level(
                value=20,
                attack_bonus=10,
                experience_required=1560000,
                hit_dice=dice.D8(9),
                hit_dice_flat_bonus=22,
                saving_throws_set=SavingThrowSet(
                    death_poison=5,
                    dragon_breath=9,
                    paralysis_stone=8,
                    spells=10,
                    wands=6
                ),
            )
        )
    )
