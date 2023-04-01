# -*- coding: utf-8 -*-
# pyuic5 -x Qt5Project/Windows.ui -o myQt_form.py
import os
import sys

from PyQt5 import QtGui, QtWidgets

from myconstants import *
import mydocfuncs
import myQt_form
from myutils import (
    load_param, save_param
)


class QtMainWindow(myQt_form.Ui_MainWindow):

    def __init__(self):
        pass

    def setup_form(self):
        pass


class MyWindow(QtWidgets.QMainWindow):
    ui = None

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = QtMainWindow()
        self.ui.setupUi(self)

        self.ui.refs_found.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.refs_error.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.refs_result.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.refs_not_used.setWordWrapMode(QtGui.QTextOption.NoWrap)

        # Установим исходные (сохранённые) координаты и размеры:
        data = load_param(PARAMETER_SAVED_MAIN_WINDOW_POZ, "")
        if data:
            self.restoreGeometry(data)

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

        file_src_name = os.path.basename(docx_files[0])
        file_dst_name = os.path.splitext(file_src_name)[0] + ' (new)' + os.path.splitext(file_src_name)[1]
        self.ui.file_src.setText(file_src_name)
        self.ui.file_dst.setText(file_dst_name)

        file_src_name = docx_files[0]
        file_dst_name = os.path.splitext(file_src_name)[0] + ' (new)' + os.path.splitext(file_src_name)[1]

        doc_object = mydocfuncs.get_docx_object(docx_files[0])
        all_ordered_refs = mydocfuncs.get_all_refs(doc_object)
        all_refs_in_list = mydocfuncs.find_refs_in_list(doc_object)

        # Подготовим полный список ссылок и выведем его для информации на форму:
        full_list = ""
        for element in all_refs_in_list:
            full_list = full_list + element[2] + '\n'

        self.ui.refs_found.setPlainText(full_list)

        # В полном списке ссылок из текста могут оказаться ссылки,
        # которых нет в списке литературы - это ошибки.
        # Найдём их, сохраним и удалим.
        all_only_refs_list = [x[0] for x in all_refs_in_list]
        good_ordered_refs = all_ordered_refs.copy()
        for element in all_ordered_refs:
            if element not in all_only_refs_list:
                good_ordered_refs.remove(element)

        # В полном списке литературы могут оказаться ссылки,
        # которые не используются в тексте. Найдём их:
        all_refs_only_in_text = mydocfuncs.get_all_refs(doc_object, p_only_in_text=True)
        all_unused_refs = all_refs_in_list.copy()
        for element in all_refs_in_list:
            if element[0] in all_refs_only_in_text:
                all_unused_refs.remove(element)

        # Отобразим их на экране для информации.
        if len(all_unused_refs):
            self.ui.refs_not_used.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.refs_not_used.setPlainText('\n'.join([x[2] for x in all_unused_refs]))
        else:
            self.ui.refs_not_used.setStyleSheet("color: rgb(0, 0, 0);")
            self.ui.refs_not_used.setPlainText(TEXT_NO_INFORMATION)

        # В итоге обрабатываем только те ссылки,
        # для которых есть запись в списке литературы:
        refs_result = mydocfuncs.replace_ref_paragraphs(doc_object, good_ordered_refs, all_refs_in_list)
        self.ui.refs_result.setPlainText('\n'.join(refs_result))

        # Выведем для информации на форму список ссылок из текста (ошибки),
        # для которых не нашлась соответствующая ссылка в списке литературы
        # или по каким-то причинам не произошла замена:
        errors = mydocfuncs.get_refs_errors(doc_object, all_ordered_refs)
        if errors:
            errors_in_text = f"Не исправлено: {len(errors)} шт.:\n"
            for element in errors:
                errors_in_text = errors_in_text + element + '\n'

            self.ui.refs_error.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.refs_error.setPlainText(errors_in_text)
        else:
            self.ui.refs_error.setStyleSheet("color: rgb(0, 0, 0);")
            self.ui.refs_error.setPlainText(TEXT_NO_INFORMATION)

        # Сохраним копию документа с исправленными ссылками:
        mydocfuncs.save_docx_object(doc_object, file_dst_name)


if __name__ == "__main__":
    pass
