#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 16:23
# @Author: xuyongchuan
# @File  : clusterUI.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout


class ClusterUI(QWidget):
    def __init__(self, parent=None):
        super(ClusterUI, self).__init__(parent)
        self.cluster_label = QLabel()
        self.cluster_1 = QCheckBox()
        self.cluster_2 = QCheckBox()
        self.para_label = QLabel()
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        self.cluster_label.setText('选择要使用的聚类方法')
        self.cluster_1.setText('K-means聚类')
        self.cluster_1.setChecked(False)
        self.cluster_2.setText('层次聚类')
        self.cluster_2.setChecked(False)
        self.para_label.setText('选择合适的参数')
        layout.addWidget(self.cluster_label)
        layout.addWidget(self.cluster_1)
        layout.addWidget(self.cluster_2)
        layout.addWidget(self.para_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ClusterUI()
    win.show()
    sys.exit(app.exec_())