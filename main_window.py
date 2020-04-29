#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/21 11:30
# @Author: xuyongchuan
# @File  : main_window.py


from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QPushButton, QWidget, QLabel, QVBoxLayout
import sys
from PyQt5.QtCore import Qt
from bordermap.border_map import BorderMapPart
from propertymap.property_map import PropertyMapPart
from functionmap.function_map import FunctionMapPart


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mm_label = QLabel()
        self.border_map_bt = QPushButton()
        self.property_map_bt = QPushButton()
        self.function_map_bt = QPushButton()
        self.exit_bt = QPushButton()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('主窗口')
        self.resize(1000, 800)

        self.mm_label = QLabel('ECoG脑功能定位临床应用软件')
        self.mm_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.mm_label.setStyleSheet('QLabel{color:rgb(0, 0, 0, 255);font-size:30px;font-weight:bold;font-family:Arial;}')

        main_button_style = 'QPushButton{color:rgb(0, 0, 0, 255);font-size:20px;font-weight:bold;font-family:Arial;}'

        self.border_map_bt.setText('功能区边界定位图')
        self.border_map_bt.setFixedSize(200, 100)
        self.border_map_bt.setStyleSheet(main_button_style)
        self.border_map_bt.clicked.connect(self.border_bt_clicked)

        self.property_map_bt = QPushButton('功能区属性定位图')
        self.property_map_bt.setFixedSize(200, 100)
        self.property_map_bt.setStyleSheet(main_button_style)
        self.property_map_bt.clicked.connect(self.property_bt_clicked)

        self.function_map_bt.setText('功能区地形图')
        self.function_map_bt.setFixedSize(200, 100)
        self.function_map_bt.setStyleSheet(main_button_style)
        self.function_map_bt.clicked.connect(self.function_bt_clicked)

        # 创建按钮实例，按钮名称：关闭主窗口
        self.exit_bt = QPushButton('退出')
        self.exit_bt.setFixedSize(100, 50)
        # 按钮的clicked信号与onButtonClick槽函数关联起来
        self.exit_bt.clicked.connect(self.exit_bt_clicked)

        # 水平布局
        main_hlayout = QHBoxLayout()
        main_hlayout.addWidget(self.border_map_bt)
        main_hlayout.addWidget(self.property_map_bt)
        main_hlayout.addWidget(self.function_map_bt)
        hwg = QWidget()
        hwg.setLayout(main_hlayout)

        # 垂直布局
        v_layout = QVBoxLayout()
        v_layout.addStretch(1)
        v_layout.addWidget(self.mm_label)
        v_layout.addStretch(1)
        v_layout.addWidget(hwg)
        v_layout.addStretch(1)
        v_layout.addWidget(self.exit_bt, alignment=Qt.AlignRight)
        v_layout.addStretch(1)

        # 创建widget窗口实例
        main_frame = QWidget()
        # 加载布局
        main_frame.setLayout(v_layout)
        # 把widget窗口加载到主窗口的中央位置
        self.setCentralWidget(main_frame)
        global dialog1, dialog2, dialog3
        dialog1 = BorderMapPart()
        dialog2 = PropertyMapPart()
        dialog3 = FunctionMapPart()
        dialog2.send_msg.connect(dialog3.get)

    def border_bt_clicked(self):
        # dialog1 = BorderMapPart(self)
        dialog1.exec()
        dialog1.destroy()

    def property_bt_clicked(self):
        # dialog2 = PropertyMapPart(self)
        dialog2.exec()
        dialog2.destroy()

    def function_bt_clicked(self):
        # dialog3 = FunctionMapPart(self)
        dialog3.exec()
        dialog3.destroy()

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
    main_app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(main_app.exec_())
