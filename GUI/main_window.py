# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QTabWidget, QWidget)

from .resources import *
from HardwareMonitor import Monitor
from .cpu import cpu_tab
from .ram import ram_tab

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(960, 540))
        main_window.setSizeIncrement(QSize(16, 9))
        main_window.setBaseSize(QSize(960, 540))
        main_window.setTabletTracking(True)
        main_window.setFocusPolicy(Qt.NoFocus)
        main_window.setContextMenuPolicy(Qt.DefaultContextMenu)
        main_window.setWindowIcon(QIcon(":/icons/icon"))
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.horizontalLayout = QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tab_container = QTabWidget(self.central_widget)
        self.tab_container.setObjectName(u"tab_container")
        self.tab_container.setLayoutDirection(Qt.LeftToRight)
        self.tab_container.setTabPosition(QTabWidget.West)
        self.tab_container.setTabShape(QTabWidget.Rounded)
        self.tab_container.setElideMode(Qt.ElideNone)
        self.system_tab = QWidget()
        self.system_tab.setObjectName(u"system_tab")
        self.tab_container.addTab(self.system_tab, "")
        self.processor_tab = cpu_tab()
        self.processor_tab.setObjectName(u"processor_tab")
        self.tab_container.addTab(self.processor_tab, "")
        self.memory_tab = ram_tab()
        self.memory_tab.setObjectName(u"memory_tab")
        self.tab_container.addTab(self.memory_tab, "")

        self.horizontalLayout.addWidget(self.tab_container)

        main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(main_window)

        self.tab_container.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"<empty>", None))
        self.tab_container.setTabText(self.tab_container.indexOf(self.system_tab), QCoreApplication.translate("main_window", u"System", None))
        self.tab_container.setTabText(self.tab_container.indexOf(self.processor_tab), QCoreApplication.translate("main_window", u"CPU", None))
        self.tab_container.setTabText(self.tab_container.indexOf(self.memory_tab), QCoreApplication.translate("main_window", u"RAM", None))
    # retranslateUi

class main_window(QMainWindow, Ui_main_window):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        self.monitor = Monitor()
        self.monitor.worker.callback = self.draw

    def closeEvent(self, event):
        pass

    @Slot()
    def draw(self):
        self.processor_tab.draw()
        self.memory_tab.draw()