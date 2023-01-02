# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cpu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

from .plot import Plot

class Ui_cpu(object):
    def setupUi(self, cpu):
        if not cpu.objectName():
            cpu.setObjectName(u"cpu")
        cpu.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cpu.sizePolicy().hasHeightForWidth())
        cpu.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        cpu.setFont(font)
        cpu.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(cpu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cpu_plot = Plot(cpu)
        self.cpu_plot.setObjectName(u"cpu_plot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cpu_plot.sizePolicy().hasHeightForWidth())
        self.cpu_plot.setSizePolicy(sizePolicy1)
        self.cpu_plot.setFont(font)

        self.verticalLayout.addWidget(self.cpu_plot)

        self.cpu_info = QGroupBox(cpu)
        self.cpu_info.setObjectName(u"cpu_info")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cpu_info.sizePolicy().hasHeightForWidth())
        self.cpu_info.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        self.cpu_info.setFont(font1)
        self.gridLayout = QGridLayout(self.cpu_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.processes = QLabel(self.cpu_info)
        self.processes.setObjectName(u"processes")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setKerning(True)
        self.processes.setFont(font2)
        self.processes.setFrameShape(QFrame.NoFrame)
        self.processes.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.processes, 3, 0, 1, 1)

        self.threads = QLabel(self.cpu_info)
        self.threads.setObjectName(u"threads")
        self.threads.setFont(font2)
        self.threads.setFrameShape(QFrame.NoFrame)
        self.threads.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.threads, 4, 0, 1, 1)

        self.pkg_usage = QLabel(self.cpu_info)
        self.pkg_usage.setObjectName(u"pkg_usage")
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.pkg_usage.setFont(font3)
        self.pkg_usage.setFrameShape(QFrame.NoFrame)
        self.pkg_usage.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.pkg_usage, 0, 0, 1, 1)

        self.pkg_clk = QLabel(self.cpu_info)
        self.pkg_clk.setObjectName(u"pkg_clk")
        self.pkg_clk.setFont(font2)
        self.pkg_clk.setFrameShape(QFrame.NoFrame)
        self.pkg_clk.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.pkg_clk, 1, 0, 1, 1)

        self.cpu_details = QGroupBox(self.cpu_info)
        self.cpu_details.setObjectName(u"cpu_details")
        sizePolicy2.setHeightForWidth(self.cpu_details.sizePolicy().hasHeightForWidth())
        self.cpu_details.setSizePolicy(sizePolicy2)
        self.cpu_details.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.cpu_details)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.processor = QLabel(self.cpu_details)
        self.processor.setObjectName(u"processor")

        self.verticalLayout_2.addWidget(self.processor)

        self.arch = QLabel(self.cpu_details)
        self.arch.setObjectName(u"arch")

        self.verticalLayout_2.addWidget(self.arch)

        self.base_clk = QLabel(self.cpu_details)
        self.base_clk.setObjectName(u"base_clk")

        self.verticalLayout_2.addWidget(self.base_clk)

        self.cores = QLabel(self.cpu_details)
        self.cores.setObjectName(u"cores")

        self.verticalLayout_2.addWidget(self.cores)

        self.logical = QLabel(self.cpu_details)
        self.logical.setObjectName(u"logical")

        self.verticalLayout_2.addWidget(self.logical)


        self.gridLayout.addWidget(self.cpu_details, 0, 1, 5, 1)

        self.temperature = QLabel(self.cpu_info)
        self.temperature.setObjectName(u"temperature")

        self.gridLayout.addWidget(self.temperature, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.cpu_info)


        self.retranslateUi(cpu)

        QMetaObject.connectSlotsByName(cpu)
    # setupUi

    def retranslateUi(self, cpu):
        cpu.setWindowTitle(QCoreApplication.translate("cpu", u"CPU", None))
        self.cpu_info.setTitle("")
        self.processes.setText(QCoreApplication.translate("cpu", u"Processes: ", None))
        self.threads.setText(QCoreApplication.translate("cpu", u"Threads: ", None))
        self.pkg_usage.setText(QCoreApplication.translate("cpu", u"Usage: ", None))
        self.pkg_clk.setText(QCoreApplication.translate("cpu", u"Clock speed: ", None))
        self.cpu_details.setTitle("")
        self.processor.setText(QCoreApplication.translate("cpu", u"Processor: ", None))
        self.arch.setText(QCoreApplication.translate("cpu", u"Architecture: ", None))
        self.base_clk.setText(QCoreApplication.translate("cpu", u"Base clock speed: ", None))
        self.cores.setText(QCoreApplication.translate("cpu", u"Cores: ", None))
        self.logical.setText(QCoreApplication.translate("cpu", u"Logical processors: ", None))
        self.temperature.setText(QCoreApplication.translate("cpu", u"Temperature: ", None))
    # retranslateUi

