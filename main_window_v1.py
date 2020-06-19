#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/6 16:32
# @Author: xuyongchuan
# @File  : main_window_v1.py

from mne.io import read_raw_edf

# data_path = r'C:\Users\xuyongchuan\Desktop\陆总数据EEG\1_reduced.edf'
# raw_data = read_raw_edf(data_path)
# plot_raw(raw_data)


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, \
    QGridLayout, QVBoxLayout, QPushButton, QStackedWidget, QFileDialog, QMessageBox
import pymysql
import qtawesome

from tabUI.system_intro import SystemIntro
from tabUI.border_map.border_map_intro import BorderMapIntro
from tabUI.border_map.datapreprocessUI import DataPreprocessUI
from tabUI.border_map.clusterUI import ClusterUI
from tabUI.border_map.load_electrode_pic import LoadElectrodePic
from tabUI.border_map.generete_border_map import GenerateBorderMap
from tabUI.property_map.property_map_intro import PropertyMapIntro
from tabUI.property_map.load_cortex_pic import LoadCortexPic
from tabUI.property_map.generate_property_map import GeneratePropertyMap
from tabUI.function_map.function_map_intro import FunctionMapIntro
from tabUI.function_map.generate_function_map import GenerateFunctionMap


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.patient_id = ''
        self.result_list = []
        self.title_lb = QPushButton()
        self.exit_bt = QPushButton()
        self.logo_bt = QPushButton()
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.left_widget = QWidget()
        self.left_layout = QGridLayout()
        self.right_widget = QStackedWidget()
        self.mid_widget = QWidget()
        self.mid_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.bottom_widget = QWidget()
        self.status_bar = QPushButton()
        # self.stack1 = QWidget()

        self.stack_system_intro = SystemIntro()
        self.stack_border_map_intro = BorderMapIntro()
        self.stack_datapreprocessUI = DataPreprocessUI()
        self.stack_clusterUI = ClusterUI()
        self.stack_load_electrode_picUI = LoadElectrodePic()
        self.stack_generate_border_mapUI = GenerateBorderMap()
        self.stack_property_map_intro = PropertyMapIntro()
        self.stack_load_cortex_pic = LoadCortexPic()
        self.stack_generate_property_map = GeneratePropertyMap()
        self.stack_function_map_intro = FunctionMapIntro()
        self.stack_generate_function_map = GenerateFunctionMap()

        self.left_close = QPushButton("")  # 关闭按钮
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_mini = QPushButton("")  # 最小化按钮
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_label_1 = QPushButton("功能区边界定位图")
        self.left_label_1.clicked.connect(self.on_border_map_bt_clicked)
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QPushButton("功能区属性定位图")
        self.left_label_2.clicked.connect(self.on_property_map_bt_clicked)
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QPushButton("功能区地形图")
        self.left_label_3.clicked.connect(self.on_function_map_bt_clicked)
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QPushButton(qtawesome.icon('fa.music', color='white'), "导入数据")
        self.left_button_1.clicked.connect(self.on_load_data_bt_clicked)
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "预处理及特征提取")
        self.left_button_2.clicked.connect(self.on_preprocessing_bt_clicked)
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QPushButton(qtawesome.icon('fa.film', color='white'), "模型加载与识别")
        self.left_button_3.clicked.connect(self.on_load_model_bt_clicked)
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QPushButton(qtawesome.icon('fa.home', color='white '), "导入电极分布图")
        self.left_button_4.clicked.connect(self.on_load_pic_bt_clicked)
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QPushButton(qtawesome.icon('fa.download', color='white'), "边界定位图")
        self.left_button_5.clicked.connect(self.on_generate_border_map_bt_clicked)
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QPushButton(qtawesome.icon('fa.heart', color='white'), "加载皮质图片")
        self.left_button_6.clicked.connect(self.on_load_cortex_bt_clicked)
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QPushButton(qtawesome.icon('fa.comment', color='white'), "属性定位图")
        self.left_button_7.clicked.connect(self.on_generate_property_map_bt_clicked)
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QPushButton(qtawesome.icon('fa.star', color='white'), "功能区地形图")
        self.left_button_8.clicked.connect(self.on_generate_function_map_bt_clicked)
        self.left_button_8.setObjectName('left_button')

        self.setupUI()
        self.raw_data = 0
        self.data_path = ''
        self.pic_path = ''
        self.border_pic_path = None
        self.feature_sample = None

    def setupUI(self):
        self.resize(1000, 800)
        self.setWindowTitle('ECoG+AL术中脑功能定位系统')
        self.title_lb.setText('ECoG+AL术中脑功能定位系统')
        self.title_lb.clicked.connect(self.on_title_bt_clicked)
        self.title_lb.setFixedSize(500, 70)
        self.title_lb.setStyleSheet('QPushButton{color:rgb(0, 0, 0, 255);border:none;font-size:30px;font-family: \
                "Helvetica Neue", Helvetica, Arial, sans-serif;}\
                QPushButton:hover{border-left:4px solid red;font-weight:700;}')
        self.exit_bt.setText('退出')
        self.exit_bt.setFixedSize(100, 50)
        self.exit_bt.setStyleSheet('QPushButton{color:rgb(0, 0, 0, 255);border:none;font-size:25px;font-family: \
        "Helvetica Neue", Helvetica, Arial, sans-serif;}\
        QPushButton:hover{border-left:4px solid red;font-weight:700;}')
        self.exit_bt.clicked.connect(self.exit_bt_clicked)
        self.logo_bt.setText('copyright@SCUT-BME-504')
        self.logo_bt.setFixedSize(300, 30)
        self.logo_bt.setStyleSheet('QPushButton{color:rgb(0, 0, 0, 255);border:none;font-size:15px;font-family: \
        "Helvetica Neue", Helvetica, Arial, sans-serif;}\
        QPushButton:hover{border-left:4px solid red;font-weight:700;}')

        self.bottom_layout.addWidget(self.status_bar, alignment=Qt.AlignLeft)
        self.bottom_layout.addWidget(self.logo_bt, alignment=Qt.AlignCenter)
        self.bottom_layout.addWidget(self.exit_bt, alignment=Qt.AlignRight)

        self.bottom_widget.setLayout(self.bottom_layout)

        self.stack_datapreprocessUI.setStyleSheet('QLabel{color:black;font-size:20px;font-family:Arial; \
         header:None}')

        self.main_widget.setLayout(self.main_layout)

        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)
        self.right_widget.setObjectName('right_widget')

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)

        # self.left_layout.setSpacing(0)
        # self.stack = QStackedWidget()
        self.right_widget.addWidget(self.stack_system_intro)
        self.right_widget.addWidget(self.stack_border_map_intro)
        self.right_widget.addWidget(self.stack_datapreprocessUI)
        self.right_widget.addWidget(self.stack_clusterUI)
        self.right_widget.addWidget(self.stack_load_electrode_picUI)
        self.right_widget.addWidget(self.stack_generate_border_mapUI)
        self.right_widget.addWidget(self.stack_property_map_intro)
        self.right_widget.addWidget(self.stack_load_cortex_pic)
        self.right_widget.addWidget(self.stack_generate_property_map)
        self.right_widget.addWidget(self.stack_function_map_intro)
        self.right_widget.addWidget(self.stack_generate_function_map)

        self.mid_layout.addWidget(self.left_widget, stretch=1)
        self.mid_layout.addWidget(self.right_widget, stretch=3)
        self.mid_widget.setFixedSize(1000, 650)
        self.mid_layout.setSpacing(0)
        self.mid_widget.setLayout(self.mid_layout)

        self.main_widget.setObjectName('main_widget')
        self.main_layout.addWidget(self.title_lb, alignment=Qt.AlignCenter, stretch=1)  # 前两个参数是所在的行列，后两个参数是占用几行几列
        self.main_layout.addWidget(self.mid_widget, stretch=7)
        self.main_layout.addWidget(self.bottom_widget, stretch=1)
        self.main_layout.setSpacing(0)
        # 设置窗口的样式
        main_widget_stylesheet = '''
            QWidget#main_widget{
                background:gray;
            }
            QPushButton#left_button{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QWidget#left_widget{
                background:grey;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QPushButton#left_label:hover{border-left:4px solid red;font-weight:700;}
        '''
        self.main_widget.setStyleSheet(main_widget_stylesheet)
        self.setCentralWidget(self.main_widget)  # 一定要有要句代码，要不然主窗口不显示
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.right_widget.setCurrentWidget(self.stack_system_intro)
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框

    def on_title_bt_clicked(self):
        self.right_widget.setCurrentWidget(self.stack_system_intro)

    def on_border_map_bt_clicked(self):
        self.right_widget.setCurrentWidget(self.stack_border_map_intro)

    def on_load_data_bt_clicked(self):

        self.right_widget.setCurrentWidget(self.stack_datapreprocessUI)

    def on_preprocessing_bt_clicked(self):
        self.feature_sample = self.stack_datapreprocessUI.feature_extract()
        if self.feature_sample:
            self.right_widget.setCurrentWidget(self.stack_datapreprocessUI)
        else:
            if not self.raw_data:
                QMessageBox.information(self, '消息', '请先加载数据', QMessageBox.Ok)
            else:
                self.feature_sample = self.stack_datapreprocessUI.feature_extract()

    def on_load_model_bt_clicked(self):
        self.stack_clusterUI.get_feature_sample(self.feature_sample)
        self.right_widget.setCurrentWidget(self.stack_clusterUI)

    def on_load_pic_bt_clicked(self):
        self.pic_path = self.stack_datapreprocessUI.trans_pic_path()
        self.stack_load_electrode_picUI.get_pic_path(self.pic_path)
        self.right_widget.setCurrentWidget(self.stack_load_electrode_picUI)

    def on_generate_border_map_bt_clicked(self):
        self.stack_generate_border_mapUI.get_pic_path(self.pic_path)
        self.result_list = self.stack_clusterUI.trans_result_list()

        self.stack_generate_border_mapUI.get_result_list(self.result_list)
        self.right_widget.setCurrentWidget(self.stack_generate_border_mapUI)

    def on_property_map_bt_clicked(self):
        self.right_widget.setCurrentWidget(self.stack_property_map_intro)

    def on_load_cortex_bt_clicked(self):
        self.right_widget.setCurrentWidget(self.stack_load_cortex_pic)

    def on_generate_property_map_bt_clicked(self):
        self.right_widget.setCurrentWidget(self.stack_generate_property_map)

    def on_function_map_bt_clicked(self):
        self.right_widget.setCurrentWidget(self.stack_function_map_intro)

    def on_generate_function_map_bt_clicked(self):
        self.right_widget.setCurrentWidget(self.stack_generate_function_map)

    def exit_bt_clicked(self):
        # sender是发送信号的对象，这里获得的是按钮的名称
        sender = self.sender()
        # 以文本的形式输出按钮的名称
        print(sender.text() + ' 被按下了')
        # 获取QApplication类的对象
        q_app = QApplication.instance()
        # 退出
        q_app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = MainWindow()
    tree.show()
    sys.exit(app.exec_())
