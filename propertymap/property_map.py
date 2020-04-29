#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2020/4/23 11:34
# @Author: xuyongchuan
# @File  : property_map.py

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QHBoxLayout, QFileDialog, \
    QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap


class PropertyMapPart(QDialog):
    send_msg = pyqtSignal()

    def __init__(self, parent=None):  # 为什么被调用的类里面需要写parent=None参数
        super(PropertyMapPart, self).__init__(parent)
        self.property_title_lb = QLabel()
        self.image_lb1 = QLabel()
        self.image_lb2 = QLabel()
        self.load_image_bt = QPushButton()
        self.show_image_bt = QPushButton()
        self.save_bt = QPushButton()
        self.setupUI()
        self.pp_map_path = ''  # 保存生成的property路径

    def setupUI(self):
        self.resize(800, 600)
        self.setWindowTitle('属性定位图部分')
        property_label_style = 'QLabel{color:rgb(0, 0, 0, 255);font-size:30px;font-weight:bold;font-family:Arial;}'
        property_button_style = 'QPushButton{color:rgb(0, 0, 0, 255);font-size:20px;font-weight:bold;font-family:Arial;}'

        self.property_title_lb.setText('属性定位图部分')
        self.property_title_lb.setStyleSheet(property_label_style)

        self.load_image_bt.setText('加载图片')
        self.load_image_bt.setStyleSheet(property_button_style)
        self.load_image_bt.setFixedSize(150, 40)
        self.load_image_bt.clicked.connect(self.load_image)

        self.image_lb1.setFixedSize(400, 300)
        self.image_lb2.setFixedSize(400, 300)

        self.show_image_bt.setText('显示属性定位图')
        self.show_image_bt.setStyleSheet(property_button_style)
        self.show_image_bt.setFixedSize(150, 40)
        self.show_image_bt.clicked.connect(self.show_image)

        self.save_bt.setText('保存定位图')
        self.save_bt.setStyleSheet(property_button_style)
        self.save_bt.setFixedSize(150, 40)
        self.save_bt.clicked.connect(self.save_image)

        property_hlayout1 = QHBoxLayout()
        property_hlayout1.addWidget(self.load_image_bt)
        property_hlayout1.addWidget(self.show_image_bt)
        dialog1 = QDialog()
        dialog1.setLayout(property_hlayout1)

        property_hlayout2 = QHBoxLayout()
        property_hlayout2.addWidget(self.image_lb1)
        property_hlayout2.addWidget(self.image_lb2)
        dialog2 = QDialog()
        dialog2.setLayout(property_hlayout2)

        property_vlayout = QVBoxLayout()
        property_vlayout.addWidget(self.property_title_lb, alignment=Qt.AlignCenter)
        property_vlayout.addWidget(dialog1)
        property_vlayout.addWidget(dialog2)
        property_vlayout.addWidget(self.save_bt, alignment=Qt.AlignRight)

        self.setLayout(property_vlayout)
        # self.setCentralWidget()

    def run(self):
        self.send_msg.emit('hello pyqt5')

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '选择皮质图片', '.', '图像文件(*.png, *.jpg)')
        # self.image_label1.setPixmap(QPixmap(file_name).scaled(400, 300))
        self.image_lb1.setPixmap(QPixmap(file_name))
        self.image_lb1.setScaledContents(True)  # 让图片自适应label的大小

    def show_image(self):
        if not self.image_lb1.pixmap():
            QMessageBox.about(self, '提示', '请先加载皮质图像')
        else:
            result = self.image_lb1.pixmap()
            self.image_lb2.setPixmap(result)
            self.image_lb2.setScaledContents(True)

    def save_image(self):
        if not self.image_lb2.pixmap():
            QMessageBox.about(self, '提示', '请先生成功能区属性定位图')
        else:
            try:
                result = self.image_lb2.pixmap()

                fname, ftype = QFileDialog.getSaveFileName(self, 'save file', './', '图像文件(*.png, *.jpg)')
                if fname:
                    result.save(fname)
                    QMessageBox.information(self, '提示', '保存成功', QMessageBox.Yes)
                    self.send_msg.emit('hello pyqt5')

                else:
                    QMessageBox.warning(self, '警告', '请输入正确的文件名', QMessageBox.Yes)

            except IOError:
                print('保存图片失败')


if __name__ == '__main__':
    property_app = QApplication(sys.argv)
    property_win = PropertyMapPart()
    property_win.show()
    sys.exit(property_app.exec_())