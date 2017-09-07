import abc
import random


class Dice(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def sides(self):
        pass

    def __init__(self, amount):
        self.amount = amount

    def roll(self):
        return sum((random.randint(1, self.sides) for _ in range(0, self.amount)))


class D1(Dice):
    sides = 1


class D4(Dice):
    sides = 4


class D6(Dice):
    sides = 6


class D8(Dice):
    sides = 8


class D10(Dice):
    sides = 10


class D12(Dice):
    sides = 12


class D20(Dice):
    sides = 20
