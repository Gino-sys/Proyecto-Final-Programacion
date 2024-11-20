# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz_uilfMICD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, ventana1):
        if not ventana1.objectName():
            ventana1.setObjectName(u"ventana1")
        ventana1.resize(772, 539)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventana1.sizePolicy().hasHeightForWidth())
        ventana1.setSizePolicy(sizePolicy)
        ventana1.setMinimumSize(QSize(200, 200))
        ventana1.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(ventana1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 901, 511))
        self.label.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"diseños/imagen_del_1.png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.torneo_button = QPushButton(self.centralwidget)
        self.torneo_button.setObjectName(u"torneo_button")
        self.torneo_button.setGeometry(QRect(100, 340, 261, 61))
        font1 = QFont()
        font1.setFamily(u"Cooper Black")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.torneo_button.setFont(font1)
        self.torneo_button.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u"diseños/imgboton1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.torneo_button.setIcon(icon)
        self.torneo_button.setIconSize(QSize(470, 100))
        ventana1.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ventana1)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 21))
        ventana1.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventana1)
        self.statusbar.setObjectName(u"statusbar")
        ventana1.setStatusBar(self.statusbar)

        self.retranslateUi(ventana1)
        self.torneo_button.clicked.connect(ventana1.abrir)

        QMetaObject.connectSlotsByName(ventana1)
    # setupUi

    def retranslateUi(self, ventana1):
        ventana1.setWindowTitle(QCoreApplication.translate("ventana1", u"Ventana1", None))
        self.label.setText("")
        self.torneo_button.setText("")
    # retranslateUi

