# Form implementation generated from reading ui file 'D:\Desktop\PycharmProjects\TDLT-UEL-PTB1\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 354)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditinputa = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditinputa.setGeometry(QtCore.QRect(90, 60, 211, 31))
        self.lineEditinputa.setObjectName("lineEditinputa")
        self.lineEditinputb = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditinputb.setGeometry(QtCore.QRect(90, 100, 211, 31))
        self.lineEditinputb.setObjectName("lineEditinputb")
        self.lineEditinputc = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditinputc.setGeometry(QtCore.QRect(90, 140, 211, 31))
        self.lineEditinputc.setObjectName("lineEditinputc")
        self.pushButtonclose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonclose.setGeometry(QtCore.QRect(170, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonclose.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Desktop\\PycharmProjects\\TDLT-UEL-PTB1\\../../../Downloads/1031533_cancel_close_cross_delete_remove_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonclose.setIcon(icon)
        self.pushButtonclose.setObjectName("pushButtonclose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonclose.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                           1st degree equation"))
        self.label_2.setText(_translate("MainWindow", "Input a:"))
        self.label_3.setText(_translate("MainWindow", "Input b:"))
        self.label_4.setText(_translate("MainWindow", "N.o x:"))
        self.pushButtonclose.setText(_translate("MainWindow", "CLOSE"))
