# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archivo5cvCbJK.ui'
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
        MainWindow.resize(705, 402)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, -120, 991, 581))
        self.label_2.setPixmap(QPixmap(u"diseños/imgventana5.png"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 190, 181, 41))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #28a745;  /* Color de fondo verde */\n"
"    color: white;               /* Color del texto */\n"
"    border-radius: 5px;         /* Bordes redondeados */\n"
"    padding: 5px;               /* Espacio interno */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #218838;  /* Color cuando el mouse pasa encima */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1e7e34;  /* Color cuando el bot\u00f3n es presionado */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"diseños/crucesimg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(400, 50))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 240, 271, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #28a745;  /* Color de fondo verde */\n"
"    color: white;               /* Color del texto */\n"
"    border-radius: 5px;         /* Bordes redondeados */\n"
"    padding: 5px;               /* Espacio interno */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #218838;  /* Color cuando el mouse pasa encima */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1e7e34;  /* Color cuando el bot\u00f3n es presionado */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"diseños/imagebot6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(300, 73))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 100, 681, 61))
        font1 = QFont()
        font1.setFamily(u"Cooper Black")
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 705, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.Volver)
        self.pushButton.clicked.connect(MainWindow.siguiente)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana5", None))
        self.label_2.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TU -TORNEO", None))
    # retranslateUi

