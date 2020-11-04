#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/19 21:56
# @Author: xuyongchuan
# @File  : function_map_intro.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class FunctionMapIntro(QWidget):
    def __init__(self, parent=None):
        super(FunctionMapIntro, self).__init__(parent)
        self.intro_label = QTextEdit()
        self.intro_label.setReadOnly(True)
        self.setupUI()

    def setupUI(self):
        # div{
        #     width:200px;height:200px;  # /*设置div的大小*/
        # }
        html = '''
            <font size = 4><font size = 5 color = blue><b><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
            &nbsp;&nbsp;基于聚类和分类的功能定位部分</div></b></font><p>\
            这里是整个系统的第三部分，这部分的主要内容是利用前两个部分分别生成的功能区边界定位图和功能区属性定位图合成最终的\
            功能区地形图。这部的主要内容包括以下几个步骤：<p>\
            <font size = 4><b>1.功能区地形图:</b></font>利用前两步得到的边界定位图和属性定位图结合对应的合成算法，得到功能区地形图。\
            <br/><br/></font>
        '''
        self.intro_label.setHtml(html)
        self.intro_label.setStyleSheet('QTextEdit{border:none}')
        layout = QVBoxLayout()
        layout.addWidget(self.intro_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FunctionMapIntro()
    win.show()
    sys.exit(app.exec_())



