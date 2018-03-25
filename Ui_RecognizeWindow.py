# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\study\pyqt5\recognize\RecognizeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(910, 562)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("backgrouong_color:rgqconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255))rgb(255, 255, 255)b(255, 255, 255)\n"
"")
        Dialog.setSizeGripEnabled(True)
        self.Button_bro = QtWidgets.QPushButton(Dialog)
        self.Button_bro.setGeometry(QtCore.QRect(530, 40, 93, 31))
        self.Button_bro.setObjectName("Button_bro")
        self.Button_close = QtWidgets.QPushButton(Dialog)
        self.Button_close.setGeometry(QtCore.QRect(810, 520, 93, 28))
        self.Button_close.setObjectName("Button_close")
        self.label_picAdr = QtWidgets.QLabel(Dialog)
        self.label_picAdr.setGeometry(QtCore.QRect(30, 10, 451, 91))
        self.label_picAdr.setObjectName("label_picAdr")
        self.pushButton_recognize = QtWidgets.QPushButton(Dialog)
        self.pushButton_recognize.setGeometry(QtCore.QRect(420, 450, 93, 41))
        self.pushButton_recognize.setObjectName("pushButton_recognize")
        self.label_img = QtWidgets.QLabel(Dialog)
        self.label_img.setEnabled(True)
        self.label_img.setGeometry(QtCore.QRect(50, 120, 371, 291))
        self.label_img.setObjectName("label_img")
        self.textEdit_text = QtWidgets.QTextEdit(Dialog)
        self.textEdit_text.setGeometry(QtCore.QRect(490, 120, 361, 301))
        self.textEdit_text.setObjectName("textEdit_text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(610, 430, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 500, 531, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background_color:rgb(255, 0, 0)")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.Button_close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_bro.setText(_translate("Dialog", "浏览图片"))
        self.Button_close.setText(_translate("Dialog", "关闭窗口"))
        self.label_picAdr.setText(_translate("Dialog", "图片地址..."))
        self.pushButton_recognize.setText(_translate("Dialog", "识别文字"))
        self.label_img.setText(_translate("Dialog", "原始图像"))
        self.label.setText(_translate("Dialog", "识别结果（可复制！）"))
        self.label_2.setText(_translate("Dialog", "提示：本软件调用百度OCR(文字识别库)，每天识别次数限量，如无法识别，请周知！（赵明2018.3.25）"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

