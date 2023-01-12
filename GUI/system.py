# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'system.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QGridLayout,
                               QGroupBox, QHeaderView, QLabel, QSizePolicy,
                               QTableView, QVBoxLayout, QWidget)

from HardwareMonitor import Monitor
from .list_model import List_Model
from itertools import zip_longest


class Ui_system_tab(object):
    def setupUi(self, system):
        if not system.objectName():
            system.setObjectName(u"system")
        system.resize(960, 540)
        self.verticalLayout = QVBoxLayout(system)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.system_info = QGroupBox(system)
        self.system_info.setObjectName(u"system_info")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_info.sizePolicy().hasHeightForWidth())
        self.system_info.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.system_info.setFont(font)
        self.gridLayout = QGridLayout(self.system_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.os = QLabel(self.system_info)
        self.os.setObjectName(u"os")

        self.gridLayout.addWidget(self.os, 0, 0, 1, 1)

        self.release = QLabel(self.system_info)
        self.release.setObjectName(u"release")

        self.gridLayout.addWidget(self.release, 1, 0, 1, 1)

        self.version = QLabel(self.system_info)
        self.version.setObjectName(u"version")

        self.gridLayout.addWidget(self.version, 2, 0, 1, 1)

        self.hostname = QLabel(self.system_info)
        self.hostname.setObjectName(u"hostname")

        self.gridLayout.addWidget(self.hostname, 0, 1, 1, 1)

        self.uptime = QLabel(self.system_info)
        self.uptime.setObjectName(u"uptime")

        self.gridLayout.addWidget(self.uptime, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.system_info)

        self.process_list = QTableView(system)
        self.process_list.setObjectName(u"process_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.process_list.sizePolicy().hasHeightForWidth())
        self.process_list.setSizePolicy(sizePolicy1)
        self.process_list.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.process_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.process_list.setDragDropOverwriteMode(False)
        self.process_list.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.process_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.process_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.process_list.setGridStyle(Qt.SolidLine)
        self.process_list.setSortingEnabled(True)
        self.process_list.horizontalHeader().setMinimumSectionSize(12)
        self.process_list.horizontalHeader().setDefaultSectionSize(18)
        self.process_list.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.process_list)

        self.retranslateUi(system)

        QMetaObject.connectSlotsByName(system)
    # setupUi

    def retranslateUi(self, system):
        system.setWindowTitle(QCoreApplication.translate("system", u"Form", None))
        self.system_info.setTitle("")
        self.os.setText(QCoreApplication.translate("system", u"Operating system: ", None))
        self.release.setText(QCoreApplication.translate("system", u"Release: ", None))
        self.version.setText(QCoreApplication.translate("system", u"Version: ", None))
        self.hostname.setText(QCoreApplication.translate("system", u"Hostname: ", None))
        self.uptime.setText(QCoreApplication.translate("system", u"Uptime: ", None))
    # retranslateUi


class system_tab(QWidget, Ui_system_tab):
    def __init__(self, parent=None):
        super(system_tab, self).__init__(parent)
        self.setupUi(self)
        self._monitor = Monitor()

        self.os.setText(f'{self.os.text().split(": ")[0]}: {self._monitor.data.system.os}')
        self.release.setText(f'{self.release.text().split(": ")[0]}: {self._monitor.data.system.release}')
        self.version.setText(f'{self.version.text().split(": ")[0]}: {self._monitor.data.system.version}')
        self.hostname.setText(f'{self.hostname.text().split(": ")[0]}: {self._monitor.data.system.hostname}')

        self.process_list.horizontalHeader().setStretchLastSection(True)
        self.process_list.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self._model = List_Model(list(self._monitor.data.system.process_list.values()),
                                 horizontal_header=["Name", "PID", "Path"])
        self.process_list.setModel(self._model)

    def draw(self):
        self.uptime.setText(
            f'{self.uptime.text().split(": ")[0]}: {str(self._monitor.data.system.boot_time).split(".")[0]}')
        ui_pids = {self._model.data(self._model.index(x, 1)) for x in range(self._model.rowCount())}
        active_pids = set(self._monitor.data.system.process_list.keys())
        remove = (
        self._model.match(self._model.index(0, 1), Qt.ItemDataRole.DisplayRole, x, 1, Qt.MatchFlag.MatchExactly) for x
        in ui_pids.difference(active_pids))
        add = active_pids.difference(ui_pids)
        for x, y in zip_longest(remove, add):
            if x:
                self._model.removeRow(x[0].row())
            if y:
                self._model.insertRow(self._model.rowCount(), rowData=self._monitor.data.system.process_list[y])
