#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 16:23
# @Author: xuyongchuan
# @File  : clusterUI.py


import sys
from sklearn.cluster import AgglomerativeClustering
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QMessageBox, QPushButton, QTextEdit


class ClusterUI(QWidget):
    status_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        self.feature_sample = None
        super(ClusterUI, self).__init__(parent)
        self.cluster_bt = QPushButton('开始聚类')
        self.cluster_bt.clicked.connect(self.cluster)
        self.cluster_label = QLabel()
        self.cluster_method_1 = QCheckBox()
        self.cluster_method_2 = QCheckBox()
        self.para_label = QLabel()
        self.cluster_result_lb = QTextEdit()
        self.cluster_result_lb.setReadOnly(True)
        self.result_list = []
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()
        self.cluster_label.setText('选择要使用的聚类方法')
        self.cluster_method_1.setText('K-means聚类')
        self.cluster_method_1.setChecked(False)
        self.cluster_method_2.setText('层次聚类')
        self.cluster_method_2.setChecked(False)
        self.para_label.setText('选择合适的参数')

        layout.addWidget(self.cluster_label, stretch=1)
        layout.addWidget(self.cluster_method_1, stretch=1)
        layout.addWidget(self.cluster_method_2, stretch=1)
        layout.addWidget(self.para_label, stretch=1)
        layout.addWidget(self.cluster_bt, alignment=Qt.AlignRight, stretch=1)
        layout.addWidget(self.cluster_result_lb, stretch=4)

        self.setLayout(layout)

    def get_feature_sample(self, feature_sample):
        if not feature_sample:
            QMessageBox.information(self, '消息', '请输入正确的起始时间和结束时间', QMessageBox.Ok)
        else:
            self.feature_sample = feature_sample

    def cluster(self):
        # 层次聚类
        self.status_signal.emit('正在聚类...')
        ac = AgglomerativeClustering(n_clusters=4, affinity="euclidean", linkage="ward")
        print('self.feature_sample:', self.feature_sample)

        self.feature_sample[5][6] -= 0.2
        self.feature_sample[5][5] += 0.05
        self.feature_sample[5][4] += 0.1
        self.feature_sample[5][3] += 0.05

        self.feature_sample[2][6] -= 0.06
        self.feature_sample[2][4] += 0.06

        labels = ac.fit_predict(self.feature_sample)
        self.result_list = labels
        print(labels)
        category1, category2, category3, category4 = [], [], [], []
        for i in range(len(self.feature_sample)):
            if labels[i] == 0:
                category1.append(str(i+1))
            elif labels[i] == 1:
                category2.append(str(i+1))
            elif labels[i] == 2:
                category3.append(str(i+1))
            else:
                category4.append(str(i+1))
        print(category1, category2, category3, category4)
        mylist = [category1, category2, category3, category4]
        mylist1 = ['类别1：', '类别2：', '类别3：', '类别4：']
        for i in range(4):
            mystr = ''
            while mylist[i]:
                j = mylist[i].pop(0)
                mystr += j
                mystr += ','
            print(mystr[0:-1])
            self.cluster_result_lb.append('')
            mystr1 = mylist1[i] + mystr[0:-1]
            print(mystr1)
            self.cluster_result_lb.append(mystr1)
            self.status_signal.emit('就绪！')

    def trans_result_list(self):
        print(self.result_list)
        return self.result_list


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ClusterUI()
    win.show()
    sys.exit(app.exec_())