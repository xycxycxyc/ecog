#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/6 16:32
# @Author: xuyongchuan
# @File  : main_window_v1.py

from mne.io import read_raw_edf
from mne.viz import plot_raw
#
# data_path = r'C:\Users\xuyongchuan\Desktop\陆总数据EEG\1_reduced.edf'
# raw_data = read_raw_edf(data_path)
# plot_raw(raw_data)


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMainWindow, QApplication, QWidget, QHBoxLayout, \
    QLabel, QListView, QListWidget, QGridLayout, QVBoxLayout, QPushButton, QFormLayout, QLineEdit, \
    QRadioButton, QCheckBox, QStackedWidget, QFileDialog, QMessageBox
from tabUI.workspaceUI import WorkSpaceUI_Info


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title_lb = QLabel()
        self.exit_bt = QPushButton()
        self.tree = QTreeWidget()
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.right_widget = QStackedWidget()
        self.mid_widget = QWidget()
        self.mid_layout = QHBoxLayout()
        # self.stack1 = QWidget()
        self.stack1 = WorkSpaceUI_Info()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        # self.tab2UI()
        # self.tab3UI()
        self.setupUI()
        self.raw_data = 0
        self.data_path = ''
        self.pic_path = ''

    def setupUI(self):
        self.resize(1000, 800)
        self.setWindowTitle('ECoG+AL术中脑功能定位系统')
        self.title_lb.setText('ECoG+AL术中脑功能定位系统')
        self.title_lb.setStyleSheet('QLabel{color:rgb(0, 0, 0, 255);font-size:30px;font-weight:bold;font-family:Arial;}')
        self.exit_bt.setText('退出')
        self.exit_bt.setFixedSize(100, 50)
        self.exit_bt.setStyleSheet('QPushButton{color:rgb(0, 0, 0, 255);font-size:20px;font-family:Arial;}')
        self.exit_bt.clicked.connect(self.exit_bt_clicked)
        self.stack1.setStyleSheet('QLabel{color:black;font-size:20px;font-family:Arial; \
         header:None}')

        self.main_widget.setLayout(self.main_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.title_lb, alignment=Qt.AlignCenter)  # 前两个参数是所在的行列，后两个参数是占用几行几列
        # self.left_widget.resize(300, 600)
        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)

        self.right_widget.setObjectName('right_widget')
        # self.right_widget.resize(700, 500)

        self.tree.setColumnCount(1)
        self.tree.setFixedSize(280, 500)
        self.tree.setHeaderLabels([''])
        root_bd = QTreeWidgetItem(self.tree)
        root_bd.setText(0, '功能区边界定位图')
        bd_child1 = QTreeWidgetItem(root_bd).setText(0, '导入数据')
        bd_child2 = QTreeWidgetItem(root_bd).setText(0, '数据预处理及特征提取')
        bd_child3 = QTreeWidgetItem(root_bd).setText(0, '模型加载与识别')
        bd_child4 = QTreeWidgetItem(root_bd).setText(0, '导入电极分布图片')
        bd_child5 = QTreeWidgetItem(root_bd).setText(0, '边界定位图')

        root_pp = QTreeWidgetItem(self.tree)
        root_pp.setText(0, '功能区属性定位图')
        pp_child1 = QTreeWidgetItem(root_pp).setText(0, '加载皮质图片')
        pp_child2 = QTreeWidgetItem(root_pp).setText(0, '属性定位图')

        root_func = QTreeWidgetItem(self.tree)
        root_func.setText(0, '功能区地形图')
        func_child1 = QTreeWidgetItem(root_func).setText(0, '合成功能区地形图')

        # self.stack = QStackedWidget()
        self.right_widget.addWidget(self.stack1)
        self.right_widget.addWidget(self.stack2)
        self.right_widget.addWidget(self.stack3)

        self.left_layout.addWidget(self.tree)

        self.mid_layout.addWidget(self.left_widget, stretch=1)
        self.mid_layout.addWidget(self.right_widget, stretch=2)
        self.mid_layout.setSpacing(0)
        self.mid_widget.setLayout(self.mid_layout)

        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.mid_widget)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.exit_bt, alignment=Qt.AlignRight)
        self.main_layout.addStretch(1)

        self.tree.setStyleSheet('QTreeWidget{color:black;font-size:22px;font-family:Arial; \
         header:None}')
        # self.left_widget.setStyleSheet('''
        # QTreeWidget{border:none;font-size:20px;background:red}
        # ''')

        self.tree.clicked.connect(self.onTreeClicked)

        # self.right_widget.setHidden(True)
        self.setCentralWidget(self.main_widget)  # 一定要有要句代码，要不然主窗口不显示

        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print(item.text(0))
        if item.text(0) == '导入数据':
            path = self.load_data()
            print(path)
            if not path:
                QMessageBox.information(self, '消息', '数据加载失败', QMessageBox.Ok)
            self.stack1.show_data_path(path)
        print('key=%s' % (item.text(0)))

        # self.right_widget.setCurrentIndex(index.row())
        self.right_widget.setCurrentWidget(self.stack1)

        if item.text(0) == '数据预处理及特征提取':
            if not self.raw_data:
                QMessageBox.information(self, '消息', '请先加载数据', QMessageBox.Ok)
            else:
                self.stack1.show_preprocess()


    def load_data(self):
        self.data_path, _ = QFileDialog.getOpenFileName(self, '加载脑电数据', '.', '脑电文件(*.edf)')
        if self.data_path:
            print(self.data_path)
            print(_)
            self.raw_data = read_raw_edf(self.data_path)
            print(self.raw_data)
            QMessageBox.information(self, '消息', '数据加载完成', QMessageBox.Ok)
            return self.data_path
        else:
            print('数据未加载')
            return


    def exit_bt_clicked(self):
        # sender是发送信号的对象，这里获得的是按钮的名称
        sender = self.sender()
        # 以文本的形式输出按钮的名称
        print(sender.text() + ' 被按下了')
        # 获取QApplication类的对象
        q_app = QApplication.instance()
        # 退出
        q_app.quit()

    def tab1UI(self, path):
        print('调用一次')
        print(path)
        layout = QFormLayout()
        data_label = QLabel('数据路径:')
        pic_label = QLabel('电极分布图路径:')
        show_data_path_lb = QLabel()
        show_data_path_lb.setText(path)
        layout.addRow(data_label, show_data_path_lb)
        # layout.addWidget(data_label, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.stack1.setLayout(layout)
        self.stack1.setStyleSheet('QLabel{color:black;font-size:20px;font-family:Arial; \
         header:None}')


    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日',QLineEdit())

        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'), alignment=Qt.AlignLeft)
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = MainWindow()
    tree.show()
    sys.exit(app.exec_())
