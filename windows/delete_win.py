# Form implementation generated from reading ui file 'delete_win.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_delete_win(object):
    def setupUi(self, delete_win):
        delete_win.setObjectName("delete_win")
        delete_win.resize(600, 258)
        delete_win.setStyleSheet("background-color: rgb(171, 217, 252);")
        self.centralwidget = QtWidgets.QWidget(parent=delete_win)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 591, 31))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(37, 27, 159)")
        self.label.setObjectName("label")
        self.delete_win_sp_poetry = QtWidgets.QComboBox(parent=self.centralwidget)
        self.delete_win_sp_poetry.setGeometry(QtCore.QRect(20, 110, 541, 51))
        self.delete_win_sp_poetry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.delete_win_sp_poetry.setObjectName("delete_win_sp_poetry")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 141, 31))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.delete_win_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_win_btn.setGeometry(QtCore.QRect(490, 190, 75, 23))
        self.delete_win_btn.setStyleSheet("background-color: rgb(103, 139, 255);")
        self.delete_win_btn.setObjectName("delete_win_btn")
        delete_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=delete_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 24))
        self.menubar.setObjectName("menubar")
        delete_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=delete_win)
        self.statusbar.setObjectName("statusbar")
        delete_win.setStatusBar(self.statusbar)

        self.retranslateUi(delete_win)
        QtCore.QMetaObject.connectSlotsByName(delete_win)

    def retranslateUi(self, delete_win):
        _translate = QtCore.QCoreApplication.translate
        delete_win.setWindowTitle(_translate("delete_win", "MainWindow"))
        self.label.setText(_translate("delete_win", "Выбери стихотворение, которое ты хочешь удалить"))
        self.label_2.setText(_translate("delete_win", "Все стихи:"))
        self.delete_win_btn.setText(_translate("delete_win", "Удалить"))
