from .system import System
from .cpu import CPU
from .ram import RAM

class Data:
    def __init__(self):
        self.system = System()
        self.cpu = CPU()
        self.memory = RAM()
        self._data = set(x for x in list(self.__dict__.values()))

    def update(self):
        for x in self._data:
            update_ = getattr(x, "update", None)
            if callable(update_):
                update_()