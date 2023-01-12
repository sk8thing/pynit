# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QAbstractItemView, QHeaderView, QSizePolicy,
                               QTableView, QVBoxLayout, QWidget)

from pyqtgraph import BarGraphItem
from HardwareData import to_units, readable
from HardwareMonitor import Monitor
from .list_model import List_Model
from .plot import Plot


class Ui_disk_tab(object):
    def setupUi(self, disk_tab):
        if not disk_tab.objectName():
            disk_tab.setObjectName(u"disk_tab")
        disk_tab.resize(960, 540)
        self.verticalLayout = QVBoxLayout(disk_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.part_list = QTableView(disk_tab)
        self.part_list.setObjectName(u"part_list")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.part_list.sizePolicy().hasHeightForWidth())
        self.part_list.setSizePolicy(sizePolicy)
        self.part_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.part_list.setTabKeyNavigation(True)
        self.part_list.setProperty("showDropIndicator", True)
        self.part_list.setDragDropOverwriteMode(True)
        self.part_list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.part_list.setCornerButtonEnabled(False)

        self.verticalLayout.addWidget(self.part_list)

        self.comp_plot = Plot(disk_tab, grid=False)
        self.comp_plot.setObjectName(u"comp_plot")
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comp_plot.sizePolicy().hasHeightForWidth())
        self.comp_plot.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.comp_plot)

        self.disk_list = QTableView(disk_tab)
        self.disk_list.setObjectName(u"disk_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.disk_list.sizePolicy().hasHeightForWidth())
        self.disk_list.setSizePolicy(sizePolicy1)
        self.disk_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.disk_list.setTabKeyNavigation(True)
        self.disk_list.setProperty("showDropIndicator", True)
        self.disk_list.setDragDropOverwriteMode(True)
        self.disk_list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.disk_list.setCornerButtonEnabled(False)

        self.verticalLayout.addWidget(self.disk_list)

        self.retranslateUi(disk_tab)

        QMetaObject.connectSlotsByName(disk_tab)
    # setupUi

    def retranslateUi(self, disk_tab):
        disk_tab.setWindowTitle(QCoreApplication.translate("disk_tab", u"Form", None))
    # retranslateUi


class disk_tab(QWidget, Ui_disk_tab):
    def __init__(self):
        super(disk_tab, self).__init__()
        self.setupUi(self)

        self._monitor = Monitor()
        self.part_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.part_list.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._model_part = List_Model(list(self._monitor.data.disk.partitions.values()),
                                      vertical_header=list(self._monitor.data.disk.partitions.keys()),
                                      horizontal_header=["Total", "Used", "Free", "Usage[%]", "Format"])
        self.part_list.setModel(self._model_part)

        self.disk_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.disk_list.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self._model_disk = List_Model(list(self._monitor.data.disk.disks.values()),
                                      vertical_header=list(self._monitor.data.disk.disks.keys()),
                                      horizontal_header=["Read Speed", "Write Speed"])
        self.disk_list.setModel(self._model_disk)

        self.comp_plot.plotItem.hideAxis("bottom")
        self.comp_plot.plotItem.hideAxis("left")
        self.comp_plot.plotItem.setYRange(0, 0.1)
        bars = list()
        bars.append(BarGraphItem(x0=[0], height=[0.1], width=self._monitor.data.disk.total_used, pen=(50, 50, 200),
                                 brush=(50, 50, 200, 100)))
        bars.append(
            BarGraphItem(x0=[bars[0].boundingRect().width()], height=[0.1], width=self._monitor.data.disk.total_free,
                         pen=(50, 50, 200),
                         brush=(200, 200, 200, 100)))
        bars[0].setToolTip(
            f'Total used space: {to_units(self._monitor.data.disk.total_used, decimals=1, offset=-3, suffix="B")}')
        bars[1].setToolTip(
            f'Total free space: {to_units(self._monitor.data.disk.total_free, decimals=1, offset=-3, suffix="B")}')
        for bar in bars:
            self.comp_plot.plotItem.addItem(bar)

    def draw(self):
        l = list(self._monitor.data.disk.disks.values())
        for x in range(self._model_disk.rowCount()):
            for y in range(self._model_disk.columnCount()):
                self._model_disk.setData(self._model_disk.index(x, y), f'{readable(l[x][y]).replace("B", "")}B/s')
