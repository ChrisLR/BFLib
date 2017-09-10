import abc

from units.base import Unit


class SpeedUnit(Unit):
    __metaclass__ = abc.ABCMeta


class FeetPerGameTurn(SpeedUnit):
    pass