import abc

class Abstract_Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate(self):
        pass
