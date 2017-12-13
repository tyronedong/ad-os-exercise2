import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from PyQt5.QtGui import QIcon
from mainPanel import Ui_exam

class Exam(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_exam()
        self.ui.setupUi(self)

    def startExamButtonClicked(self):
        # userName = self.ui.userTBox.getText()
        pass
        #print()

    def submitButtonClicked(self):
        pass
