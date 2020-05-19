#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 11:37
# @Author: xuyongchuan
# @File  : datapreprocessUI.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMainWindow, QApplication, QWidget, QHBoxLayout, \
    QLabel, QListView, QListWidget, QGridLayout, QVBoxLayout, QPushButton, QFormLayout, QLineEdit, \
    QRadioButton, QCheckBox, QStackedWidget, QFileDialog, QMessageBox


class DataPreprocessUI(QWidget):
    def __init__(self, parent=None):
        super(DataPreprocessUI, self).__init__(parent)
        self.show_data_path_lb = QLabel()
        self.show_preprocess_lb = QLabel()
        self.show_feature_lb = QLabel()
        self.show_pic_path_lb = QLabel()
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.show_data_path_lb, alignment=Qt.AlignLeft | Qt.AlignTop, stretch=1)
        layout.addWidget(self.show_preprocess_lb, alignment=Qt.AlignLeft | Qt.AlignTop, stretch=1)
        layout.addWidget(self.show_feature_lb, alignment=Qt.AlignLeft | Qt.AlignTop, stretch=1)
        layout.addStretch(10)

        self.setLayout(layout)

    def show_data_path(self, path):
        self.show_data_path_lb.setText('加载数据:'+path)

    def show_preprocess(self):
        self.show_preprocess_lb.setText('预处理:1Hz高通滤波--->49Hz-51Hz陷波滤波    完成！')
        self.show_feature_lb.setText('特征提取:使用db3小波，六层小波分解，提取七个子频带的能量占比作为特征    完成！')

    def test(self):  # 测试伸缩量的函数
        self.show_data_path_lb.setText('hhhhhhhhh')
        self.show_preprocess_lb.setText('hhhhhh')
        self.show_feature_lb.setText('hhhhhhhhh')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = DataPreprocessUI()
    tree.show()
    tree.test()
    sys.exit(app.exec_())

