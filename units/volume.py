import abc

from units.base import Unit


class VolumeUnit(Unit):
    __metaclass__ = abc.ABCMeta


class CubicFeet(VolumeUnit):
    pass
