# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
                               QLabel, QPushButton, QSizePolicy, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QTableView, QAbstractItemView)

from HardwareMonitor import Monitor
from .list_model import List_Model
from datetime import datetime
from itertools import repeat

class Ui_history_tab(object):
    def setupUi(self, history_tab):
        if not history_tab.objectName():
            history_tab.setObjectName(u"history_tab")
        history_tab.resize(960, 540)
        self.verticalLayout = QVBoxLayout(history_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list = QTableView(history_tab)
        self.list.setObjectName(u"list")
        self.list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.list.setCornerButtonEnabled(False)

        self.verticalLayout.addWidget(self.list)

        self.history_info = QGroupBox(history_tab)
        self.history_info.setObjectName(u"history_info")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_info.sizePolicy().hasHeightForWidth())
        self.history_info.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.history_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reset_button = QPushButton(self.history_info)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.reset_button.setFont(font)

        self.gridLayout.addWidget(self.reset_button, 0, 0, 1, 1)

        self.delta = QLabel(self.history_info)
        self.delta.setObjectName(u"delta")
        font1 = QFont()
        font1.setPointSize(18)
        self.delta.setFont(font1)
        self.delta.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.delta, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.history_info)


        self.retranslateUi(history_tab)

        QMetaObject.connectSlotsByName(history_tab)
    # setupUi

    def retranslateUi(self, history_tab):
        history_tab.setWindowTitle(QCoreApplication.translate("history_tab", u"Form", None))
        self.history_info.setTitle("")
        self.reset_button.setText(QCoreApplication.translate("history_tab", u"Reset Min/Max/Avg", None))
        self.delta.setText(QCoreApplication.translate("history_tab", u"Time since started: ", None))
    # retranslateUi


class history_tab(QWidget, Ui_history_tab):
    def __init__(self, parent=None):
        super(history_tab, self).__init__(parent)
        self.setupUi(self)
        self._monitor = Monitor()

        self._started = datetime.now()
        self.reset_button.clicked.connect(self.__reset)

        self.list.horizontalHeader().setStretchLastSection(True)
        self.list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.list.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self._model = List_Model([[0 for col in range(4)] for row in range(3)],
                                 ["CPU Usage[%]", "CPU Temperature[°C]", "Memory Usage[%]", "GPU Usage[%]", "GPU Temperature[°C]"],
                                 ["Current", "Min", "Max", "Avg"])
        self.list.setModel(self._model)
        if self._monitor.data.gpu is not None:
            self._model.insertRow(self._model.rowCount() - 1, rowData=[0 for x in range(4)])
            self._model.insertRow(self._model.rowCount() - 1, rowData=[0 for x in range(4)])

    def __reset(self):
        self._started = datetime.now()
        data = [self._monitor.data.cpu.pkg_usage, self._monitor.data.cpu.temperature, self._monitor.data.memory.usage]
        if self._monitor.data.gpu is not None:
            data.extend([self._monitor.data.gpu.load, self._monitor.data.gpu.temperature])
        for x in range(self._model.rowCount()):
            for y in range(self._model.columnCount()):
                index = self._model.index(x, y)
                self._model.setData(index, data[x])

    def draw(self):
        delta = datetime.now() - self._started
        self.delta.setText(f'{self.delta.text().split(": ")[0]}: {str(delta).split(".")[0]}')
        data = [self._monitor.data.cpu.pkg_usage, self._monitor.data.cpu.temperature, self._monitor.data.memory.usage]
        if self._monitor.data.gpu is not None:
            data.extend([self._monitor.data.gpu.load, self._monitor.data.gpu.temperature])
        for x in range(self._model.rowCount()):
            for y in range(self._model.columnCount()):
                index = self._model.index(x, y)
                if y == 0:
                    self._model.setData(index, data[x])
                elif y == 1:
                    self._model.setData(index, min(data[x], self._model.data(index) or data[x]))
                elif y == 2:
                    self._model.setData(index, max(data[x], self._model.data(index) or data[x]))
                elif y == 3:
                    self._model.setData(index, round(
                        ((self._model.data(index) * round(delta.total_seconds())) + data[x]) / (
                                    round(delta.total_seconds()) + 1)) or data[x])