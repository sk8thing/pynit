from collections import deque
from enum import StrEnum
from itertools import repeat
from platform import system
from psutil import virtual_memory
OS = system().lower()

if OS == "windows":
    from winstats import get_perf_data as get_perf
    from .perfmons import Perfmon

class _Generic(object):
    def __init__(self):
        self.plot_data = deque(list(repeat(0, 60)), 60)
        self.comp_data = dict()
        info = virtual_memory()
        self.installed = round(info.total * 9.537 * 1e-7)
        self.total = round(info.total * 9.31 * 1e-7)
        self.used = None
        self.usage = None
        self.available = None
        self.free = None
        self.standby = None
        self.modified = None

class _Linux(_Generic):
    def __init__(self):
        super(_Linux, self).__init__()

    def update(self):
        pass

class _Windows(_Generic):
    def __init__(self):
        super(_Windows, self).__init__()

    def update(self):
        info = virtual_memory()
        self.usage = round(info.percent)
        self.used = round(info.used * 9.31 * 1e-7)
        self.available = round(info.available * 9.537 * 1e-7)
        self.free = round(get_perf(Perfmon.FREE_MEMORY, delay=50)[0] * 9.537 * 1e-7)
        self.modified = round(get_perf(Perfmon.MODIFIED_MEMORY, delay=50)[0] * 9.537 * 1e-7)
        self.standby = self.available - self.free
        self.plot_data.appendleft(self.usage)
        self.comp_data = {
            "In use": self.used,
            "Modified": self.modified,
            "Standby": self.standby,
            "Free": self.free
        }

class RAM:
    _platforms = dict(windows=_Windows, linux=_Linux)

    def __new__(cls, *args, **kwargs):
        if OS not in cls._platforms.keys():
            raise NotImplementedError("Your operating system is not supported.")
        else:
            return cls._platforms.get(OS)()