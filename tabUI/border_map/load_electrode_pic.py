#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 18:14
# @Author: xuyongchuan
# @File  : load_electrode_pic.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class LoadElectrodePic(QWidget):
    def __init__(self, parent=None):
        super(LoadElectrodePic, self).__init__(parent)
        self.pic_path = ''
        self.load_pic_button = QPushButton()
        self.pic_label = QLabel()

        self.setupUI()
        self.pic = None

    def setupUI(self):
        layout = QVBoxLayout()
        self.load_pic_button.setText('加载电极图片')
        self.load_pic_button.setObjectName('upload_button')
        self.load_pic_button.setFixedSize(150, 50)
        self.load_pic_button.clicked.connect(self.load_pic)

        layout.addWidget(self.load_pic_button, alignment=Qt.AlignLeft)
        layout.addWidget(self.pic_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.setStyleSheet('''
        QPushButton#upload_button{   
                color:black;
                border:none;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        QPushButton#upload_button:hover{border-right:4px solid red;font-weight:700;}
        ''')

    def get_pic_path(self, pic_path):
        self.pic_path = pic_path
        print(self.pic_path)

    def load_pic(self):

        if self.pic_path:
            self.pic_label.setPixmap(QPixmap(self.pic_path))
            self.pic_label.setScaledContents(True)  # 让图片自适应label的大小

            self.pic = self.pic_label.pixmap()
            QMessageBox.information(self, '消息', '电极分布图片加载完成', QMessageBox.Ok)
        else:
            QMessageBox.information(self, '消息', '未找到电极分布图片', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadElectrodePic()
    win.show()
    sys.exit(app.exec_())