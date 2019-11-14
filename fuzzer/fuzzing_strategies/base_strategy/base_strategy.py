import abc
from datetime import datetime
from random import Random


class Abstract_Strategy(metaclass=abc.ABCMeta):
    def __init__(self, seed=datetime.now().microsecond):
        self._random = Random(seed)
        self.seed = seed

    @abc.abstractmethod
    def generate(self):
        pass
