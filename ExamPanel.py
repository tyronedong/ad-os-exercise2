import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from mainPanel import Ui_exam
import socket

class Exam(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_exam()                     # 初始化ui界面
        self.ui.setupUi(self)

        res, code = self.init_connection()      # 建立socket连接
        if not res:
            sys.exit(code)

        self.tableWidget = self.ui.tableWidget  # 赋值以方便操作
        self.examRunning = False

    def init_connection(self):
        # return True, None
        host = 'localhost'
        port = 8888

        try:
            self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname(host)
            self.socket_.connect((remote_ip, port))
            return True, None
        except socket.error as err:
            print(err)
            return False, err.args[0]

    def startExamButtonClicked(self):
        if self.examRunning:
            return
        userName = self.ui.userTBox.text()
        count = self.ui.qusNumBox.value()
        if count <= 0 or userName == '':
            return

        self.socket_.sendall(bytes(userName, encoding='utf-8'))         # 发送名字
        self.socket_.sendall(bytes(str(count), encoding='utf-8'))       # 发送题数

        self.questList = []
        for i in range(count):
            question = str(self.socket_.recv(1024), encoding='utf-8')   # 接收问题
            self.questList.append(question)
            print('%s: %s' % (i + 1, question))
            self.socket_.sendall(bytes('^EOF^', encoding='utf-8'))    # 终止服务端的阻塞

        self.populateTable(self.questList)
        self.ui.examResultTBox.setText('')
        self.examRunning = True

    def submitButtonClicked(self):
        if not self.examRunning:
            return
        for row in range(len(self.questList)):
            item = self.tableWidget.item(row, 2)
            if item is None:
                answer = 'empty'
            else:
                answer = item.text().strip()
            self.socket_.sendall(bytes(answer, encoding='utf-8'))   # 发送答案
            self.socket_.recv(1024)
            print(item)
        result = str(self.socket_.recv(1024), encoding='utf-8')     # 接收结果
        resultList = result.split('\t')
        right = 0
        for row, res in enumerate(resultList):                      # 展示结果
            self.tableWidget.setItem(row, 0, QTableWidgetItem(res))
            if res == '正确':
                right += 1
        self.ui.examResultTBox.setText('%s/%s'%(right, len(resultList)))
        self.examRunning = False

    def populateTable(self, questionList):
        self.tableWidget.clear()
        # self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(len(questionList))
        headers = ["Judge", "Question", "Answer"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        for row, question in enumerate(questionList):
            item = QTableWidgetItem(question)
            item.setData(Qt.UserRole, id(question))
            self.tableWidget.setItem(row, 1, item)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.resizeColumnsToContents()

        self.tableWidget.setColumnWidth(1, 240)     # 设置列宽需要放到最后
        self.tableWidget.setColumnWidth(2, 99)