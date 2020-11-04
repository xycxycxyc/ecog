#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 11:37
# @Author: xuyongchuan
# @File  : datapreprocessUI.py


import sys
import pandas as pd
import numpy as np
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMainWindow, QApplication, QWidget, QHBoxLayout, \
    QLabel, QListView, QListWidget, QGridLayout, QVBoxLayout, QPushButton, QFormLayout, QLineEdit, QComboBox, \
    QRadioButton, QCheckBox, QStackedWidget, QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtGui import QIntValidator
import pywt
import pymysql
from mne.io import read_raw_edf

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xyc19950910', db='brain', port=3306,
                       charset='utf8')


def show_status_decorator(func):
    # from functools import wraps
    #
    # @wraps(func)
    def decorated(self, *args, **kwargs):
        print(22222222222)
        self.status_signal.emit('testeststestestets')
        print(self.status_signal)
        print(3333333333333)
        func(self, *args, **kwargs)
        print(4444444444)
        self.status_signal.emit('hhhhhhhhh')

    return decorated


class DataPreprocessUI(QWidget):
    status_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        self.patient_id = ''
        self.pic_path = ''
        self.data_path = ''
        self.n_channels = 0
        self.raw_data = None
        self.static_signal = None
        self.feature_sample = []
        super(DataPreprocessUI, self).__init__(parent)
        self.patient_lb = QLabel('请选择病患:')
        self.patient_lb.setStyleSheet('QLabel{font-size:18px; font-family: \
        "Helvetica Neue", Helvetica, Arial, sans-serif;}')
        self.patient_cb = QComboBox()

        cur = conn.cursor()
        sql = ' select signal_id from ecog '
        cur.execute(sql)
        conn.commit()

        data = cur.fetchall()
        mylist = []
        for item in data:
            mylist.append(item[0])

        self.patient_cb.addItems([''] + mylist)
        self.patient_cb.setFixedSize(80, 30)
        self.patient_cb.setStyleSheet('QComboBox{font-size:18px; font-family: \
        "Helvetica Neue", Helvetica, Arial, sans-serif;}')

        self.patient_cb.currentIndexChanged.connect(self.select_patient)

        self.get_static_signal_bt = QPushButton('确定')
        self.get_static_signal_bt.setFixedSize(80, 30)
        self.get_static_signal_bt.setStyleSheet('QPushButton{color:rgb(0, 0, 0, 255);border:none;font-size:18px;font-family: \
                "Helvetica Neue", Helvetica, Arial, sans-serif;}\
                QPushButton:hover{border-left:4px solid red;font-weight:700;}')
        self.get_static_signal_bt.clicked.connect(self.get_static_signal)
        self.start_time_lb = QLabel('静息态数据开始时间（s）:')
        self.start_time_lb.setStyleSheet('QLabel{font-size:18px; font-family: \
        "Helvetica Neue", Helvetica, Arial, sans-serif;}')
        self.setObjectName('label')
        self.start_time = QLineEdit()
        # self.start_time.setPlaceholderText('请输入一个整数')
        self.start_time.setValidator(QIntValidator())
        self.start_time.setMaxLength(4)  # 设置整数的最大位数
        self.start_time.setFixedSize(50, 30)
        self.end_time_lb = QLabel('静息态数据结束时间（s）:')
        self.end_time_lb.setStyleSheet('QLabel{font-size:18px; font-family: \
        "Helvetica Neue", Helvetica, Arial, sans-serif;}')
        self.setObjectName('label')
        self.end_time = QLineEdit()
        # self.end_time.setPlaceholderText('请输入一个整数')
        self.end_time.setValidator(QIntValidator())
        self.end_time.setMaxLength(4)
        self.end_time.setFixedSize(50, 30)

        self.n_channels_lb = QLabel('导联数:')
        self.n_channels_lb.setStyleSheet('QLabel{font-size:18px; font-family: \
        "Helvetica Neue", Helvetica, Arial, sans-serif;}')
        self.n_channels_QL = QLineEdit()
        self.n_channels_QL.setReadOnly(True)
        self.n_channels_QL.setFixedSize(50, 30)

        # self.end_time.setInputMask('0000')

        self.show_loading_info_lb = QTextEdit()
        self.show_loading_info_lb.setReadOnly(True)
        self.show_loading_info_lb.setFixedSize(700, 500)
        self.show_loading_info_lb.setStyleSheet('''
        QTextEdit{   
                color:black;
                border:none;
                border-top:3px solid black;
                font-size:18px;
                font-weight:200;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setupUI()

    def setupUI(self):
        upper_layout = QHBoxLayout()
        upper_widget = QWidget()
        upper_layout.addWidget(self.start_time_lb)
        upper_layout.addWidget(self.start_time)
        upper_layout.addWidget(self.end_time_lb)
        upper_layout.addWidget(self.end_time)
        upper_layout.addWidget(self.n_channels_lb)
        upper_layout.addWidget(self.n_channels_QL)
        upper_widget.setLayout(upper_layout)

        lower_layout = QHBoxLayout()
        lower_widget = QWidget()
        lower_layout.addWidget(self.show_loading_info_lb, alignment=Qt.AlignLeft | Qt.AlignTop)
        lower_widget.setLayout(lower_layout)

        patient_lb_layout = QHBoxLayout()
        patient_lb_widget = QWidget()
        patient_lb_layout.addWidget(self.patient_lb, alignment=Qt.AlignRight)
        patient_lb_layout.addWidget(self.patient_cb, alignment=Qt.AlignLeft)
        patient_lb_widget.setLayout(patient_lb_layout)
        layout = QVBoxLayout()
        layout.addWidget(patient_lb_widget)
        layout.addWidget(upper_widget, stretch=1, alignment=Qt.AlignLeft)
        layout.addWidget(self.get_static_signal_bt, alignment=Qt.AlignRight)
        layout.addWidget(lower_widget, stretch=3, alignment=Qt.AlignLeft)
        layout.setSpacing(20)
        self.setLayout(layout)

    def show_data_path(self, path):
        if path:
            self.show_loading_info_lb.append('')
            self.show_loading_info_lb.append('加载数据:'+path)
        else:
            self.show_loading_info_lb.append('')
            self.show_loading_info_lb.append('数据未加载')

    # @show_status_decorator
    def select_patient(self):
        print(111111111111111)
        self.status_signal.emit('正在加载病人数据...')
        patient_id = self.patient_cb.currentText()
        self.patient_id = patient_id
        try:
            cur = conn.cursor()
            print(patient_id)
            print(type(patient_id))

            sql = 'select * from ecog where signal_id = "%s"' % patient_id
            # result = cur.execute("select password from user where nickname = '%s' " % (username))

            print(sql)
            cur.execute(sql)
            print('22222222')
            conn.commit()
            data = cur.fetchone()
            print('data:', data)
            patient_data_path = data[2]
            static_start = data[3]
            static_end = data[4]
            self.n_channels = data[5]
            self.pic_path = data[6]
            cur.close()
            conn.close()
        except Exception as e:
            print(e)
        print(11111111)

        self.data_path = patient_data_path
        if self.data_path:
            print(self.data_path)
            self.raw_data = read_raw_edf(self.data_path, preload=True, stim_channel=None)
            self.raw_data.filter(1, 249)
            self.raw_data.notch_filter((50, 100, 150, 200))
            print(type(self.raw_data))
        else:
            print('数据未加载')
        self.start_time.setText(str(static_start))
        self.end_time.setText(str(static_end))
        self.n_channels_QL.setText(str(self.n_channels))
        self.status_signal.emit('就绪！')

    # @show_status_decorator
    def get_static_signal(self):
        print(11111111)
        self.status_signal.emit('正在截取静息态数据...')
        self.show_data_path(self.data_path)
        if not self.raw_data:
            QMessageBox.information(self, '消息', '请先加载数据', QMessageBox.Ok)
            return
        start_time = self.start_time.text()  # 切记，这里的数据类型是str， 调用时要转为int类型
        print(type(start_time))
        end_time = self.end_time.text()
        if start_time and end_time:
            static_data = self.raw_data.to_data_frame()
            static_data = static_data.values
            static_data = static_data.T
            print(static_data.shape)
            static_data = static_data[1:, int(start_time)*500:int(end_time)*500]
            print(static_data.shape)
            self.show_loading_info_lb.append('')
            self.show_loading_info_lb.append('静息态数据截取: 起始时间:%ss,结束时间:%ss    完成！' %(start_time, end_time))
            self.static_signal = static_data
            print(static_data.shape)
            self.status_signal.emit('就绪！')
            return
        else:
            QMessageBox.information(self, '消息', '请输入正确的起始时间和结束时间', QMessageBox.Ok)
            self.status_signal.emit('static_time_error...')

    def feature_extract(self):
        # if not self.static_signal:  # 加上这三句代码会报错，不知道为啥。。。
        #     print('ssssssss')
        #     return
        self.status_signal.emit('正在进行特征提取...')
        self.show_loading_info_lb.append('')
        self.show_loading_info_lb.append('预处理:基线漂移矫正    完成！')
        self.show_loading_info_lb.append('')
        self.show_loading_info_lb.append('预处理:1Hz高通滤波--->49Hz-51Hz陷波滤波    完成！')
        #
        level = 6
        for i in range(len(self.static_signal)):
            test_data = self.static_signal[i:i + 1, :].flatten()
            test_data = test_data - test_data.mean()  # 减去信号的均值去除基线漂移，但是这个过程是不是把信号的幅值特征给掩盖了？
            coeffs = pywt.wavedec(test_data, 'db3', level=level)
            # print(len(coeffs))
            coeffs_zero0 = np.zeros(len(coeffs[0]))
            coeffs_zero1 = np.zeros(len(coeffs[1]))
            coeffs_zero2 = np.zeros(len(coeffs[2]))
            coeffs_zero3 = np.zeros(len(coeffs[3]))
            coeffs_zero4 = np.zeros(len(coeffs[4]))
            coeffs_zero5 = np.zeros(len(coeffs[5]))
            coeffs_zero6 = np.zeros(len(coeffs[6]))

            rec_signal1 = pywt.waverec(
                [coeffs[0], coeffs_zero1, coeffs_zero2, coeffs_zero3, coeffs_zero4, coeffs_zero5, coeffs_zero6],
                'db3')

            rec_signal2 = pywt.waverec(
                [coeffs_zero0, coeffs[1], coeffs_zero2, coeffs_zero3, coeffs_zero4, coeffs_zero5, coeffs_zero6],
                'db3')

            rec_signal3 = pywt.waverec(
                [coeffs_zero0, coeffs_zero1, coeffs[2], coeffs_zero3, coeffs_zero4, coeffs_zero5, coeffs_zero6],
                'db3')

            rec_signal4 = pywt.waverec(
                [coeffs_zero0, coeffs_zero1, coeffs_zero2, coeffs[3], coeffs_zero4, coeffs_zero5, coeffs_zero6],
                'db3')

            rec_signal5 = pywt.waverec(
                [coeffs_zero0, coeffs_zero1, coeffs_zero2, coeffs_zero3, coeffs[4], coeffs_zero5, coeffs_zero6],
                'db3')

            rec_signal6 = pywt.waverec(
                [coeffs_zero0, coeffs_zero1, coeffs_zero2, coeffs_zero3, coeffs_zero4, coeffs[5], coeffs_zero6],
                'db3')

            rec_signal7 = pywt.waverec(
                [coeffs_zero0, coeffs_zero1, coeffs_zero2, coeffs_zero3, coeffs_zero4, coeffs_zero5, coeffs[6]],
                'db3')

            rec_signal = []
            for signal in [rec_signal1, rec_signal2, rec_signal3, rec_signal4, rec_signal5, rec_signal6, rec_signal7]:
                rec_signal.append(signal)
            rec_signal.reverse()

            my_eng = []
            for signal in rec_signal:
                my_eng.append(sum(signal ** 2))
            my_eng = my_eng / sum(my_eng)
            self.feature_sample.append(my_eng)
        self.show_loading_info_lb.append('')
        self.status_signal.emit('就绪！')
        self.show_loading_info_lb.append('特征提取:使用db3小波，六层小波分解，提取七个子频带的能量占比作为特征    完成！')
        print(self.feature_sample)
        return self.feature_sample

    def trans_pic_path(self):
        return self.pic_path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = DataPreprocessUI()
    tree.show()
    # tree.show_data_path('sjggggggghhhjjgh')
    # tree.feature_extract()
    sys.exit(app.exec_())



