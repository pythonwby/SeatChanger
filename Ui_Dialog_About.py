# Ui_Dialog_About of SeatChanger v1.0.2
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_About(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(535, 395)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.resize(400, 300)
        Dialog.setWindowTitle(_translate("Dialog", "关于"))
        # self.label_2.setText(_translate("Dialog", "该项目已在Github上开源:github.com/pythonwby/SeatChanger"))
        self.label.setText(_translate("Dialog", "座位计算器v1.0.1 By 乌搏猿 2024.4.7"))
        self.textEdit.setText('''该项目已在Github上开源:
github.com/pythonwby/SeatChanger

制作本程序使用的软件和工具：

Python 3.12.2
PyCharm Community Edition
PyQt6.QtWidgets
PyQt6.QtCore
PyQt6.QtGUI
QtDesigner6
DateTime
Pyinstaller 
UPX''')
        self.textEdit.setReadOnly(True)
