#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/19 21:56
# @Author: xuyongchuan
# @File  : property_map_intro.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class PropertyMapIntro(QWidget):
    def __init__(self, parent=None):
        super(PropertyMapIntro, self).__init__(parent)
        self.intro_label = QTextEdit()
        self.intro_label.setReadOnly(True)
        self.setupUI()

    def setupUI(self):
        # div{
        #     width:200px;height:200px;  # /*设置div的大小*/
        # }
        html = '''
            <font size = 4><font size = 5 color = blue><b><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
            &nbsp;&nbsp;功能区属性定位图部分</div></b></font><p>\
            这里是整个系统的第二部分，这部分的主要内容是根据经典的解剖学定位图，结合和脑皮质的主要沟回确\
            定功能区的在脑皮质的相对位置，接着使用图像处理的方法标记出不同属性的功能区边界。得到功能区属性定位图。\
            这部分的主要内容由以下几个步骤组成：<p>\
            <font size = 4><b>1.加载皮质图片:</b></font>加载开颅后的皮质图片。<br/><br/>\
            <font size = 4><b>2.属性定位图:</b></font>主要技术路线是根据经典的解剖学定位图，结合和脑皮质的主要沟回确\
            定功能区的在脑皮质的相对位置，接着使用图像处理的方法标记出不同属性的功能区边界,得到功能区属性定位图。<br/><br/></font>\

        '''
        self.intro_label.setHtml(html)
        self.intro_label.setStyleSheet('QTextEdit{border:none}')
        layout = QVBoxLayout()
        layout.addWidget(self.intro_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PropertyMapIntro()
    win.show()
    sys.exit(app.exec_())



