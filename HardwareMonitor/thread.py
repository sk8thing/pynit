import sys
import traceback
from PySide6.QtCore import QObject, Signal, QRunnable, Slot, QThreadPool, QTimer

class Worker_Signals(QObject):
    tick = Signal()
    error = Signal(tuple)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self._fn = fn
        self._args = args
        self._kwargs = kwargs
        self.signals = Worker_Signals()

    @Slot()
    def run(self):
        try:
            self._fn(*self._args, **self._kwargs)
        except:
            traceback.print_exc()
            exec_type, value = sys.exc_info()[:2]
            self.signals.error.emit((exec_type, value, traceback.format_exc()))
        else:
            try:
                self.signals.tick.emit()
            except RuntimeError:
                self.autoDelete()

class Worker_Thread(QThreadPool):
    def __init__(self, fn):
        super(Worker_Thread, self).__init__()
        self.callback = None
        self._job = fn
        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self.__execute)
        self._timer.start()

    def __del__(self):
        self._timer.stop()
        self.clear()

    def __execute(self):
        work = Worker(self._job)
        if callable(self.callback):
            work.signals.tick.connect(self.callback)
        self.start(work)