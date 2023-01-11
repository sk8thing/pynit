from HardwareData import Data
from .thread import Worker_Thread

class Monitor:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Monitor, cls).__new__(cls)
            cls._instance.data = Data()
            cls._instance.worker = Worker_Thread(cls._instance.data.update)
        return cls._instance
