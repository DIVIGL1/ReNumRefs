import sys
import mainform


class MyApplication:

    def __init__(self):
        self.mainwindow = mainform.MyWindow()
        self.mainwindow.show()

        sys.exit(self.mainwindow.app.exec_())