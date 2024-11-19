# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nombre_torneoRVhYVl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, ventana2):
        if not ventana2.objectName():
            ventana2.setObjectName(u"ventana2")
        ventana2.resize(710, 489)
        self.centralwidget = QWidget(ventana2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-50, 0, 861, 501))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setPixmap(QPixmap(u"diseños/imagenV2.png"))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 260, 501, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 360, 211, 61))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
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
        ventana2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ventana2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 710, 21))
        ventana2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventana2)
        self.statusbar.setObjectName(u"statusbar")
        ventana2.setStatusBar(self.statusbar)

        self.retranslateUi(ventana2)

        QMetaObject.connectSlotsByName(ventana2)
    # setupUi

    def retranslateUi(self, ventana2):
        ventana2.setWindowTitle(QCoreApplication.translate("ventana2", u"Ventana2", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ventana2", u"Ingrese el nombre del torneo", None))
        self.pushButton.setText(QCoreApplication.translate("ventana2", u"CONTINUAR", None))
    # retranslateUi

