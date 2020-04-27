#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/22 18:45
# @Author: xuyongchuan
# @File  : border_map.py

from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QHBoxLayout, QPushButton, QWidget, QLabel, QVBoxLayout
import sys
from PyQt5.QtCore import Qt


class BorderMapPart(QDialog):
    def __init__(self, parent=None):
        super(BorderMapPart, self).__init__(parent)
        self.border_title_lb = QLabel()
        self.border_ld_bt = QPushButton()
        self.border_pp_bt = QPushButton()
        self.border_lmr_bt = QPushButton()
        self.border_pm_bt = QPushButton()
        self.setupUI()

    def setupUI(self):
        self.resize(800, 600)
        self.setWindowTitle('边界定位图部分')
        border_label_style = 'QLabel{color:rgb(0, 0, 0, 255);font-size:30px;font-weight:bold;font-family:Arial;}'
        border_button_style = 'QPushButton{color:rgb(0, 0, 0, 255);font-size:20px;font-weight:bold;font-family:Arial;}'

        self.border_title_lb.setText('边界定位图部分')
        self.border_title_lb.setStyleSheet(border_label_style)

        border_vlayout = QVBoxLayout()
        border_vlayout.addStretch(1)
        border_vlayout.addWidget(self.border_title_lb, alignment=Qt.AlignCenter)

        border_button_text_list = ['导入数据及电极分布图片', '数据预处理及特征提取', '模型加载与识别', '画出边界定位图并保存']
        border_button_list = [self.border_ld_bt, self.border_pp_bt, self.border_lmr_bt, self.border_pm_bt]

        for i in range(4):
            border_button_list[i].setText(border_button_text_list[i])
            border_button_list[i].setStyleSheet(border_button_style)
            border_button_list[i].setFixedSize(250, 50)
            border_vlayout.addStretch(1)
            border_vlayout.addWidget(border_button_list[i], alignment=Qt.AlignLeft)
        border_vlayout.addStretch(1)
        self.setLayout(border_vlayout)

    def load_data(self):
        pass


if __name__ == '__main__':
    border_app = QApplication(sys.argv)
    border_win = BorderMapPart()
    border_win.show()
    sys.exit(border_app.exec_())


