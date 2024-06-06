# Ui_Dialog_About of SeatChanger v1.0.4
# Updated on 2024.4.10

from PyQt6 import QtCore, QtWidgets


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
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于"))
        self.label_2.setText(_translate("Dialog", "制作本程序使用的软件和工具："))
        self.label.setText(_translate("Dialog", "座位计算器v1.0.4 By 乌搏猿 2024.6.6"))
        self.label_3.setText(_translate("Dialog",
                                        "该项目已在Github上开源:<a href=\'github.com/pythonwby/SeatChanger\'>github.com/pythonwby/SeatChanger</a>"))
        self.label_3.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.textEdit.setText('''Python 3.10.14
Python 3.8.19 (only Win7 version)
MiniConda
PyCharm Community Edition
PyQt6
QtDesigner6
DateTime
Pip
Pyinstaller 
the Ultimate Packer for eXecutables(UPX)''')
        self.textEdit.setReadOnly(True)
