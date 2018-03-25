# -*- coding: utf-8 -*-

"""
Module implementing RecognizeWindow.
"""
from PIL import Image
import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_RecognizeWindow import Ui_Dialog
from common import config
from common.baiduocr import get_text_from_image

global file_name, app_id, app_key, app_secret, text
app_id = '10689406'
app_key = 'BAubMHA9tfxbMQxuGoOwpwgg'
app_secret = '1Ke1XWpQdKCitRfbVAORf8S92eAGBXvX'
text = '我是赵义柔'
class MyThread(QThread):
    def __init__(self, parent = None):
        super(MyThread, self).__init__(parent)
    def run(self):
        pass
        #global file_name
        

class RecognizeWindow(QDialog, Ui_Dialog):
    
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(RecognizeWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.setWindowTitle("图片文字识别软件-赵明2018.3.25（待完善）")
        self.setWindowIcon(QIcon('H:\\study\\pyqt5\\recognize\\zm.jpg'))   #图标的位置 
    @pyqtSlot()
    def on_Button_bro_clicked(self):
        global file_name
        file_name, file_type = QFileDialog.getOpenFileName(self,"选择一张图片",".","*.jpg")
        self.label_picAdr.setText(file_name)
        img = cv2.imread(file_name)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = img.shape
        qimg = QImage(img_rgb.data, width, height,3*width, QImage.Format_RGB888)#原始图
        qpiximg = QPixmap.fromImage(qimg)
        self.label_img.setPixmap(qpiximg.scaled(self.label_img.width(), self.label_img.height()))
    @pyqtSlot()
    def on_pushButton_recognize_clicked(self):
        #thread.start()
        img = cv2.imread(file_name)
        f = open(file_name, 'rb')
        im = f.read()
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, bytesPerComponent = img.shape
        text = get_text_from_image(im, app_id, app_key, app_secret, 0, 3)
        self.textEdit_text.setMaximumWidth(400)
        self.textEdit_text.setText(text)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = RecognizeWindow()
    dlg.show()
    thread = MyThread()
    sys.exit(app.exec_())
