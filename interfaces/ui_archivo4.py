# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archivo4ahrovN.ui'
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
        MainWindow.resize(672, 497)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 20, 681, 471))
        self.label.setPixmap(QPixmap(u"diseños/ImagenV4.png"))
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(130, 190, 201, 31))
        self.lineEdit_1.setStyleSheet(u"QPushButton {\n"
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
        self.lineEdit_1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 230, 201, 31))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 270, 201, 31))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(130, 310, 201, 31))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(480, 190, 191, 31))
        self.lineEdit_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(480, 230, 191, 31))
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(480, 270, 191, 31))
        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(480, 310, 191, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 380, 261, 51))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(16)
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
        icon.addFile(u"diseños/imgbot4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(700, 120))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 672, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.siguiente)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana4", None))
        self.label.setText("")
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ingrese el nombre del equipo", None))
        self.pushButton.setText("")
    # retranslateUi

