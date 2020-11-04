#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/6/27 20:01
# @Author: xuyongchuan
# @File  : test_status_bar.py


'''
创建和使用状态栏
'''

import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("状态栏演示")
        self.resize(300, 200)
        self.btn1 = QPushButton('1111')
        self.btn2 = QPushButton('22222')
        self.btn3 = QPushButton('33333')

        # file.triggered.connect(self.processTrigger)

        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.main_layout.addWidget(self.btn1)
        self.main_layout.addWidget(self.btn2)
        self.main_layout.addWidget(self.btn3)

        self.main_widget.setLayout(self.main_layout)

        self.statusBar.showMessage(" 菜单被点击了")
        # self.statusBar.clearMessage()
        # self.statusBar.showMessage(" 菜单被点击了", 5000)


    # def processTrigger(self, q):
    #     if q.text() == "show":
    #         self.statusBar.showMessage(q.text() + " 菜单被点击了", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec_())
