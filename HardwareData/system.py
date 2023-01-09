from platform import system, release, version, platform, win32_edition, node
from re import match
from psutil import pids, Process, boot_time
import datetime

class _Generic(object):
    def __init__(self):
        self.boot_time = None
        self.release = None
        self.os = system()
        self.version = version()
        self.hostname = node()
        self.process_list = dict()
        self.update()

    def update(self):
        self.boot_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(boot_time())
        active = set(pids())
        add = active.difference(set(self.process_list.keys()))
        remove = set(self.process_list.keys()).difference(active)
        for pid in add:
            try:
                p = Process(pid)
                with p.oneshot():
                    name = p.name()
                    if name.strip() == "":
                        continue
                    self.process_list.update({pid: [name, pid, p.exe().strip()]})
            except:
                continue
        for pid in remove:
            del self.process_list[pid]


class _Linux(_Generic):
    def __init__(self):
        super(_Linux, self).__init__()
        self.release = release()

class _Windows(_Generic):
    def __init__(self):
        super(_Windows, self).__init__()
        self.release = self.__win32_release()

    @staticmethod
    def __win32_release():
        release_major = release() if not match("Windows-10-10.0.22[0-9]{3}", platform()) else "11"
        return f'{release_major} {win32_edition()}'

class System:
    _platforms = dict(windows=_Windows, linux=_Linux)

    def __new__(cls, os, *args, **kwargs):
        if os not in cls._platforms.keys():
            raise NotImplementedError("Your operating system is not supported.")
        else:
            return cls._platforms.get(os)()