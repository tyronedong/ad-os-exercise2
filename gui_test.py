import sys
from PyQt5.QtWidgets import QApplication, QWidget
from mainPanel import *
from ExamPanel import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # w = QWidget()
    #
    # ui = Ui_exam()
    # ui.setupUi(w)
    main = Exam()
    main.show()

    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Simple')
    # w.show()

    sys.exit(app.exec_())