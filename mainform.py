# -*- coding: utf-8 -*-
# pyuic5 -x Qt5Project/Windows.ui -o myQt_form.py
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

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

        doc_object = mydocfuncs.get_docx_object(file_src_name)
        all_ordered_refs = mydocfuncs.get_all_refs_in_text(doc_object)
        all_refs_list = mydocfuncs.find_refs_list(doc_object)
        mydocfuncs.replace_ref_paragraphs(doc_object, all_ordered_refs, all_refs_list)

        mydocfuncs.save_docx_object(doc_object, file_dst_name)


if __name__ == "__main__":
    pass
