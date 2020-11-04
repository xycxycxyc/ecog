#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 20:46
# @Author: xuyongchuan
# @File  : generete_border_map.py


import sys
import os
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import cv2
import numpy as np
import json


class GenerateBorderMap(QWidget):
    status_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(GenerateBorderMap, self).__init__(parent)
        self.show_border_map_bt = QPushButton()
        self.border_map_label = QLabel()
        self.setupUI()
        self.pic = None
        self.pic_path = ''
        self.result_list = []
        self.border_map_path = ''

    def setupUI(self):
        layout = QVBoxLayout()
        self.show_border_map_bt.setText('生成边界定位图')
        self.show_border_map_bt.setFixedSize(150, 50)

        self.show_border_map_bt.setObjectName('show_border_map_bt')
        self.show_border_map_bt.clicked.connect(self.show_border_map)

        layout.addWidget(self.show_border_map_bt, alignment=Qt.AlignLeft)
        layout.addWidget(self.border_map_label, alignment=Qt.AlignCenter)
        self.setStyleSheet('''
        QPushButton#show_border_map_bt{   
                color:black;
                border:none;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        QPushButton#show_border_map_bt:hover{border-right:4px solid red;font-weight:700;}
        ''')

        self.setLayout(layout)

    def show_border_map(self):
        self.plot_border_map()
        os.getcwd()
        file_list = os.listdir(os.getcwd())
        print(file_list)
        if 'border_map.jpg' in file_list:
            print('sssss')
            border_map_path = os.getcwd() + '\\border_map.jpg'
            self.border_map_path = border_map_path

            self.border_map_label.setPixmap(QPixmap(self.border_map_path))
            self.border_map_label.setScaledContents(True)  # 让图片自适应label的大小
        else:
            QMessageBox.warning(self, '警告', '请先生成边界定位图', QMessageBox.Ok)

    def get_pic_path(self, pic_path):
        self.pic_path = pic_path
        print(self.pic_path)

    def get_result_list(self, result_list):
        self.result_list = result_list
        print(self.result_list)

    def plot_border_map(self):
        self.status_signal.emit('正在绘制边界图...')
        if len(self.result_list) == 0:
            QMessageBox.warning(self, '警告', '请先生成聚类结果', QMessageBox.Ok)
            return False
        if self.pic_path == '':
            QMessageBox.warning(self, '警告', '请先加载电极图片', QMessageBox.Ok)
            return False
        print(self.pic_path)
        img = cv2.imread(self.pic_path)
        print(img)
        # img = cv2.imread(r'C:\Users\xuyongchuan\Desktop\brain.jpg')
        f = open('coords.json', encoding="utf-8")  # 如何访问上一级目录中的json文件呢？
        user_dic = json.load(f)
        print(user_dic['area_coords'])
        area_index = user_dic['area_coords']
        electrode_coords = user_dic['ele_coords'][::-1]
        f.close()
        x, y = [], []

        for i, j in area_index:
            x.append(i)
            y.append(j)
        k1 = (y[1] - y[0]) / (x[1] - x[0])
        b1 = y[1] - k1 * x[1]

        k2 = (y[1] - y[3]) / (x[1] - x[3])
        b2 = y[1] - k2 * x[1]

        k3 = (y[2] - y[3]) / (x[2] - x[3])
        b3 = y[2] - k3 * x[2]

        k4 = (y[0] - y[2]) / (x[0] - x[2])
        b4 = y[0] - k4 * x[0]

        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)

        def left_border(x):
            return k4 * x + b4

        def right_border(x):
            return k2 * x + b2

        def bottom_border(x):
            return k1 * x + b1

        def top_border(x):
            return k3 * x + b3

        for i in range(x_min, x_max):

            for j in range(y_min, y_max):

                right = right_border(i)
                left = left_border(i)
                bottom = bottom_border(i)
                top = top_border(i)

                if int(left) in [j - 1, j, j + 1] or int(right) in [j - 1, j, j + 1] or int(bottom) in [j - 1, j,
                                                                                                        j + 1] or int(
                        top) in [j - 1, j, j + 1]:
                    #         if left < j < right and top < j < bottom:

                    img[j, i] = (255, 255, 255)
        # cv2.imshow('image', img)

        result_list = [0, 0, 2, 1, 1, 1, 3, 0]
        electrode_list1 = []
        electrode_list2 = []
        electrode_list3 = []
        electrode_list4 = []

        for i in range(len(result_list)):
            if result_list[i] == 0:
                electrode_list1.append(electrode_coords[i])
            if result_list[i] == 1:
                electrode_list2.append(electrode_coords[i])
            if result_list[i] == 2:
                electrode_list3.append(electrode_coords[i])
            if result_list[i] == 3:
                electrode_list4.append(electrode_coords[i])

        print(electrode_list1)

        # 定义插值函数
        # 插值公式  numerator： 分子  denominator：分母
        def my_interpolation(i, j, color, electrode_list):
            numerator = 0
            denominator = 0
            for x, y in electrode_list:
                numerator += (1 / (np.sqrt((x - i) ** 2 + (y - j) ** 2)))
            for x, y in electrode_coords:
                denominator += (1 / (np.sqrt((x - i) ** 2 + (y - j) ** 2)))

            tmp = numerator / denominator
            #     if tmp >= 0.5:
            if len(electrode_list) == 1:
                if 0.3 < tmp < 0.315:
                    return color
            else:
                if 0.5 < tmp < 0.515:
                    return color
            return img[j, i]

        for i in range(x_min, x_max):
            for j in range(y_min, y_max):
                #         print((i, j))
                right = right_border(i)
                left = left_border(i)
                bottom = bottom_border(i)
                top = top_border(i)
                if int(left) in [j - 1, j, j + 1] or int(right) in [j - 1, j, j + 1] or int(bottom) in [j - 1, j,
                                                                                                        j + 1] or int(
                        top) in [j - 1, j, j + 1]:
                    #         if left < j < right and top < j < bottom:

                    img[j, i] = (255, 255, 255)
        # cv2.imshow('image', img)
        color_map = [(255, 0, 0), (0, 255, 255), (0, 255, 0), (34, 139, 34)]

        ele_list = [electrode_list1, electrode_list2, electrode_list3, electrode_list4]
        for index, electrode_list in enumerate(ele_list):
            for i in range(x_min, x_max):
                for j in range(y_min, y_max):
                    right = right_border(i)
                    left = left_border(i)
                    bottom = bottom_border(i)
                    top = top_border(i)
                    #         if left < j < right and bottom < j < top:
                    #         if right < j < left and bottom < j < top:
                    if left < j < right and top < j < bottom:
                        #         if right < j < left and top < j < bottom:

                        if [i, j] in electrode_coords:
                            if [i, j] in electrode_list:
                                img[j, i] = color_map[index]
                        else:
                            img[j, i] = my_interpolation(i, j, color_map[index], electrode_list)

        cv2.imwrite("border_map.jpg", img)
        self.status_signal.emit('就绪！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GenerateBorderMap()
    # win.plot_border_map()
    win.show()
    sys.exit(app.exec_())