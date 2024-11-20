# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archivo9hbPmbL.ui'
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
        MainWindow.resize(598, 374)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -40, 731, 461))
        self.label.setPixmap(QPixmap(u"diseños/imagenV9.png"))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 10, 291, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 50, 131, 31))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(300, 90, 291, 181))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 290, 151, 31))
        font1 = QFont()
        font1.setFamily(u"Cooper Black")
        font1.setPointSize(16)
        self.pushButton_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.regresar)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana9", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
    # retranslateUi

