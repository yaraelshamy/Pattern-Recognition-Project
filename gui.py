# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 624)
        MainWindow.setMinimumSize(QtCore.QSize(757, 624))
        MainWindow.setMaximumSize(QtCore.QSize(757, 675))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(757, 624))
        self.centralwidget.setMaximumSize(QtCore.QSize(757, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.GUI_label = QtWidgets.QLabel(self.centralwidget)
        self.GUI_label.setGeometry(QtCore.QRect(11, 11, 731, 31))
        self.GUI_label.setMinimumSize(QtCore.QSize(4, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.GUI_label.setFont(font)
        self.GUI_label.setAlignment(QtCore.Qt.AlignCenter)
        self.GUI_label.setObjectName("GUI_label")
        self.browse_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.browse_pushButton.setGeometry(QtCore.QRect(10, 50, 741, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.browse_pushButton.setFont(font)
        self.browse_pushButton.setStyleSheet("")
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.org_img_disp_label = QtWidgets.QLabel(self.centralwidget)
        self.org_img_disp_label.setGeometry(QtCore.QRect(11, 90, 741, 401))
        self.org_img_disp_label.setText("")
        self.org_img_disp_label.setObjectName("org_img_disp_label")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(10, 510, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.result_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.result_label_2.setGeometry(QtCore.QRect(10, 550, 741, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.result_label_2.setFont(font)
        self.result_label_2.setText("")
        self.result_label_2.setObjectName("result_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GUI_label.setText(_translate("MainWindow", "Image Classification"))
        self.browse_pushButton.setText(_translate("MainWindow", "Browse"))

