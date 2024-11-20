# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archivo8OMkuzK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(661, 443)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -30, 691, 461))
        self.label.setPixmap(QPixmap(u"diseños/imagen8.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 80, 191, 21))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 160, 181, 16))
        font1 = QFont()
        font1.setFamily(u"Constantia")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: white;\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 350, 191, 41))
        font2 = QFont()
        font2.setFamily(u"Cooper Black")
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: #1e7e34;  /* Verde oscuro */\n"
"color: white;               /* Texto en blanco */\n"
"")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 350, 91, 41))
        font3 = QFont()
        font3.setFamily(u"Cooper Black")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"background-color: #1e7e34;  /* Verde oscuro */\n"
"color: white;               /* Texto en blanco */\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 230, 181, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: white;\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 230, 181, 16))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: white;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 661, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.next)
        self.pushButton_2.clicked.connect(MainWindow.principio)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana8", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOMBRE_TORNEO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"VER HISTORIAL", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

