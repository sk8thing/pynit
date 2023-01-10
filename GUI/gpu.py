# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gpu.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

from .plot import Plot
from itertools import repeat
from HardwareMonitor import Monitor


class Ui_gpu_tab(object):
    def setupUi(self, gpu_tab):
        if not gpu_tab.objectName():
            gpu_tab.setObjectName(u"gpu_tab")
        gpu_tab.resize(960, 540)
        self.verticalLayout = QVBoxLayout(gpu_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gpu_plot = Plot(gpu_tab, limits=((0, 60), (0, 100)))
        self.gpu_plot.setObjectName(u"gpu_plot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpu_plot.sizePolicy().hasHeightForWidth())
        self.gpu_plot.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.gpu_plot)

        self.gpu_info = QGroupBox(gpu_tab)
        self.gpu_info.setObjectName(u"gpu_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gpu_info.sizePolicy().hasHeightForWidth())
        self.gpu_info.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(18)
        self.gpu_info.setFont(font)
        self.gridLayout = QGridLayout(self.gpu_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gpu_details = QGroupBox(self.gpu_info)
        self.gpu_details.setObjectName(u"gpu_details")
        font1 = QFont()
        font1.setPointSize(12)
        self.gpu_details.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.gpu_details)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chipset = QLabel(self.gpu_details)
        self.chipset.setObjectName(u"chipset")

        self.verticalLayout_2.addWidget(self.chipset)

        self.name = QLabel(self.gpu_details)
        self.name.setObjectName(u"name")

        self.verticalLayout_2.addWidget(self.name)


        self.gridLayout.addWidget(self.gpu_details, 0, 1, 2, 1)

        self.load = QLabel(self.gpu_info)
        self.load.setObjectName(u"load")

        self.gridLayout.addWidget(self.load, 0, 0, 1, 1)

        self.temperature = QLabel(self.gpu_info)
        self.temperature.setObjectName(u"temperature")

        self.gridLayout.addWidget(self.temperature, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.gpu_info)


        self.retranslateUi(gpu_tab)

        QMetaObject.connectSlotsByName(gpu_tab)
    # setupUi

    def retranslateUi(self, gpu_tab):
        gpu_tab.setWindowTitle(QCoreApplication.translate("gpu_tab", u"Form", None))
        self.gpu_info.setTitle("")
        self.gpu_details.setTitle("")
        self.chipset.setText(QCoreApplication.translate("gpu_tab", u"Chipset: ", None))
        self.name.setText(QCoreApplication.translate("gpu_tab", u"Graphics card: ", None))
        self.load.setText(QCoreApplication.translate("gpu_tab", u"Usage: ", None))
        self.temperature.setText(QCoreApplication.translate("gpu_tab", u"Temperature: ", None))
    # retranslateUi

class gpu_tab(QWidget, Ui_gpu_tab):
    def __init__(self, parent=None):
        super(gpu_tab, self).__init__(parent)
        self.setupUi(self)

        self._monitor = Monitor()
        if self._monitor.data.gpu is not None:
            self.chipset.setText(f'{self.chipset.text().split(": ")[0]}: {self._monitor.data.gpu.brand}')
            self.name.setText(f'{self.name.text().split(": ")[0]}: {self._monitor.data.gpu.name}')

            self.gpu_plot.plotItem.invertX(True)
            self.gpu_plot.plotItem.setLabel("bottom", "Time", units="seconds", **self.gpu_plot.style)
            self.gpu_plot.plotItem.setLabel("left", "GPU Usage", units="%", **self.gpu_plot.style)
            self.data_line = self.gpu_plot.plot(range(60), list(repeat(0, 60)), 60, pen=(50, 50, 200), fillLevel=0,
                                                    brush=(50, 50, 200, 100))

    def draw(self):
        if self._monitor.data.gpu is not None:
            self.load.setText(f'{self.load.text().split(": ")[0]}: {self._monitor.data.gpu.load}%')
            self.temperature.setText(f'{self.temperature.text().split(": ")[0]}: {self._monitor.data.gpu.temperature}°C')
            self.data_line.setData(range(60), self._monitor.data.gpu.plot_data)
