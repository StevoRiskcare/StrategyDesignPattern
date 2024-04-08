import abc


class AbsStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_fee(self):
        pass