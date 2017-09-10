import abc


class Attack(object):
    name = ""
    __metaclass__ = abc.ABCMeta


class WeaponAttack(Attack):
    name = "Weapon"


class NaturalAttack(Attack):
    __metaclass__ = abc.ABCMeta
    __slots__ = ["damage_dice", "damage_bonus"]
    name = ""

    def __init__(self, damage_dice, damage_bonus=0):
        self.damage_dice = damage_dice
        self.damage_bonus = damage_bonus


class Bite(NaturalAttack):
    name = "Bite"


class Claw(NaturalAttack):
    name = "Claw"


class Hoof(NaturalAttack):
    name = "Hoof"


class AttackSet(object):
    __slots__ = ["amount", "attack", "special_properties"]

    def __init__(self, attack, amount=1, special_properties=None):
        self.amount = amount  # type: int
        self.attack = attack  # type :
        self.special_properties = special_properties
