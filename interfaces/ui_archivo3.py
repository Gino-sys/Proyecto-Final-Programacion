# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archivo3jwnCzg.ui'
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
        MainWindow.resize(700, 426)
        MainWindow.setMinimumSize(QSize(200, 200))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labeljj = QLabel(self.centralwidget)
        self.labeljj.setObjectName(u"labeljj")
        self.labeljj.setGeometry(QRect(-190, -40, 1081, 471))
        self.labeljj.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(26)
        self.labeljj.setFont(font)
        self.labeljj.setPixmap(QPixmap(u"diseños/nueva imagen del 3.png"))
        self.labeljj.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 230, 281, 101))
        font1 = QFont()
        font1.setFamily(u"Cooper Black")
        font1.setPointSize(28)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 250, 301, 71))
        font2 = QFont()
        font2.setFamily(u"Cooper Black")
        font2.setPointSize(18)
        self.pushButton.setFont(font2)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.otra)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana3", None))
        self.labeljj.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TU_TORNEO", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR EQUIPOS ", None))
    # retranslateUi

