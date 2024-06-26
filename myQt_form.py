# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt5Project/Windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 740)
        MainWindow.setMinimumSize(QtCore.QSize(700, 740))
        MainWindow.setMaximumSize(QtCore.QSize(700, 740))
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowTitle("[ Замена ссылок в соответствии с их очерёдностью ]")
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_src = QtWidgets.QLineEdit(self.centralwidget)
        self.file_src.setGeometry(QtCore.QRect(10, 27, 311, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.file_src.setPalette(palette)
        self.file_src.setToolTip("")
        self.file_src.setStatusTip("")
        self.file_src.setWhatsThis("")
        self.file_src.setReadOnly(True)
        self.file_src.setObjectName("file_src")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 341, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.file_dst = QtWidgets.QLineEdit(self.centralwidget)
        self.file_dst.setGeometry(QtCore.QRect(330, 27, 361, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.file_dst.setPalette(palette)
        self.file_dst.setToolTip("")
        self.file_dst.setStatusTip("")
        self.file_dst.setWhatsThis("")
        self.file_dst.setReadOnly(True)
        self.file_dst.setObjectName("file_dst")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 53, 381, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 510, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.refs_found = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.refs_found.setEnabled(True)
        self.refs_found.setGeometry(QtCore.QRect(10, 70, 681, 181))
        self.refs_found.setMinimumSize(QtCore.QSize(300, 0))
        self.refs_found.setToolTip("")
        self.refs_found.setStatusTip("")
        self.refs_found.setWhatsThis("")
        self.refs_found.setStyleSheet("color: rgb(0, 0, 0);")
        self.refs_found.setReadOnly(True)
        self.refs_found.setPlainText("Выберите файл в браузере и с помощью мышки \"бросьте\" его на эту форму.")
        self.refs_found.setObjectName("refs_found")
        self.refs_error = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.refs_error.setEnabled(True)
        self.refs_error.setGeometry(QtCore.QRect(559, 527, 133, 51))
        self.refs_error.setMinimumSize(QtCore.QSize(0, 0))
        self.refs_error.setToolTip("")
        self.refs_error.setStatusTip("")
        self.refs_error.setWhatsThis("")
        self.refs_error.setStyleSheet("color: rgb(0, 0, 0);")
        self.refs_error.setReadOnly(True)
        self.refs_error.setObjectName("refs_error")
        self.refs_result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.refs_result.setEnabled(True)
        self.refs_result.setGeometry(QtCore.QRect(10, 303, 681, 191))
        self.refs_result.setMinimumSize(QtCore.QSize(300, 0))
        self.refs_result.setToolTip("")
        self.refs_result.setStatusTip("")
        self.refs_result.setWhatsThis("")
        self.refs_result.setStyleSheet("color: rgb(0, 0, 0);")
        self.refs_result.setReadOnly(True)
        self.refs_result.setPlainText("Выберите файл в браузере и с помощью мышки \"бросьте\" его на эту форму.")
        self.refs_result.setObjectName("refs_result")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 286, 321, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 510, 461, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.refs_not_used = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.refs_not_used.setEnabled(True)
        self.refs_not_used.setGeometry(QtCore.QRect(10, 527, 541, 121))
        self.refs_not_used.setMinimumSize(QtCore.QSize(300, 0))
        self.refs_not_used.setToolTip("")
        self.refs_not_used.setStatusTip("")
        self.refs_not_used.setWhatsThis("")
        self.refs_not_used.setStyleSheet("color: rgb(0, 0, 0);")
        self.refs_not_used.setReadOnly(True)
        self.refs_not_used.setPlainText("Выберите файл в браузере и с помощью мышки \"бросьте\" его на эту форму.")
        self.refs_not_used.setObjectName("refs_not_used")
        self.progressBar1 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar1.setGeometry(QtCore.QRect(10, 675, 681, 23))
        self.progressBar1.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar1.setMaximumSize(QtCore.QSize(716, 16777215))
        self.progressBar1.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #d5d5d5;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #d5d5d5;\n"
"    width: 20px;\n"
"}")
        self.progressBar1.setProperty("value", 24)
        self.progressBar1.setFormat("")
        self.progressBar1.setObjectName("progressBar1")
        self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar2.setGeometry(QtCore.QRect(10, 700, 681, 10))
        self.progressBar2.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar2.setMaximumSize(QtCore.QSize(716, 16777215))
        self.progressBar2.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #d5d5d5;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #d5d5d5;\n"
"    width: 20px;\n"
"}")
        self.progressBar2.setProperty("value", 24)
        self.progressBar2.setFormat("")
        self.progressBar2.setObjectName("progressBar2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 267, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.befor_num = QtWidgets.QLineEdit(self.centralwidget)
        self.befor_num.setGeometry(QtCore.QRect(230, 266, 31, 21))
        self.befor_num.setToolTip("")
        self.befor_num.setStatusTip("")
        self.befor_num.setWhatsThis("")
        self.befor_num.setReadOnly(False)
        self.befor_num.setObjectName("befor_num")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 267, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.after_num = QtWidgets.QLineEdit(self.centralwidget)
        self.after_num.setGeometry(QtCore.QRect(321, 266, 31, 21))
        self.after_num.setToolTip("")
        self.after_num.setStatusTip("")
        self.after_num.setWhatsThis("")
        self.after_num.setReadOnly(False)
        self.after_num.setObjectName("after_num")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 250, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.del_unused_refs = QtWidgets.QCheckBox(self.centralwidget)
        self.del_unused_refs.setGeometry(QtCore.QRect(10, 650, 541, 20))
        self.del_unused_refs.setStyleSheet("QCheckBox::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 0px;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.del_unused_refs.setObjectName("del_unused_refs")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 494, 701, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(559, 580, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.refs_dubls = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.refs_dubls.setEnabled(True)
        self.refs_dubls.setGeometry(QtCore.QRect(559, 597, 133, 51))
        self.refs_dubls.setMinimumSize(QtCore.QSize(0, 0))
        self.refs_dubls.setToolTip("")
        self.refs_dubls.setStatusTip("")
        self.refs_dubls.setWhatsThis("")
        self.refs_dubls.setStyleSheet("color: rgb(0, 0, 0);")
        self.refs_dubls.setReadOnly(True)
        self.refs_dubls.setObjectName("refs_dubls")
        self.sotr_by_alphabetically = QtWidgets.QCheckBox(self.centralwidget)
        self.sotr_by_alphabetically.setGeometry(QtCore.QRect(370, 285, 331, 20))
        self.sotr_by_alphabetically.setStyleSheet("QCheckBox::indicator {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 0px;\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.sotr_by_alphabetically.setObjectName("sotr_by_alphabetically")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.file_src.setText(_translate("MainWindow", "Выберите файл в браузере и с помощью мышки \"бросьте\" его на эту форму."))
        self.label.setText(_translate("MainWindow", "Имя документа (файла):"))
        self.label_2.setText(_translate("MainWindow", "Имя обработанного (итогового) документа (файла):"))
        self.file_dst.setText(_translate("MainWindow", "Выберите файл в браузере и с помощью мышки \"бросьте\" его на эту форму."))
        self.label_3.setText(_translate("MainWindow", "Обнаружен список литературы:"))
        self.label_4.setText(_translate("MainWindow", "Ошибки замены:"))
        self.label_5.setText(_translate("MainWindow", "Итоговая сортировка списка литературы:"))
        self.label_6.setText(_translate("MainWindow", "Не использованные в тексте источники из списка литературы:"))
        self.label_7.setText(_translate("MainWindow", "Ограничители номера строки слева:"))
        self.label_8.setText(_translate("MainWindow", "справа:"))
        self.after_num.setText(_translate("MainWindow", "."))
        self.del_unused_refs.setText(_translate("MainWindow", "Удалить не использванную литературу из списка литературы в итоговом файле"))
        self.label_9.setText(_translate("MainWindow", "Дубли меток в списке:"))
        self.sotr_by_alphabetically.setText(_translate("MainWindow", "Сортировать литературу по алфавиту (сначала кириллица)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
