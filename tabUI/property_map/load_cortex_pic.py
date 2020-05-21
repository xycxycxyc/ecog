#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/21 22:29
# @Author: xuyongchuan
# @File  : load_cortex_pic.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class LoadCortexPic(QWidget):
    def __init__(self, parent=None):
        super(LoadCortexPic, self).__init__(parent)
        self.load_pic_button = QPushButton()
        self.pic_label = QLabel()

        self.setupUI()
        self.pic = None

    def setupUI(self):
        layout = QVBoxLayout()
        self.load_pic_button.setText('加载皮质图片')
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

    def load_pic(self):
        pic_path, _ = QFileDialog.getOpenFileName(self, '加载皮质图片', '.', '图像文件(*.png, *.jpg)')
        if pic_path:
            print(pic_path)
            self.pic_label.setPixmap(QPixmap(pic_path))
            self.pic_label.setScaledContents(True)  # 让图片自适应label的大小

            self.pic = self.pic_label.pixmap()
            QMessageBox.information(self, '消息', '皮质图片加载完成', QMessageBox.Ok)
        else:
            print('皮质图片未加载')

    def get_pixmap(self):
        if self.pic_label.pixmap():
            return self.pic_label.pixmap()
        else:
            QMessageBox.information(self, '消息', '请先导入皮质图片', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadCortexPic()
    win.show()
    sys.exit(app.exec_())