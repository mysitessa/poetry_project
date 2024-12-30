# Form implementation generated from reading ui file './windows/inf_win.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_inf_win(object):
    def setupUi(self, inf_win):
        inf_win.setObjectName("inf_win")
        inf_win.resize(463, 443)
        inf_win.setStyleSheet("background-color: rgb(171, 217, 252);")
        self.centralwidget = QtWidgets.QWidget(parent=inf_win)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 31))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(37, 27, 159)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 211, 20))
        self.label_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 251, 16))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 231, 21))
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.inf_win_poetry_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inf_win_poetry_name.setGeometry(QtCore.QRect(10, 180, 221, 20))
        self.inf_win_poetry_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inf_win_poetry_name.setObjectName("inf_win_poetry_name")
        self.inf_win_autor_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inf_win_autor_name.setGeometry(QtCore.QRect(10, 260, 221, 20))
        self.inf_win_autor_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inf_win_autor_name.setObjectName("inf_win_autor_name")
        self.inf_win_save_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.inf_win_save_btn.setGeometry(QtCore.QRect(300, 350, 75, 23))
        self.inf_win_save_btn.setStyleSheet("background-color: rgb(103, 139, 255);")
        self.inf_win_save_btn.setObjectName("inf_win_save_btn")
        self.inf_win_rus_lang = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.inf_win_rus_lang.setGeometry(QtCore.QRect(140, 100, 82, 17))
        self.inf_win_rus_lang.setObjectName("inf_win_rus_lang")
        self.inf_win_oset_lang = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.inf_win_oset_lang.setGeometry(QtCore.QRect(20, 100, 82, 17))
        self.inf_win_oset_lang.setObjectName("inf_win_oset_lang")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 201, 16))
        self.label_5.setObjectName("label_5")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(10, 360, 281, 41))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.inf_win_poetry_text = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.inf_win_poetry_text.setGeometry(QtCore.QRect(10, 330, 221, 21))
        self.inf_win_poetry_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inf_win_poetry_text.setObjectName("inf_win_poetry_text")
        inf_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=inf_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 24))
        self.menubar.setObjectName("menubar")
        inf_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=inf_win)
        self.statusbar.setObjectName("statusbar")
        inf_win.setStatusBar(self.statusbar)

        self.retranslateUi(inf_win)
        QtCore.QMetaObject.connectSlotsByName(inf_win)

    def retranslateUi(self, inf_win):
        _translate = QtCore.QCoreApplication.translate
        inf_win.setWindowTitle(_translate("inf_win", "MainWindow"))
        self.label.setText(_translate("inf_win", "Информация о стихотворении"))
        self.label_2.setText(_translate("inf_win", "1. Выбери язык стиха:"))
        self.label_3.setText(_translate("inf_win", "2. Напиши название стиха:"))
        self.label_4.setText(_translate("inf_win", "3. Напиши автора стиха:"))
        self.inf_win_save_btn.setText(_translate("inf_win", "Сохранить"))
        self.inf_win_rus_lang.setText(_translate("inf_win", "Русский"))
        self.inf_win_oset_lang.setText(_translate("inf_win", "Осетинский"))
        self.label_5.setText(_translate("inf_win", "4. Введи текст стихотворения:"))
