# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ram.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
                               QSizePolicy, QVBoxLayout, QWidget, QGraphicsView, QToolTip)

from .plot import Plot
from pyqtgraph import BarGraphItem
from itertools import repeat
from HardwareMonitor import Monitor
from HardwareData import to_units

class Ui_ram_tab(object):
    def setupUi(self, ram):
        if not ram.objectName():
            ram.setObjectName(u"ram")
        ram.resize(960, 540)
        self.verticalLayout = QVBoxLayout(ram)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ram_plot = Plot(ram, limits=((0, 60), (0, 100)))
        self.ram_plot.setObjectName(u"ram_plot")

        self.verticalLayout.addWidget(self.ram_plot)

        self.comp_plot = Plot(ram, grid=False)
        self.comp_plot.setObjectName(u"comp_plot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comp_plot.sizePolicy().hasHeightForWidth())
        self.comp_plot.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.comp_plot)

        self.ram_info = QGroupBox(ram)
        self.ram_info.setObjectName(u"ram_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ram_info.sizePolicy().hasHeightForWidth())
        self.ram_info.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.ram_info.setFont(font)
        self.gridLayout = QGridLayout(self.ram_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.usage = QLabel(self.ram_info)
        self.usage.setObjectName(u"usage")
        font1 = QFont()
        font1.setPointSize(18)
        self.usage.setFont(font1)

        self.gridLayout.addWidget(self.usage, 0, 0, 1, 1)

        self.ram_details = QGroupBox(self.ram_info)
        self.ram_details.setObjectName(u"ram_details")
        sizePolicy1.setHeightForWidth(self.ram_details.sizePolicy().hasHeightForWidth())
        self.ram_details.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.ram_details)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.available = QLabel(self.ram_details)
        self.available.setObjectName(u"available")

        self.verticalLayout_2.addWidget(self.available)

        self.standby = QLabel(self.ram_details)
        self.standby.setObjectName(u"standby")

        self.verticalLayout_2.addWidget(self.standby)

        self.modified = QLabel(self.ram_details)
        self.modified.setObjectName(u"modified")

        self.verticalLayout_2.addWidget(self.modified)

        self.free = QLabel(self.ram_details)
        self.free.setObjectName(u"free")

        self.verticalLayout_2.addWidget(self.free)


        self.gridLayout.addWidget(self.ram_details, 0, 1, 3, 1)

        self.total = QLabel(self.ram_info)
        self.total.setObjectName(u"total")
        self.total.setFont(font1)

        self.gridLayout.addWidget(self.total, 1, 0, 1, 1)

        self.in_use = QLabel(self.ram_info)
        self.in_use.setObjectName(u"in_use")
        self.in_use.setFont(font1)

        self.gridLayout.addWidget(self.in_use, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.ram_info)


        self.retranslateUi(ram)

        QMetaObject.connectSlotsByName(ram)
    # setupUi

    def retranslateUi(self, ram):
        ram.setWindowTitle(QCoreApplication.translate("ram", u"Form", None))
        self.ram_info.setTitle("")
        self.usage.setText(QCoreApplication.translate("ram", u"Usage: ", None))
        self.ram_details.setTitle("")
        self.available.setText(QCoreApplication.translate("ram", u"Available: ", None))
        self.standby.setText(QCoreApplication.translate("ram", u"Standby: ", None))
        self.modified.setText(QCoreApplication.translate("ram", u"Modified/Swap: ", None))
        self.free.setText(QCoreApplication.translate("ram", u"Free/Inactive: ", None))
        self.total.setText(QCoreApplication.translate("ram", u"Total: ", None))
        self.in_use.setText(QCoreApplication.translate("ram", u"In use: ", None))
    # retranslateUi

class ram_tab(QWidget, Ui_ram_tab):
    def __init__(self, parent=None):
        super(ram_tab, self).__init__(parent)
        self.setupUi(self)

        self._monitor = Monitor()
        self.total.setText(
            f'{self.total.text().split(": ")[0]}: {to_units(self._monitor.data.memory.total, offset=-6, decimals=1, suffix="B")}')
        self.ram_plot.plotItem.invertX(True)
        self.ram_plot.plotItem.setLabel("bottom", "Time", units="seconds", **self.ram_plot.style)
        self.ram_plot.plotItem.setLabel("left", "RAM Usage", units="%", **self.ram_plot.style)
        self.data_line = self.ram_plot.plot(range(60), list(repeat(0, 60)), 60, pen=(50, 50, 200), fillLevel=0,
                                                brush=(50, 50, 200, 100))

        self.comp_plot.plotItem.hideAxis("bottom")
        self.comp_plot.plotItem.hideAxis("left")
        self.comp_plot.plotItem.setYRange(0, 0.1)
        self.bars = list()
        for x in range(4):
            self.bars.append(BarGraphItem(x0=[0], height=[0], width=0, pen=(50, 50, 200), brush=(50 + 50 * x, 50 + 50 * x, 200, 100)))
            self.comp_plot.plotItem.addItem(self.bars[x])

    def draw(self):
        self.data_line.setData(range(60), self._monitor.data.memory.plot_data)
        self.usage.setText(f'{self.usage.text().split(": ")[0]}: {self._monitor.data.memory.usage}%')
        self.in_use.setText(
            f'{self.in_use.text().split(": ")[0]}: {to_units(self._monitor.data.memory.used, offset=-6, decimals=1, suffix="B")}')
        self.available.setText(f'{self.available.text().split(": ")[0]}: {self._monitor.data.memory.available}MB')
        self.modified.setText(f'{self.modified.text().split(": ")[0]}: {self._monitor.data.memory.modified}MB')
        self.standby.setText(f'{self.standby.text().split(": ")[0]}: {self._monitor.data.memory.standby}MB')
        self.free.setText(f'{self.free.text().split(": ")[0]}: {self._monitor.data.memory.free}MB')

        for index, key in enumerate(self._monitor.data.memory.comp_data):
            value = self._monitor.data.memory.comp_data[key]
            self.bars[index].setOpts(
                x0=[self.bars[index - 1 or 0].boundingRect().width() + self.bars[index - 1 or 0].boundingRect().left()],
                height=[0.1], width=value)
            self.bars[index].setToolTip(f'{key}: {value}MB')

