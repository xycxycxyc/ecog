#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/22 18:45
# @Author: xuyongchuan
# @File  : border_map.py

from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QApplication, QHBoxLayout, \
    QPushButton, QWidget, QLabel, QVBoxLayout, QFileDialog
import sys
from PyQt5.QtCore import Qt
from mne.io import read_raw_edf
from mne.viz import plot_raw
import numpy as np


class BorderMapPart(QDialog):
    def __init__(self, parent=None):
        super(BorderMapPart, self).__init__(parent)
        self.border_title_lb = QLabel()
        self.border_ld_bt = QPushButton()
        self.border_pp_bt = QPushButton()
        self.border_lmr_bt = QPushButton()
        self.border_pm_bt = QPushButton()
        self.setupUI()
        self.data_path = ''
        self.pic_path = ''
        self.raw_data = 0

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

        self.border_ld_bt.clicked.connect(self.load_data)
        self.border_pp_bt.clicked.connect(self.preprocess)
        self.border_lmr_bt.clicked.connect(self.recognize)
        self.border_pm_bt.clicked.connect(self.paint_bd_map)

    def load_data(self):
        QMessageBox.information(self, '提示', '请先加载脑电数据', QMessageBox.Yes)
        self.data_path, _ = QFileDialog.getOpenFileName(self, '加载脑电数据', '.', '脑电文件(*.edf)')

        QMessageBox.information(self, '提示', '请加载皮质图片', QMessageBox.Yes)
        self.pic_path, _ = QFileDialog.getOpenFileName(self, '加载皮质图片', '.', '图像文件(*.png, *.jpg)')

        if self.data_path and self.pic_path:
            print(self.data_path)
            print(_)
            self.raw_data = read_raw_edf(self.data_path)
            print(self.raw_data)
            QMessageBox.information(self, '消息', '数据加载完成', QMessageBox.Ok)
        else:
            if (not self.data_path) and (not self.pic_path):
                print('数据未加载')
            else:
                if self.data_path:
                    print('皮质图片未加载')
                else:
                    print('脑电数据未加载')

    def preprocess(self):  # 预处理步骤：静息态数据截取->49-51Hz陷波滤波->ICA滤波
        plot_raw(self.raw_data)
        QMessageBox.information(self, '消息', '数据预处理完成', QMessageBox.Ok)

    def recognize(self):
        QMessageBox.information(self, '消息', '功能区识别完成', QMessageBox.Ok)

    def paint_bd_map(self):
        QMessageBox.information(self, '消息', '绘制功能区边界图完成', QMessageBox.Ok)


if __name__ == '__main__':
    border_app = QApplication(sys.argv)
    border_win = BorderMapPart()
    border_win.show()
    sys.exit(border_app.exec_())


