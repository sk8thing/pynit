from enum import StrEnum
from platform import system, machine
from itertools import repeat
from collections import deque
from psutil import cpu_count, pids
from .cpuinfo import cpu as cpuinfo
OS = system().lower()

if OS == "windows":
    from winstats import get_perf_data as get_perf
    from .perfmons import Perfmon

class _Generic(object):
    def __init__(self):
        self.plot_data = deque(list(repeat(0, 60)), 60)
        self.brand = cpuinfo.info[0]["ProcessorNameString"]
        self.arch = machine()
        self.cores = cpu_count(logical=False)
        self.logical = cpu_count()
        self.base_clk = None
        self.pkg_clk = None
        self.pkg_usage = None
        self.processes = None
        self.threads = None
        self.temp_celsius = None
        self.temp_fahrenheit = None

class _Linux(_Generic):
    def __init__(self):
        super(_Linux, self).__init__()

    def update(self):
        pass

class _Windows(_Generic):
    def __init__(self):
        super(_Windows, self).__init__()
        self.base_clk = get_perf(Perfmon.BASE_CLK, delay=1)[0]

    def update(self):
        self.pkg_clk = round((get_perf(Perfmon.PERFORMANCE, delay=300, fmts="double")[0] / 100) * self.base_clk)
        self.pkg_usage = round(get_perf(Perfmon.USAGE, delay=400, fmts="double")[0])
        self.threads = get_perf(Perfmon.THREADS, delay=50)[0]
        self.processes = len(pids())
        temperature = get_perf(Perfmon.CPU_TEMP, delay=50)[0]
        self.temp_celsius = round(temperature - 273.15)
        self.temp_fahrenheit = round((temperature * 9 / 5) - 459.67)
        self.plot_data.appendleft(self.pkg_usage)

class CPU:
    _platforms = dict(windows=_Windows, linux=_Linux)

    def __new__(cls, *args, **kwargs):
        if OS not in cls._platforms.keys():
            raise NotImplementedError("Your operating system is not supported.")
        else:
            return cls._platforms.get(OS)()