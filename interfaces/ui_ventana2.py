# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nombre_torneo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, ventana2):
        ventana2.setObjectName("ventana2")
        ventana2.resize(800, 518)
        self.centralwidget = QtWidgets.QWidget(ventana2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, -10, 861, 501))
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("diseños/imagenV2.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 260, 501, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 370, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #28a745;  /* Color de fondo verde */\n"
"    color: white;               /* Color del texto */\n"
"    border-radius: 5px;         /* Bordes redondeados */\n"
"    padding: 5px;               /* Espacio interno */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #218838;  /* Color cuando el mouse pasa encima */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1e7e34;  /* Color cuando el botón es presionado */\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        ventana2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventana2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        ventana2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventana2)
        self.statusbar.setObjectName("statusbar")
        ventana2.setStatusBar(self.statusbar)

        self.retranslateUi(ventana2)
        QtCore.QMetaObject.connectSlotsByName(ventana2)

    def retranslateUi(self, ventana2):
        _translate = QtCore.QCoreApplication.translate
        ventana2.setWindowTitle(_translate("ventana2", "Ventana2"))
        self.pushButton.setText(_translate("ventana2", "CONTINUAR"))
