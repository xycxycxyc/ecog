#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/21 22:41
# @Author: xuyongchuan
# @File  : generate_function_map.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class GenerateFunctionMap(QWidget):
    def __init__(self, parent=None):
        super(GenerateFunctionMap, self).__init__(parent)
        self.show_border_map_bt = QPushButton()
        self.border_map_label = QLabel()
        self.setupUI()
        self.pic = None

    def setupUI(self):
        layout = QVBoxLayout()
        self.show_border_map_bt.setText('生成功能区地形图')
        self.show_border_map_bt.setFixedSize(170, 50)

        self.show_border_map_bt.setObjectName('show_function_map_bt')
        self.show_border_map_bt.clicked.connect(self.show_function_map)

        layout.addWidget(self.show_border_map_bt, alignment=Qt.AlignLeft)
        layout.addWidget(self.border_map_label, alignment=Qt.AlignCenter)
        self.setStyleSheet('''
        QPushButton#show_function_map_bt{   
                color:black;
                border:none;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        QPushButton#show_function_map_bt:hover{border-right:4px solid red;font-weight:700;}
        ''')

        self.setLayout(layout)

    def show_function_map(self):
        if not self.pic:
            QMessageBox.warning(self, '警告', '请先生成功能区地形图', QMessageBox.Ok)
        else:
            self.border_map_label.setPixmap(self.pic)
            self.border_map_label.setScaledContents(True)

    def set_pixmap(self, pixmap):
        if not pixmap:
            pass
        else:
            self.pic = pixmap


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GenerateFunctionMap()
    win.show()
    sys.exit(app.exec_())