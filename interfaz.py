# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 461, 501))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1.setGeometry(QtCore.QRect(270, 50, 41, 23))
        self.btn1.setObjectName("btn1")
        self.cmb1 = QtWidgets.QComboBox(self.groupBox)
        self.cmb1.setGeometry(QtCore.QRect(18, 50, 241, 22))
        self.cmb1.setObjectName("cmb1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 211, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 141, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 160, 431, 331))
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 391, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 371, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 260, 371, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 300, 371, 16))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 371, 16))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 380, 381, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 420, 381, 16))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(30, 460, 371, 16))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 391, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(30, 200, 371, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(30, 240, 371, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(30, 280, 371, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(30, 320, 371, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(30, 360, 381, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(30, 400, 381, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(30, 440, 371, 16))
        self.label_20.setObjectName("label_20")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(60, 550, 75, 23))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(240, 550, 75, 23))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(390, 550, 75, 23))
        self.btn4.setObjectName("btn4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M??dulo r??ster"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos de entrada"))
        self.label.setText(_translate("MainWindow", "Seleciona el archivo"))
        self.btn1.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Sistema de referencia geoespacial"))
        self.label_3.setText(_translate("MainWindow", "SRG"))
        self.label_4.setText(_translate("MainWindow", "Datos de informaci??n"))
        self.label_13.setText(_translate("MainWindow", "Extend:"))
        self.label_14.setText(_translate("MainWindow", "x minima:"))
        self.label_15.setText(_translate("MainWindow", "x maxima:"))
        self.label_16.setText(_translate("MainWindow", "y minima:"))
        self.label_17.setText(_translate("MainWindow", "y maxima:"))
        self.label_18.setText(_translate("MainWindow", "Ancho:"))
        self.label_19.setText(_translate("MainWindow", "Alto:"))
        self.label_20.setText(_translate("MainWindow", "Tama??o de pixel:"))
        self.btn2.setText(_translate("MainWindow", "Ayuda"))
        self.btn3.setText(_translate("MainWindow", "Ejecutar"))
        self.btn4.setText(_translate("MainWindow", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
