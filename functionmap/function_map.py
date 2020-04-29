#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/23 11:42
# @Author: xuyongchuan
# @File  : function_map


import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QHBoxLayout, QPushButton, \
    QWidget, QLabel, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from bordermap.border_map import BorderMapPart
from propertymap.property_map import PropertyMapPart
from functionmap.composed_image import ComposedImage


class FunctionMapPart(QDialog):

    def __init__(self, parent=None):
        super(FunctionMapPart, self).__init__(parent)
        self.function_title_lb = QLabel()
        self.image_lb1 = QLabel()
        self.image_lb2 = QLabel()
        self.load_bd_image_bt = QPushButton()
        self.load_pp_image_bt = QPushButton()
        self.compose_bt = QPushButton()
        self.a = []
        self.setupUI()

    def setupUI(self):
        self.resize(800, 600)
        self.setWindowTitle('功能区地形图部分')
        function_lb_style = 'QLabel{color:rgb(0, 0, 0, 255);font-size:30px;font-weight:bold;font-family:Arial;}'
        function_bt_style = 'QPushButton{color:rgb(0, 0, 0, 255);font-size:20px;font-weight:bold;font-family:Arial;}'

        self.function_title_lb.setText('功能区地形图部分')
        self.function_title_lb.setStyleSheet(function_lb_style)

        self.load_bd_image_bt.setText('加载功能区边界定位图')
        self.load_bd_image_bt.setStyleSheet(function_bt_style)
        self.load_bd_image_bt.setFixedSize(230, 40)
        self.load_bd_image_bt.clicked.connect(self.load_bd_image)

        self.image_lb1.setFixedSize(400, 300)
        self.image_lb2.setFixedSize(400, 300)

        self.load_pp_image_bt.setText('加载功能区属性定位图')
        self.load_pp_image_bt.setStyleSheet(function_bt_style)
        self.load_pp_image_bt.setFixedSize(230, 40)
        self.load_pp_image_bt.clicked.connect(self.load_pp_image)

        self.compose_bt.setText('生成功能区地形图')
        self.compose_bt.setStyleSheet(function_bt_style)
        self.compose_bt.setFixedSize(200, 40)
        self.compose_bt.clicked.connect(self.compose_image)

        function_hlayout1 = QHBoxLayout()
        function_hlayout1.addWidget(self.load_bd_image_bt)
        function_hlayout1.addWidget(self.load_pp_image_bt)
        dialog1 = QDialog()
        dialog1.setLayout(function_hlayout1)

        function_hlayout2 = QHBoxLayout()
        function_hlayout2.addWidget(self.image_lb1)
        function_hlayout2.addWidget(self.image_lb2)
        dialog2 = QDialog()
        dialog2.setLayout(function_hlayout2)

        function_vlayout = QVBoxLayout()
        function_vlayout.addWidget(self.function_title_lb, alignment=Qt.AlignCenter)
        function_vlayout.addWidget(dialog1)
        function_vlayout.addWidget(dialog2)
        function_vlayout.addWidget(self.compose_bt, alignment=Qt.AlignRight)

        self.setLayout(function_vlayout)
        # self.setCentralWidget()

    def load_bd_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '加载功能区边界定位图', '.', '图像文件(*.png, *.jpg)')
        # print(file_name)  # 文件路径及文件名
        # self.image_label1.setPixmap(QPixmap(file_name).scaled(400, 300))
        self.image_lb1.setPixmap(QPixmap(file_name))
        self.image_lb1.setScaledContents(True)  # 让图片自适应label的大小

    def load_pp_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '加载功能区属性定位图', '.', '图像文件(*.png, *.jpg)')
        # self.image_label1.setPixmap(QPixmap(file_name).scaled(400, 300))
        self.image_lb2.setPixmap(QPixmap(file_name))
        self.image_lb2.setScaledContents(True)  # 让图片自适应label的大小

    def compose_image(self):
        if not (self.image_lb1.pixmap() and self.image_lb2.pixmap()):
            if not self.image_lb1.pixmap():
                QMessageBox.about(self, '提示', '请先加载功能区边界定位图')
            else:
                QMessageBox.about(self, '提示', '请先加载功能区属性定位图')
        else:
            print('执行合成函数，返回合成图片的路径')
            path = r'C:/Users/xuyongchuan/Desktop/脑皮质.jpg'
            composed_dialog = ComposedImage()
            composed_dialog.show_composed_image(path=path)
            composed_dialog.exec()

    # 静态方法测试例
    @staticmethod
    def get(parent=None):
        print('执行合成函数')
        a = 666
        return a


if __name__ == '__main__':
    function_app = QApplication(sys.argv)
    function_win = FunctionMapPart()
    function_win.show()
    sys.exit(function_app.exec_())




