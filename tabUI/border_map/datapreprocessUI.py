#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 11:37
# @Author: xuyongchuan
# @File  : datapreprocessUI.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMainWindow, QApplication, QWidget, QHBoxLayout, \
    QLabel, QListView, QListWidget, QGridLayout, QVBoxLayout, QPushButton, QFormLayout, QLineEdit, \
    QRadioButton, QCheckBox, QStackedWidget, QFileDialog, QMessageBox, QTextEdit


class DataPreprocessUI(QWidget):
    def __init__(self, parent=None):
        super(DataPreprocessUI, self).__init__(parent)
        self.show_loading_info_lb = QTextEdit()
        self.show_loading_info_lb.setReadOnly(True)
        self.show_loading_info_lb.setFixedSize(700, 600)
        self.show_loading_info_lb.setStyleSheet('''
        QTextEdit{   
                color:black;
                border:none;
                font-size:18px;
                font-weight:200;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.show_loading_info_lb, alignment=Qt.AlignLeft | Qt.AlignTop)

        self.setLayout(layout)

    def show_data_path(self, path):
        if path:
            self.show_loading_info_lb.append('')
            self.show_loading_info_lb.append('加载数据:'+path)
        else:
            self.show_loading_info_lb.append('')
            self.show_loading_info_lb.append('数据未加载')

    def show_preprocess(self):
        self.show_loading_info_lb.append('')
        self.show_loading_info_lb.append('预处理:1Hz高通滤波--->49Hz-51Hz陷波滤波    完成！')
        self.show_loading_info_lb.append('')
        self.show_loading_info_lb.append('特征提取:使用db3小波，六层小波分解，提取七个子频带的能量占比作为特征    完成！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = DataPreprocessUI()
    tree.show()
    tree.show_data_path('sjggggggghhhjjgh')
    tree.show_preprocess()
    sys.exit(app.exec_())

