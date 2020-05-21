#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/19 21:56
# @Author: xuyongchuan
# @File  : border_map_intro.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class BorderMapIntro(QWidget):
    def __init__(self, parent=None):
        super(BorderMapIntro, self).__init__(parent)
        self.intro_label = QTextEdit()
        self.intro_label.setReadOnly(True)
        self.setupUI()

    def setupUI(self):
        # div{
        #     width:200px;height:200px;  # /*设置div的大小*/
        # }
        html = '''
            <font size = 4><font size = 5 color = blue><b><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
            &nbsp;&nbsp;功能区边界定位图部分</div></b></font><p>\
            这里是整个系统的第一部分，这部分的主要功能是首先对输入的脑电信号进行预处理和特征提取操作，接着使用聚类模型识别电极属性\
            ，最后在电极分布图上画出功能区边界定位图。这部分的主要内容由以下几个步骤组成：<p>\
            <font size = 4><b>1.导入数据:</b></font>处理数据的第一步操作，选择要处理的数据并导入。<br/><br/>\
            <font size = 4><b>2.预处理及特征提取:</b></font>这一步进行一些脑电数据分析常规的数据预处理操作，对ECoG数据来说，得益于\
            较好的数据质量预处理只包括49-51Hz陷波滤波，和1Hz高通滤波。接着使用db3小波对处理过的数据进\
            行六层小波分解，计算七个子频带的能量占比作为特征。<br/><br/>\
            <font size = 4><b>3.模型加载与识别:</b></font>选择识别电极属性时想要使用的聚类算法，并确定相应的模型参数。识别出电极的\
            类别。<br/><br/>\
            <font size = 4><b>4.导入电极分布图:</b></font>导入采集脑电数据时电极在皮质上的位置的图片。<br/><br/>\
            <font size = 4><b>5.边界定位图:</b></font>利用第三步得出的电极类别，采用双线性插值的方法在第四步导入的图片上画出等高线\
            图，得到不同类别的电极之间的边界定位图。<br/><br/></font>\
        '''
        self.intro_label.setHtml(html)
        self.intro_label.setStyleSheet('QTextEdit{border:none}')
        layout = QVBoxLayout()
        layout.addWidget(self.intro_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BorderMapIntro()
    win.show()
    sys.exit(app.exec_())
