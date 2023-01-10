import sys
from collections import deque
from itertools import repeat
try:
    from pyadl import *
except:
    from GPUtil import getGPUs

class _Generic(object):
    def __init__(self):
        self.plot_data = deque(list(repeat(0, 60)), 60)
        self.name = None
        self.vram_total = None
        self.vram_free = None
        self.vram_used = None
        self.vram_usage = None
        self.load = None
        self.temperature = None

class _AMD(_Generic):
    def __init__(self):
        super(_AMD, self).__init__()
        device = ADLManager.getInstance().getDevices()[0]
        self.brand = "AMD"
        self.name = device.adapterName

    def update(self):
        device = ADLManager.getInstance().getDevices()[0]
        self.load = device.getCurrentUsage()
        self.temperature = round(device.getCurrentTemperature())
        self.plot_data.appendleft(self.load)

class _NVIDIA(_Generic):
    def __init__(self):
        super(_NVIDIA, self).__init__()
        device = getGPUs()[0]
        self.brand = "NVIDIA"
        self.name = device.name

    def update(self):
        device = getGPUs()[0]
        self.load = round(device.load * 100)
        self.temperature = round(device.temperature)
        self.plot_data.appendleft(self.load)

class GPU:
    _brands = dict(AMD=_AMD, NVIDIA=_NVIDIA)

    def __new__(cls, *args, **kwargs):
        brand = cls.__get_brand()
        return cls._brands.get(brand)() if cls.__get_brand() in cls._brands.keys() else None

    @staticmethod
    def __get_brand():
        if "pyadl" in sys.modules:
            return "AMD" if len(ADLManager.getInstance().getDevices()) > 0 else None
        else:
            return "NVIDIA" if len(getGPUs()) > 0 else None