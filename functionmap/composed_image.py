#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/27 16:04
# @Author: xuyongchuan
# @File  : composed_image.py

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# from functionmap.function_map import FunctionMapPart
import functionmap.function_map


class ComposedImage(QDialog):
    def __init__(self, parent=None):
        super(ComposedImage, self).__init__(parent)
        self.composed_title_lb = QLabel()
        self.composed_image_lb = QLabel()
        self.save_image_bt = QPushButton()
        self.setupUI()

    def setupUI(self):
        self.resize(600, 400)
        self.setWindowTitle('功能区地形图')
        composed_lb_style = 'QLabel{color:rgb(0, 0, 0, 255);font-size:30px;font-weight:bold;font-family:Arial;}'
        composed_bt_style = 'QPushButton{color:rgb(0, 0, 0, 255);font-size:20px;font-weight:bold;font-family:Arial;}'

        self.composed_title_lb.setText('功能区地形图')
        self.composed_title_lb.setStyleSheet(composed_lb_style)

        self.composed_image_lb.setFixedSize(400, 300)

        self.save_image_bt.setText('保存')
        self.save_image_bt.setStyleSheet(composed_bt_style)
        self.save_image_bt.setFixedSize(100, 40)
        self.save_image_bt.clicked.connect(self.save_composed_image)

        composed_vlayout = QVBoxLayout()
        composed_vlayout.addWidget(self.composed_title_lb, alignment=Qt.AlignCenter)
        composed_vlayout.addWidget(self.composed_image_lb, alignment=Qt.AlignCenter)
        composed_vlayout.addWidget(self.save_image_bt, alignment=Qt.AlignRight)

        self.setLayout(composed_vlayout)

    def show_composed_image(self, path):
        self.composed_image_lb.setPixmap(QPixmap(path))

    def save_composed_image(self):
        # a = FunctionMapPart.get()
        # print(a)
        if not self.composed_image_lb.pixmap():
            QMessageBox.about(self, '提示', '请先合成功能区地形图')
        else:
            result = self.composed_image_lb.pixmap()

            fname, ftype = QFileDialog.getSaveFileName(self, 'save file', './', '图像文件(*.png, *.jpg)')
            if fname:
                result.save(fname)
                QMessageBox.information(self, '提示', '保存成功', QMessageBox.Yes)

    # 静态方法传参测试函数
    def testa(self):
        # fun = functionmap.function_map.FunctionMapPart()
        # fun.get1()
        # a = fun.get()
        a = functionmap.function_map.FunctionMapPart().get()
        print(a)

    # 信号与槽传参测试
    def process_fun(self):
        fun = functionmap.function_map.FunctionMapPart()
        fun.test_signal.connect(self.process)
        fun.emit_test_signal()

    def process(self, mystr, a, b):
        print(mystr)
        print(a+b)


if __name__ == '__main__':
    composed_app = QApplication(sys.argv)
    composed_win = ComposedImage()
    # composed_win.testa()  # 静态方法传参测试
    composed_win.process_fun()  #信号与槽传参测试
    composed_win.show()
    sys.exit(composed_app.exec_())