#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 18:14
# @Author: xuyongchuan
# @File  : load_pic.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class LoadPic(QWidget):
    def __init__(self, parent=None):
        super(LoadPic, self).__init__(parent)
        self.load_pic_button = QPushButton()
        self.pic_label = QLabel()

        self.setupUI()
        self.pic = None

    def setupUI(self):
        layout = QVBoxLayout()
        self.load_pic_button.setText('加载电极图片')
        self.load_pic_button.clicked.connect(self.load_pic)

        layout.addWidget(self.load_pic_button, alignment=Qt.AlignLeft)
        layout.addWidget(self.pic_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def load_pic(self):
        pic_path, _ = QFileDialog.getOpenFileName(self, '加载电极分布图片', '.', '图像文件(*.png, *.jpg)')
        if pic_path:
            print(pic_path)
            self.pic_label.setPixmap(QPixmap(pic_path))
            self.pic_label.setScaledContents(True)  # 让图片自适应label的大小

            self.pic = self.pic_label.pixmap()
            QMessageBox.information(self, '消息', '电极分布图片加载完成', QMessageBox.Ok)
        else:
            print('电极分布图片未加载')

    def get_pixmap(self):
        if self.pic_label.pixmap():
            return self.pic_label.pixmap()
        else:
            QMessageBox.information(self, '消息', '请先导入电极分布图片', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadPic()
    win.show()
    sys.exit(app.exec_())