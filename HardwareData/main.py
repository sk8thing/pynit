from platform import system
from .system import System
from .cpu import CPU
from .ram import RAM
from .gpu import GPU
from .disk import Disk

class Data:
    def __init__(self):
        os = system().lower()
        self.system = System(os)
        self.cpu = CPU(os)
        self.memory = RAM(os)
        self.disk = Disk()
        self.gpu = GPU()
        self._data = set(x for x in list(self.__dict__.values()))

    def update(self):
        for x in self._data:
            update_ = getattr(x, "update", None)
            if callable(update_):
                update_()