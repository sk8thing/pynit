from HardwareData import Data
from .thread import Worker_Thread

class Monitor:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Monitor, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = Data()
        self.worker = Worker_Thread(self.data.update)
