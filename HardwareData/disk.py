from itertools import repeat
from psutil import disk_partitions, disk_usage, disk_io_counters, WINDOWS
from psutil._common import bytes2human as readable

class Disk:
    def __init__(self):
        self.partitions = dict()
        self.disks = dict()
        self.total_free = 0
        self.total_used = 0
        self._prev_disks = dict()
        partitions = disk_partitions(all=False)
        for part in partitions:
            if WINDOWS and ("cdrom" in part.opts or part.fstype == ""):
                continue
            info = disk_usage(part.mountpoint)
            self.total_free += info.free / 1024
            self.total_used += info.used / 1024
            self.partitions.update({part.device: [readable(info.total), readable(info.used), readable(info.free),
                                                  info.percent, part.fstype]})
        disks = disk_io_counters(perdisk=True)
        for key, value in disks.items():
            self.disks.update({key: list(repeat(0, 2))})
            self._prev_disks.update({key: value})

    def update(self):
        disks = disk_io_counters(perdisk=True)
        for key, value in disks.items():
            self.disks.update({key: [value.read_bytes - self._prev_disks[key].read_bytes,
                                     value.write_bytes - self._prev_disks[key].write_bytes]})
            self._prev_disks.update({key: value})