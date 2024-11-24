# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archivo7nRxDLO.ui'
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
        MainWindow.resize(845, 577)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -20, 901, 641))
        self.label.setPixmap(QPixmap(u"diseños/ImagenCruces.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 240, 101, 31))
        font = QFont()
        font.setFamily(u"Cooper Black")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 330, 101, 20))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 400, 101, 21))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 480, 101, 31))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(730, 240, 91, 31))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(730, 330, 91, 20))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(730, 400, 91, 20))
        self.label_8.setFont(font)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(730, 479, 91, 31))
        self.label_9.setFont(font)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 279, 101, 31))
        self.label_10.setFont(font)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(180, 440, 101, 21))
        self.label_11.setFont(font)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(590, 279, 91, 31))
        self.label_12.setFont(font)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(590, 440, 91, 31))
        self.label_13.setFont(font)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(310, 370, 91, 31))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(460, 370, 91, 31))
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 340, 121, 21))
        font1 = QFont()
        font1.setFamily(u"Cooper Black")
        font1.setPointSize(11)
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 460, 251, 61))
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
        icon = QIcon()
        icon.addFile(u"diseños/imgbot8.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(300, 90))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 845, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.siguiente_pag)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana7", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Equipo_1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Equipo_2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Equipo_3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Equipo_4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Equipo_5", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Equipo_6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Equipo_7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Equipo_8", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ganador_1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ganador_2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ganador_3", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ganador_4", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ganador_5", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ganador_6", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ganador_Final", None))
        self.pushButton.setText("")
    # retranslateUi

