from platform import system
from psutil import pids, Process
OS = system().lower()

class _Generic(object):
    def __init__(self):
        pass

class _Linux(_Generic):
    def __init__(self):
        super(_Linux, self).__init__()

    def update(self):
        pass

class _Windows(_Generic):
    def __init__(self):
        super(_Windows, self).__init__()

    def update(self):
        pass

class System:
    _platforms = dict(windows=_Windows, linux=_Linux)

    def __new__(cls, *args, **kwargs):
        if OS not in cls._platforms.keys():
            raise NotImplementedError("Your operating system is not supported.")
        else:
            return cls._platforms.get(OS)()