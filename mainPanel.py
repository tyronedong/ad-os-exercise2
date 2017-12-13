# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPanel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exam(object):
    def setupUi(self, exam):
        exam.setObjectName("exam")
        exam.resize(442, 551)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        exam.setFont(font)
        self.label = QtWidgets.QLabel(exam)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(exam)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.qusNumBox = QtWidgets.QSpinBox(exam)
        self.qusNumBox.setGeometry(QtCore.QRect(260, 20, 51, 31))
        self.qusNumBox.setObjectName("qusNumBox")
        self.startExamButton = QtWidgets.QPushButton(exam)
        self.startExamButton.setGeometry(QtCore.QRect(340, 20, 81, 31))
        self.startExamButton.setObjectName("startExamButton")
        self.submitButton = QtWidgets.QPushButton(exam)
        self.submitButton.setGeometry(QtCore.QRect(20, 480, 75, 31))
        self.submitButton.setObjectName("submitButton")
        self.label_4 = QtWidgets.QLabel(exam)
        self.label_4.setGeometry(QtCore.QRect(230, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.userTBox = QtWidgets.QLineEdit(exam)
        self.userTBox.setGeometry(QtCore.QRect(60, 20, 131, 31))
        self.userTBox.setObjectName("userTBox")
        self.examResultTBox = QtWidgets.QLineEdit(exam)
        self.examResultTBox.setGeometry(QtCore.QRect(310, 480, 111, 31))
        self.examResultTBox.setObjectName("examResultTBox")
        # self.tableView = QtWidgets.QTableView(exam)
        # self.tableView.setGeometry(QtCore.QRect(20, 60, 401, 411))
        # self.tableView.setObjectName("tableView")
        self.tableWidget = QtWidgets.QTableWidget(exam)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 401, 411))
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(exam)
        self.startExamButton.clicked.connect(exam.startExamButtonClicked)
        self.submitButton.clicked.connect(exam.submitButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(exam)

    def retranslateUi(self, exam):
        _translate = QtCore.QCoreApplication.translate
        exam.setWindowTitle(_translate("exam", "Welcome to the exam"))
        self.label.setText(_translate("exam", "姓名"))
        self.label_2.setText(_translate("exam", "题数"))
        self.startExamButton.setText(_translate("exam", "开始测验"))
        self.submitButton.setText(_translate("exam", "提交答案"))
        self.label_4.setText(_translate("exam", "测验结果"))