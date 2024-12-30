import random

from windows.main_window import Ui_MainWindow
from windows.task_read import Ui_SecondWindow2
from windows.delete_win import Ui_delete_win
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys
import sqlite3
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap
from windows.inf_win import Ui_inf_win
from windows.task_random_string import Ui_random_string_win
from random import choice
from windows.pass_word import Ui_pass_word


class ChoiseFile(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.setWindowTitle('Учи стихи легко!')
        self.initUI()
        self.iteration_counter = 0
        self.con = sqlite3.connect('BaseDate.sqlite')
        self.cur = self.con.cursor()
        self.res = self.cur.execute("""SELECT count FROM poetry_count""").fetchall()
        self.kolvo_learn_poetry.setText(f'Кол-во выуч. стихов: {self.res[0][0]}')
        self.choose_russian_poetry.clicked.connect(self.click_choiseFromBD)
        self.choose_ossetian_poetry.clicked.connect(self.click_choiseFromBD_ose)
        self.dialog_btn_main_wind.clicked.connect(self.click_choiseFile)
        self.delete_file.clicked.connect(self.click_delete)
        self.add_poetry_btn.clicked.connect(self.click_AddPoetry)
        self.add_items()

    def add_items(self):
        self.result_rus = self.cur.execute("""SELECT title FROM poetry
                                    WHERE lang = 'ru'""").fetchall()
        self.main_sp_rus_poetry = []
        for i in self.result_rus:
            self.main_sp_rus_poetry.append(*i)

        self.result_oset = self.cur.execute("""SELECT title FROM poetry
                                            WHERE lang = 'oset'""").fetchall()

        self.main_sp_oset_poetry = []
        for i in self.result_oset:
            self.main_sp_oset_poetry.append(*i)

        for i in self.main_sp_oset_poetry:
            self.sp_ossetian_poetry.addItem(i)

        for i in self.main_sp_rus_poetry:
            self.sp_russian_poetry.addItem(i)

    def initUI(self):
        self.pixmap = QPixmap('image/icon.png')
        self.label_for_image.setPixmap(self.pixmap)

    def click_choiseFile(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', '*.txt')[0]
        if self.fname:  # Проверяем, что файл был выбран
            self.Task_read_win = Task_read(self.fname, self.iteration_counter)  # Передаем fname в Task_read
            self.Task_read_win.open_file_text()
            self.Task_read_win.show()

    def click_choiseFromBD(self):
        self.current_text = self.sp_russian_poetry.currentText()
        self.result = self.cur.execute(f"SELECT text FROM poetry WHERE title = '{self.current_text}'").fetchall()
        self.text = self.result[0][0]
        self.task_read_win = Task_read(self.text, self.iteration_counter)
        self.task_read_win.text_fromBD()
        self.task_read_win.show()

    def click_delete(self):
        self.delete = Delete(self.sp_ossetian_poetry, self.sp_russian_poetry, self.main_sp_oset_poetry,
                             self.main_sp_rus_poetry)
        self.delete.show()
        # self.delete.del_from_sp()

    def click_choiseFromBD_ose(self):
        self.current_text = self.sp_ossetian_poetry.currentText()
        con = sqlite3.connect('BaseDate.sqlite')
        cur = con.cursor()
        self.result = cur.execute(f"SELECT text FROM poetry WHERE title = '{self.current_text}'").fetchall()
        self.text = self.result[0][0]
        self.task_read_win = Task_read(self.text, self.iteration_counter)
        self.task_read_win.text_fromBD()
        self.task_read_win.show()

    def click_AddPoetry(self):
        self.addPoet = Add_PoetryToBD(self.main_sp_oset_poetry, self.main_sp_rus_poetry, self.sp_ossetian_poetry,
                                      self.sp_russian_poetry)
        self.addPoet.show()


class Task_read(QMainWindow, Ui_SecondWindow2):
    def __init__(self, text, iteration):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.setWindowTitle('Учи стихи легко!')
        self.text = text
        self.iteration_counter = iteration
        self.ready_read.clicked.connect(self.click_ready)

    def open_file_text(self):
        self.sp_strings = list(map(str.strip, open(self.text).readlines()))
        self.text = list(map(str.strip, open(self.text).readlines()))
        for i in range(self.sp_strings.count('')):
            self.sp_strings.remove('')
        self.split_sp_text = [self.sp_strings[i:i + 4] for i in range(0, len(self.sp_strings), 4)]
        self.four_string_original.setText('\n'.join(self.split_sp_text[self.iteration_counter]))

    def text_fromBD(self):  # doing
        self.text = self.text.split('\n')
        for i in range(self.text.count('')):
            self.text.remove('')
        self.split_sp_text = [self.text[i:i + 4] for i in range(0, len(self.text), 4)]
        self.four_string_original.setText('\n'.join(self.split_sp_text[self.iteration_counter]))

    def click_ready(self):
        self.random_string_win = Task_random_string(self.iteration_counter, self.split_sp_text, self.text)
        self.random_string_win.show()
        self.hide()


class Delete(QMainWindow, Ui_delete_win):
    def __init__(self, sp_oset, sp_rus, main_sp_oset, main_sp_rus):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.setWindowTitle('Учи стихи легко!')
        self.sp_oset = sp_oset
        self.sp_rus = sp_rus
        self.oset_items = main_sp_oset
        self.rus_items = main_sp_rus
        self.items_to_sp()
        self.delete_win_btn.clicked.connect(self.del_from_sp)

    def items_to_sp(self):
        self.All_Items = self.oset_items + self.rus_items
        for i in self.All_Items:
            self.delete_win_sp_poetry.addItem(i)

    def del_from_sp(self):
        self.flag = True
        if self.flag:
            for i in range(self.sp_oset.count()):
                if self.delete_win_sp_poetry.currentText() in self.sp_oset.itemText(i):
                    self.sp_oset.removeItem(self.sp_oset.findText(self.delete_win_sp_poetry.currentText()))
                    con = sqlite3.connect('BaseDate.sqlite')
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM poetry WHERE title = '{self.delete_win_sp_poetry.currentText()}'")
                    self.oset_items.remove(self.delete_win_sp_poetry.currentText())
                    con.commit()
                    self.flag = False
                    con.close()
                    self.delete_win_sp_poetry.clear()
                    self.items_to_sp()
                    self.hide()
                    break

        if self.flag:
            for i in range(self.sp_rus.count()):
                if self.delete_win_sp_poetry.currentText() in self.sp_rus.itemText(i):
                    self.sp_rus.removeItem(self.sp_rus.findText(self.delete_win_sp_poetry.currentText()))
                    con = sqlite3.connect('BaseDate.sqlite')
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM poetry WHERE title = '{self.delete_win_sp_poetry.currentText()}'")
                    self.rus_items.remove(self.delete_win_sp_poetry.currentText())
                    con.commit()
                    con.close()
                    self.delete_win_sp_poetry.clear()
                    self.items_to_sp()
                    self.hide()
                    break


class Add_PoetryToBD(QMainWindow, Ui_inf_win):
    def __init__(self, main_oset, main_rus, sp_oset, sp_rus):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.setWindowTitle('Учи стихи легко!')
        self.check_Lang = None
        self.main_oset = main_oset
        self.main_rus = main_rus
        self.sp_oset = sp_oset
        self.sp_rus = sp_rus

        self.inf_win_oset_lang.toggled.connect(self.check_oset_poetry)
        self.inf_win_rus_lang.toggled.connect(self.check_rus_poetry)
        self.inf_win_save_btn.clicked.connect(self.Add_poetry_to_SP)

    def check_oset_poetry(self):
        self.check_Lang = True

    def check_rus_poetry(self):
        self.check_Lang = False

    def Add_poetry_to_SP(self):
        if self.check_Lang:
            self.lang = 'oset'
            con = sqlite3.connect('BaseDate.sqlite')
            cur = con.cursor()
            if len(self.inf_win_poetry_text.toPlainText()) > 0 and len(self.inf_win_poetry_name.text()) > 0 and len(
                    self.inf_win_autor_name.text()) > 0 and self.check_Lang != None:
                cur.execute(
                    f"INSERT INTO poetry(author, title, text, lang) VALUES('{self.inf_win_autor_name.text()}', '{self.inf_win_poetry_name.text()}', '{self.inf_win_poetry_text.toPlainText()}', '{self.lang}')")
                con.commit()
                self.main_oset.append(self.inf_win_poetry_name.text())
                self.sp_oset.addItem(self.inf_win_poetry_name.text())
                self.error_label.setText('Успешно добавлено')
                self.hide()

            elif len(self.inf_win_autor_name.text()) == 0:
                self.error_label.setText('Введи имя автора')
            elif len(self.inf_win_poetry_name.text()) == 0:
                self.error_label.setText('Введи название')
            elif len(self.inf_win_poetry_text.toPlainText()) == 0:
                self.error_label.setText('Введи текст')

        elif self.check_Lang == False:
            self.lang = 'ru'
            con = sqlite3.connect('BaseDate.sqlite')
            cur = con.cursor()
            if len(self.inf_win_poetry_text.toPlainText()) > 0 and len(self.inf_win_poetry_name.text()) > 0 and len(
                    self.inf_win_autor_name.text()) > 0 and self.check_Lang != None:
                cur.execute(
                    f"INSERT INTO poetry(author, title, text, lang) VALUES('{self.inf_win_autor_name.text()}', '{self.inf_win_poetry_name.text()}', '{self.inf_win_poetry_text.toPlainText()}', '{self.lang}')")
                con.commit()
                self.main_rus.append(self.inf_win_poetry_name.text())
                self.sp_rus.addItem(self.inf_win_poetry_name.text())
                self.error_label.setText('Успешно добавлено')

            elif len(self.inf_win_autor_name.text()) == 0:
                self.error_label.setText('Введи имя автора')
            elif len(self.inf_win_poetry_name.text()) == 0:
                self.error_label.setText('Введи название')
            elif len(self.inf_win_poetry_text.toPlainText()) == 0:
                self.error_label.setText('Введи текст')

        else:
            self.error_label.setText('Выбери язык')


class Task_random_string(QMainWindow, Ui_random_string_win):
    def __init__(self, iteration_count, sp, text):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.setWindowTitle('Учи стихи легко!')
        self.iteration_count = iteration_count
        self.split_sp_text = sp
        self.text = text
        self.answers = {}
        self.add_ans()
        self.add_strings()
        self.random_string_win_checkBtn.clicked.connect(self.check_ans)
        self.dalee_btn.clicked.connect(self.click_dalee)
        self.dalee_btn.hide()

    def add_ans(self):
        for i in range(len(self.split_sp_text[self.iteration_count])):
            self.answers[self.split_sp_text[self.iteration_count][i]] = i + 1

    def add_strings(self):
        print(self.split_sp_text)
        self.cur_strings = self.split_sp_text[self.iteration_count].copy()
        print(self.cur_strings)
        if len(self.cur_strings) >= 4:

            self.random_str_win_1.setText(choice(self.cur_strings))
            self.cur_strings.remove(self.random_str_win_1.text())

            self.random_str_win_2.setText(choice(self.cur_strings))
            self.cur_strings.remove(self.random_str_win_2.text())

            self.random_str_win_3.setText(choice(self.cur_strings))
            self.cur_strings.remove(self.random_str_win_3.text())

            self.random_str_win_4.setText(choice(self.cur_strings))
            self.cur_strings.remove(self.random_str_win_4.text())
        elif len(self.cur_strings) == 1:
            self.random_str_win_1.setText(self.cur_strings[0])
        elif len(self.cur_strings) == 2:
            self.random_str_win_1.setText(choice(self.cur_strings))
            self.cur_strings.remove(self.random_str_win_1.text())
            self.random_str_win_2.setText(self.cur_strings[0])
        elif len(self.cur_strings) == 3:
            self.random_str_win_1.setText(choice(self.cur_strings))
            self.cur_strings.remove(self.random_str_win_1.text())
            self.random_str_win_2.setText(choice(self.cur_strings))
            self.cur_strings.remove(self.random_str_win_2.text())
            print(self.cur_strings)
            self.random_str_win_3.setText(self.cur_strings[0])

    def check_ans(self):
        self.r_ans_cou = 0
        if len(self.random_str_win_1.text()) > 0 and len(self.random_str_win_2.text()) > 0 and len(
                self.random_str_win_3.text()) > 0 and len(self.random_str_win_4.text()) > 0:
            if self.answers.get(self.random_str_win_1.text()) == self.random_string_num1.value():
                self.r_ans_cou += 1

            if self.answers.get(self.random_str_win_2.text()) == self.random_string_num2.value():
                self.r_ans_cou += 1

            if self.answers.get(self.random_str_win_2.text()) == self.random_string_num2.value():
                self.r_ans_cou += 1

            if self.answers.get(self.random_str_win_2.text()) == self.random_string_num2.value():
                self.r_ans_cou += 1

            if self.r_ans_cou == 4:
                self.label.setText('ВСЕ ПРАВИЛЬНО')
                self.label.setStyleSheet("background-color: green")
                self.dalee_btn.show()


            else:
                self.label.setText('ЕСТЬ ОШИБКА')
                self.label.setStyleSheet("background-color: red")

        elif len(self.random_str_win_1.text()) > 0 and len(self.random_str_win_2.text()) > 0 and len(
                self.random_str_win_3.text()) > 0:
            if self.answers.get(self.random_str_win_1.text()) == self.random_string_num1.value():
                self.r_ans_cou += 1

            if self.answers.get(self.random_str_win_2.text()) == self.random_string_num2.value():
                self.r_ans_cou += 1

            if self.answers.get(self.random_str_win_4.text()) == self.random_string_num3.value():
                self.r_ans_cou += 1

            if self.r_ans_cou == 3:
                self.label.setText('ВСЕ ПРАВИЛЬНО')
                self.label.setStyleSheet("background-color: green")
                self.dalee_btn.show()
            else:
                self.label.setText('ЕСТЬ ОШИБКА')
                self.label.setStyleSheet("background-color: red")

        elif len(self.random_str_win_1.text()) > 0 and len(self.random_str_win_2.text()) > 0:
            if self.answers.get(self.random_str_win_1.text()) == self.random_string_num1.value():
                self.r_ans_cou += 1

            if self.answers.get(self.random_str_win_2.text()) == self.random_string_num2.value():
                self.r_ans_cou += 1
            if self.r_ans_cou == 2:
                self.label.setText('ВСЕ ПРАВИЛЬНО')
                self.label.setStyleSheet("background-color: green")
                self.dalee_btn.show()
            else:
                self.label.setText('ЕСТЬ ОШИБКА')
                self.label.setStyleSheet("background-color: red")
        elif len(self.random_str_win_1.text()) > 0:
            if self.answers.get(self.random_str_win_1.text()) == self.random_string_num1.value():
                self.r_ans_cou += 1
            if self.r_ans_cou == 1:
                self.label.setText('ВСЕ ПРАВИЛЬНО')
                self.label.setStyleSheet("background-color: green")
                self.dalee_btn.show()
            else:
                self.label.setText('ЕСТЬ ОШИБКА')
                self.label.setStyleSheet("background-color: red")
        print(self.answers)

    def click_dalee(self):
        self.TaskPassWord = TaskPassWord(self.split_sp_text, self.iteration_count, self.text)
        self.TaskPassWord.show()
        self.hide()


class TaskPassWord(QMainWindow, Ui_pass_word):
    def __init__(self, split_sp_text, iteration_count, text):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('image/icon.png'))
        self.setWindowTitle('Учи стихи легко!')
        self.text = text
        self.string_counter = 0
        self.split_sp_text = split_sp_text
        self.iteration_count = iteration_count
        self.cur_sp = self.split_sp_text[self.iteration_count].copy()
        self.pass_word()
        self.podsk_cou = 2
        self.pass_word_podskazka_cou.setText(f'Подсказок осталось: {str(self.podsk_cou)}')
        self.pass_word_checkAns.clicked.connect(self.check_ans)
        self.pass_word_dalee.clicked.connect(self.new_win)
        self.pass_word_podskazka.clicked.connect(self.click_podskazka)
        self.pass_word_dalee.hide()

    def pass_word(self):
        self.sp_string = self.cur_sp[self.string_counter].split()
        self.random_index = random.randint(0, len(self.sp_string) - 1)
        self.answer = ''
        for i in self.sp_string[self.random_index]:
            if i.isalpha():
                self.answer += i.lower()
        if 'æ' in self.answer:
            self.answer = self.answer.replace('æ', 'ае')

        self.sp_string[self.random_index] = "*пропуск*"
        self.pass_word_string.setText(' '.join(self.sp_string))

    def check_ans(self):
        if self.pass_word_input.text().lower() == self.answer.lower():
            self.pass_word_result.setText('ВЕРНО!')
            self.pass_word_result.setStyleSheet('background-color:green')
            # iteration_counter += 1
            if self.string_counter == len(self.cur_sp) - 1 and self.iteration_count < len(self.split_sp_text):
                self.iteration_count += 1
                self.pass_word_result.setText('УРА!Все!')
                self.pass_word_dalee.show()



            # string counter - номер строки
            elif self.string_counter < len(self.cur_sp) - 1:
                self.string_counter += 1
                self.pass_word_input.clear()
                self.pass_word()

        else:
            self.pass_word_result.setText('НЕВЕРНО!')
            self.pass_word_result.setStyleSheet('background-color:red')

    def new_win(self):
        if self.iteration_count < len(self.split_sp_text):
            self.tasRead = Task_read('\n'.join(self.text), self.iteration_count)
            self.tasRead.show()
            self.tasRead.text_fromBD()
            self.hide()
        if self.iteration_count == len(self.split_sp_text):
            self.hide()
            con = sqlite3.connect('BaseDate.sqlite')
            cur = con.cursor()
            res = cur.execute("""SELECT count FROM poetry_count""").fetchall()
            cur.execute(f"UPDATE poetry_count SET count = '{res[0][0] + 1}'")
            con.commit()
            QApplication.closeAllWindows()
            self.main_win = ChoiseFile()
            self.main_win.show()

    def click_podskazka(self):
        if self.podsk_cou > 0:
            self.pass_word_input.setText(self.answer)
            self.podsk_cou -= 1
            self.pass_word_podskazka_cou.setText(f'Подсказок осталось: {str(self.podsk_cou)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChoiseFile()
    ex.show()
    sys.exit(app.exec())
