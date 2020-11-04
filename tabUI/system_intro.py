#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/19 21:56
# @Author: xuyongchuan
# @File  : system_intro.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class SystemIntro(QWidget):
    def __init__(self, parent=None):
        super(SystemIntro, self).__init__(parent)
        self.intro_label = QTextEdit()
        self.intro_label.setReadOnly(True)
        self.setupUI()

    def setupUI(self):
        # div{
        #     width:200px;height:200px;  # /*设置div的大小*/
        # }
        html = '''
            <font size = 4><font size = 5 color = blue><b><div>&nbsp;\
            &nbsp;基于静息态ECoG聚类和二分类的术中脑功能定位系统</div></b></font><p>\
            本系统的主要功能是协助医生在脑外科手术中准确定位皮质功能区的位置，并实时指导医生进行开颅手术，减轻医生的手术负担。\
            主要技术路线是通过机器学习的方法识别出不同属性的电极，并画出不同类别的等高线地形图作为不同类别类别的功能区的边界\
            定位图,然后结合使用解剖学定位与图像处理的方法画出功能区的属性定图，最后一步是使用前两步得到的功能区边界定位图和功\
            能区属性定位图合成最终指导医生手术的脑皮层功能区地形图。因此，本系统主要由以下三个部分组成：<p>\
            <font size = 4><b>1.功能区边界聚类算法:</b></font>主要技术路线是采用机器学习的方法。对输入的ECoG数据进行预处理，\
            特征提取，接着使用聚类算法识别出不同功能区属性的电极，并画出相应的等高线图，得到功能区边界定位图<br/><br/>
            <font size = 4><b>2.功能区属性分类算法:</b></font>主要技术路线是根据经典的解剖学定位图，结合和脑皮质的主要沟回确\
            定功能区的在脑皮质的相对位置，接着使用图像处理的方法标记出不同属性的功能区边界。得到功能区属性定位图。<br/><br/>\
            <font size = 4><b>3.基于聚类和分类的脑功能定位算法:</b></font>主要技术路线是使用前两步得到的边界定位图和属性定位图合成最终的功能\
            区地形图。<br/><br/></font>\

        '''
        self.intro_label.setHtml(html)
        self.intro_label.setStyleSheet('QTextEdit{border:none}')
        layout = QVBoxLayout()
        layout.addWidget(self.intro_label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SystemIntro()
    win.show()
    sys.exit(app.exec_())



