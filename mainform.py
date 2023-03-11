# -*- coding: utf-8 -*-
# pyuic5 -x Qt5Project/Windows.ui -o myQt_form.py
import os
import sys

from PyQt5 import QtGui, QtWidgets

from myconstants import *
import mydocfuncs
import myQt_form


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
        all_ordered_refs = mydocfuncs.get_all_refs_in_text(doc_object)
        all_refs_list = mydocfuncs.find_refs_list(doc_object)

        full_list = ""
        for element in all_refs_list:
            full_list = full_list + element[2] + '\n'

        self.ui.refs_found.setPlainText(full_list)

        mydocfuncs.replace_ref_paragraphs(doc_object, all_ordered_refs, all_refs_list)

        errors = mydocfuncs.get_refs_errors(doc_object, all_ordered_refs)
        if errors:
            errors_in_text = f"Не исправленных ссылок: {len(errors)} шт.:\n"
            for element in errors:
                errors_in_text = errors_in_text + element + '\n'

            self.ui.refs_error.setPlainText(errors_in_text)
        else:
            self.ui.refs_error.setPlainText("- нет -")

        mydocfuncs.save_docx_object(doc_object, file_dst_name)


if __name__ == "__main__":
    pass
