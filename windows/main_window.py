# Form implementation generated from reading ui file './windows/untitled.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 576)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(171, 217, 252);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_first = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_first.setGeometry(QtCore.QRect(210, 0, 441, 51))
        self.title_first.setStyleSheet("color: rgb(37, 27, 159);\n"
"font: 8pt \"MS Sans Forgetica Dlg 2\";")
        self.title_first.setObjectName("title_first")
        self.title2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title2.setGeometry(QtCore.QRect(130, 60, 701, 31))
        self.title2.setStyleSheet("color: rgb(37, 27, 159);\n"
"font: 8pt \"Sans Forgetica\";")
        self.title2.setObjectName("title2")
        self.dialog_btn_main_wind = QtWidgets.QPushButton(parent=self.centralwidget)
        self.dialog_btn_main_wind.setGeometry(QtCore.QRect(670, 430, 181, 41))
        self.dialog_btn_main_wind.setStyleSheet("background-color: rgb(103, 139, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.dialog_btn_main_wind.setObjectName("dialog_btn_main_wind")
        self.Osetian_language = QtWidgets.QLabel(parent=self.centralwidget)
        self.Osetian_language.setGeometry(QtCore.QRect(20, 300, 271, 39))
        self.Osetian_language.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.Osetian_language.setObjectName("Osetian_language")
        self.sp_ossetian_poetry = QtWidgets.QComboBox(parent=self.centralwidget)
        self.sp_ossetian_poetry.setGeometry(QtCore.QRect(20, 350, 731, 51))
        self.sp_ossetian_poetry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.sp_ossetian_poetry.setObjectName("sp_ossetian_poetry")
        self.sp_russian_poetry = QtWidgets.QComboBox(parent=self.centralwidget)
        self.sp_russian_poetry.setGeometry(QtCore.QRect(20, 200, 731, 51))
        self.sp_russian_poetry.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.sp_russian_poetry.setObjectName("sp_russian_poetry")
        self.Russian_language = QtWidgets.QLabel(parent=self.centralwidget)
        self.Russian_language.setGeometry(QtCore.QRect(20, 160, 211, 31))
        self.Russian_language.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.Russian_language.setObjectName("Russian_language")
        self.choose_russian_poetry = QtWidgets.QPushButton(parent=self.centralwidget)
        self.choose_russian_poetry.setGeometry(QtCore.QRect(760, 200, 91, 51))
        self.choose_russian_poetry.setStyleSheet("background-color: rgb(103, 139, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.choose_russian_poetry.setObjectName("choose_russian_poetry")
        self.choose_ossetian_poetry = QtWidgets.QPushButton(parent=self.centralwidget)
        self.choose_ossetian_poetry.setGeometry(QtCore.QRect(760, 350, 91, 51))
        self.choose_ossetian_poetry.setStyleSheet("background-color: rgb(103, 139, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.choose_ossetian_poetry.setObjectName("choose_ossetian_poetry")
        self.delete_file = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_file.setGeometry(QtCore.QRect(20, 430, 161, 41))
        self.delete_file.setStyleSheet("background-color: rgb(103, 139, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.delete_file.setObjectName("delete_file")
        self.label_for_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_for_image.setGeometry(QtCore.QRect(720, 0, 111, 101))
        self.label_for_image.setText("")
        self.label_for_image.setObjectName("label_for_image")
        self.add_poetry_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_poetry_btn.setGeometry(QtCore.QRect(350, 430, 161, 41))
        self.add_poetry_btn.setStyleSheet("background-color: rgb(103, 139, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.add_poetry_btn.setObjectName("add_poetry_btn")
        self.kolvo_learn_poetry = QtWidgets.QLabel(parent=self.centralwidget)
        self.kolvo_learn_poetry.setGeometry(QtCore.QRect(550, 120, 311, 20))
        self.kolvo_learn_poetry.setText("")
        self.kolvo_learn_poetry.setObjectName("kolvo_learn_poetry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_first.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">УЧИ СТИХИ ЛЕГКО!</span></p></body></html>"))
        self.title2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Выбери стихотворение из списка или файл с текстом</span></p></body></html>"))
        self.dialog_btn_main_wind.setText(_translate("MainWindow", "Выбрать Файл"))
        self.Osetian_language.setText(_translate("MainWindow", "Осетинский язык:"))
        self.Russian_language.setText(_translate("MainWindow", "Русский язык:"))
        self.choose_russian_poetry.setText(_translate("MainWindow", "Выбрать"))
        self.choose_ossetian_poetry.setText(_translate("MainWindow", "Выбрать"))
        self.delete_file.setText(_translate("MainWindow", "Удалить стих из списка"))
        self.add_poetry_btn.setText(_translate("MainWindow", "Добавить стих в список"))