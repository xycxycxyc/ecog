#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/5/12 20:46
# @Author: xuyongchuan
# @File  : generete_border_map.py


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class GenerateBorderMap(QWidget):
    def __init__(self, parent=None):
        super(GenerateBorderMap, self).__init__(parent)
        self.show_border_map_button = QPushButton()
        self.border_map_label = QLabel()
        self.setupUI()
        self.pic = None

        self.border_map_label.setHidden(True)

    def setupUI(self):
        layout = QVBoxLayout()
        self.show_border_map_button.setText('生成边界定位图')
        self.show_border_map_button.clicked.connect(self.show_border_map)

        layout.addWidget(self.show_border_map_button, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(self.border_map_label, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def show_border_map(self):
        self.border_map_label.setHidden(False)

    def set_pixmap(self, pixmap):
        if not pixmap:
            pass
        else:
            self.border_map_label.setPixmap(pixmap)
            self.border_map_label.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GenerateBorderMap()
    win.show()
    sys.exit(app.exec_())