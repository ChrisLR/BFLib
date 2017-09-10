import abc


class ItemComponent(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def NAME(self):
        pass
