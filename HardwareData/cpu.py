from platform import machine
from itertools import repeat
from collections import deque
from psutil import cpu_count, cpu_percent, cpu_freq, pids, Process, WINDOWS, LINUX
from .cpuinfo import cpu as cpuinfo
if WINDOWS:
    from winstats import get_perf_data as get_perf
    from .perfmons import Perfmon
elif LINUX:
    from psutil import sensors_temperatures

class _Generic(object):
    def __init__(self):
        self.plot_data = deque(list(repeat(0, 60)), 60)
        self.brand = None
        self.arch = machine()
        self.cores = cpu_count(logical=False)
        self.logical = cpu_count()
        self.base_clk = None
        self.pkg_clk = None
        self.pkg_usage = None
        self.processes = None
        self.threads = None
        self.temperature = None

class _Linux(_Generic):
    def __init__(self):
        super(_Linux, self).__init__()
        self.brand = cpuinfo.info[0]["model name"]
        self.base_clk = round(float(cpuinfo.info[0]["cpu MHz"]))

    def update(self):
        self.pkg_clk = round(cpu_freq(percpu=False).current)
        self.pkg_usage = round(cpu_percent(percpu=False))
        self.threads = self.__thread_count()
        self.processes = len(pids())
        self.temperature = round(sensors_temperatures()["coretemp"][0].current) if len(
            sensors_temperatures().items()) > 0 else 0
        self.plot_data.appendleft(self.pkg_usage)

    @staticmethod
    def __thread_count():
        result = 0
        for pid in pids():
            try:
                p = Process(pid)
                with p.oneshot():
                    result += p.num_threads()
            except:
                continue
        return result

class _Windows(_Generic):
    def __init__(self):
        super(_Windows, self).__init__()
        self.brand = cpuinfo.info[0]["ProcessorNameString"]
        self.base_clk = get_perf(Perfmon.BASE_CLK, delay=1)[0]

    def update(self):
        self.pkg_clk = round((get_perf(Perfmon.PERFORMANCE, delay=100, fmts="double")[0] / 100) * self.base_clk)
        self.pkg_usage = min(round(get_perf(Perfmon.USAGE, delay=200, fmts="double")[0]), 100)
        self.threads = get_perf(Perfmon.THREADS, delay=50)[0]
        self.processes = len(pids())
        temperature = get_perf(Perfmon.CPU_TEMP, delay=50)[0]
        self.temperature = round(temperature - 273.15)
        self.plot_data.appendleft(self.pkg_usage)

class CPU:
    _platforms = dict(windows=_Windows, linux=_Linux)

    def __new__(cls, os, *args, **kwargs):
        if os not in cls._platforms.keys():
            raise NotImplementedError("Your operating system is not supported.")
        else:
            return cls._platforms.get(os)()