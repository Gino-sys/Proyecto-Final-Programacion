# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nombre_torneoSIPawv.ui'
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
        ventana2.resize(711, 489)
        self.centralwidget = QWidget(ventana2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-60, 0, 861, 501))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setPixmap(QPixmap(u"diseños/imagenV2.png"))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 260, 451, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 350, 241, 51))
        icon = QIcon()
        icon.addFile(u"diseños/imgbot2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(500, 90))
        ventana2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ventana2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 711, 21))
        ventana2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventana2)
        self.statusbar.setObjectName(u"statusbar")
        ventana2.setStatusBar(self.statusbar)

        self.retranslateUi(ventana2)
        self.pushButton.clicked.connect(ventana2.ir_a_siguiente_pestana)

        QMetaObject.connectSlotsByName(ventana2)
    # setupUi

    def retranslateUi(self, ventana2):
        ventana2.setWindowTitle(QCoreApplication.translate("ventana2", u"Ventana2", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ventana2", u"Ingrese el nombre del torneo", None))
        self.pushButton.setText("")
    # retranslateUi

