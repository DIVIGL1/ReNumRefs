# -*- coding: utf-8 -*-
# pyuic5 -x Qt5Project/Windows.ui -o myQt_form.py
import os
import sys
import time
import threading

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

from myconstants import *
import mydocfuncs
import myQt_form
from myutils import (
    load_param, save_param
)


def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper


class Communicate(QObject):
    commander = pyqtSignal(str)


@thread
def document_processing(ui, file_src_name, file_dst_name):
    ui.status_bar_secs = 0
    ui.delay = 0.1

    # Получим документ
    doc_object = mydocfuncs.get_docx_object(file_src_name)

    ui.set_form_element_text("status bar", "Получаем список всех ссылок в документе...")
    all_ordered_refs = mydocfuncs.get_all_refs(doc_object)

    ui.set_form_element_text("status bar", "Получаем список всех ссылок в списке литературы...")
    all_refs_in_list = mydocfuncs.find_refs_in_list(doc_object)

    # Подготовим полный список ссылок и выведем его для информации на форму:
    ui.set_form_element_text("status bar", "Обрабатываем список всех ссылок...")
    full_list = ""
    for element in all_refs_in_list:
        full_list = full_list + element[2] + '\n'

    ui.set_form_element_text("refs_found", full_list)

    # В полном списке ссылок из текста могут оказаться ссылки,
    # которых нет в списке литературы - это ошибки.
    # Найдём их, сохраним и удалим.
    ui.set_form_element_text("status bar", "Ищем ссылки, которых нет в списке литературы...")
    all_only_refs_list = [x[0] for x in all_refs_in_list]
    good_ordered_refs = all_ordered_refs.copy()
    for element in all_ordered_refs:
        if element not in all_only_refs_list:
            good_ordered_refs.remove(element)

    # В полном списке литературы могут оказаться ссылки,
    # которые не используются в тексте. Найдём их:
    ui.set_form_element_text("status bar", "Ищем литературу, на которую нет ссылок...")
    all_refs_only_in_text = mydocfuncs.get_all_refs(doc_object, p_only_in_text=True)
    all_unused_refs = []
    for element in all_refs_in_list:
        if element[0] in all_refs_only_in_text:
            pass
        else:
            all_unused_refs.append(["", "", element[2]])

    # Отобразим их на экране для информации.
    if len(all_unused_refs):
        ui.set_form_element_text("refs_not_used", '\n'.join([x[2] for x in all_unused_refs]))
    else:
        ui.set_form_element_text("refs_not_used", TEXT_NO_INFORMATION)

    # В итоге обрабатываем только те ссылки,
    # для которых есть запись в списке литературы:
    ui.set_form_element_text("status bar", "Сортируем литературу и заменяем ссылки на номера...")
    refs_result = mydocfuncs.replace_ref_paragraphs(ui, doc_object, good_ordered_refs, all_refs_in_list)
    ui.set_form_element_text("refs_result", '\n'.join(refs_result))

    # Выведем для информации на форму список ссылок из текста (ошибки),
    # для которых не нашлась соответствующая ссылка в списке литературы
    # или по каким-то причинам не произошла замена:
    ui.set_form_element_text("status bar", "Выведем ошибки замены...")
    errors = mydocfuncs.get_refs_errors(doc_object, all_ordered_refs)
    if errors:
        errors_in_text = f"Не исправлено: {len(errors)} шт.:\n"
        for element in errors:
            errors_in_text = errors_in_text + element + '\n'

        ui.set_form_element_text("refs_error", errors_in_text)
    else:
        ui.set_form_element_text("refs_error", TEXT_NO_INFORMATION)

    # Сохраним копию документа с исправленными ссылками:
    ui.set_form_element_text("status bar", "Сохраняем документ...")
    mydocfuncs.save_docx_object(doc_object, file_dst_name)
    ui.status_bar_secs = 3
    ui.set_form_element_text("status bar", "Завершено")


class QtMainWindow(myQt_form.Ui_MainWindow):
    status_bar_secs = 0
    delay = 0
    saved_text = ""

    def __init__(self):
        self.parent = None

    def setup_form(self):
        pass

    def set_form_element_text(self, element, text):
        self.saved_text = text
        self.parent.communicate.commander.emit(element)
        time.sleep(self.delay)


class MyWindow(QtWidgets.QMainWindow):
    ui = None

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = QtMainWindow()
        self.ui.parent = self
        self.ui.setupUi(self)

        self.ui.refs_found.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.refs_error.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.refs_result.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.refs_not_used.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.progressBar1.setValue(0)
        self.ui.progressBar2.setValue(0)

        self.communicate = Communicate()
        self.communicate.commander.connect(lambda command: self.communication_handler(command))

        # Установим исходные (сохранённые) координаты и размеры:
        data = load_param(PARAMETER_SAVED_MAIN_WINDOW_POZ, "")
        if data:
            self.restoreGeometry(data)

        self.ui.befor_num.setText(load_param(BEFORE_NUM_PART_SAVE_NAME, BEFORE_NUM_PART_DEFAULT_VALUE))
        self.ui.after_num.setText(load_param(AFTER_NUM_PART_SAVE_NAME, AFTER_NUM_PART_DEFAULT_VALUE))

    def communication_handler(self, element):
        self.ui.progressBar1.setValue(self.ui.progressBar1.value() + 1)
        if element == "status bar":
            self.ui.statusBar.showMessage(self.ui.saved_text, self.ui.status_bar_secs * 1000)
            return
        if element == "refs_found":
            self.ui.refs_found.setPlainText(self.ui.saved_text)
            return
        if element == "refs_result":
            self.ui.refs_result.setPlainText(self.ui.saved_text)
            return
        if element == "refs_error":
            self.ui.refs_error.setPlainText(self.ui.saved_text)

            if self.ui.saved_text == TEXT_NO_INFORMATION:
                self.ui.refs_error.setStyleSheet("color: rgb(0, 0, 0);")
            else:
                self.ui.refs_error.setStyleSheet("color: rgb(255, 0, 0);")

            return
        if element == "refs_not_used":
            self.ui.refs_not_used.setPlainText(self.ui.saved_text)

            if self.ui.saved_text == TEXT_NO_INFORMATION:
                self.ui.refs_not_used.setStyleSheet("color: rgb(0, 0, 0);")
            else:
                self.ui.refs_not_used.setStyleSheet("color: rgb(255, 0, 0);")
            return

    def moveEvent(self, event):
        super(MyWindow, self).moveEvent(event)
        data = self.saveGeometry()
        save_param(PARAMETER_SAVED_MAIN_WINDOW_POZ, data)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Из полученных файлов выберем только с расширением docx:
        docx_files = [u.toLocalFile() for u in event.mimeData().urls() if u.toLocalFile()[-5:].lower() == FILE_EXTENSION.lower()]

        if not docx_files:
            return

        # Обнулим значения "градусников":
        self.ui.progressBar1.setMinimum(0)
        self.ui.progressBar1.setMaximum(13)
        self.ui.progressBar1.setValue(0)
        self.ui.progressBar2.setValue(0)

        # "Обнулим" значения текстовых полей:
        self.ui.refs_not_used.setStyleSheet("color: rgb(0, 0, 0);")
        self.ui.refs_error.setStyleSheet("color: rgb(0, 0, 0);")
        self.ui.refs_found.setPlainText("")
        self.ui.refs_result.setPlainText("")
        self.ui.refs_not_used.setPlainText(TEXT_NO_INFORMATION)
        self.ui.refs_error.setPlainText(TEXT_NO_INFORMATION)

        # Выведем первое сообщение:
        self.ui.statusBar.showMessage("Начинаем. Открываем файл...")

        # Получим имя файла с расширением:
        file_src_name = os.path.basename(docx_files[0])
        self.ui.file_src.setText(file_src_name)

        # Сформируем имя нового файла, в котором будут содержаться замены:
        file_dst_name = os.path.splitext(file_src_name)[0] + TEXT_APPENDIX_FOR_NEW_FILE + os.path.splitext(file_src_name)[1]
        self.ui.file_dst.setText(file_dst_name)

        file_src_name = docx_files[0]
        file_dst_name = os.path.splitext(file_src_name)[0] + TEXT_APPENDIX_FOR_NEW_FILE + os.path.splitext(file_src_name)[1]

        document_processing(self.ui, file_src_name, file_dst_name)

    def keyReleaseEvent(self, event):
        if self.ui.befor_num.isModified():
            self.ui.befor_num.setModified(False)
            save_param(BEFORE_NUM_PART_SAVE_NAME, self.ui.befor_num.text())
        if self.ui.after_num.isModified():
            self.ui.after_num.setModified(False)
            save_param(AFTER_NUM_PART_SAVE_NAME, self.ui.after_num.text())


if __name__ == "__main__":
    pass
