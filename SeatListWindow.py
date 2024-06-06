# Ui_Dialog_Set_Seat of SeatChanger v1.0.4
# Updated on 2024.5.12

import datetime

from PyQt6 import QtCore, QtWidgets


class Ui_Dialog_Set_Seat(object):
    def __init__(self, SeatListShare, SeatImage1, Flag_Cancel, Value):
        self.SeatListShare = SeatListShare
        self.SeatImage1 = SeatImage1
        self.Flag_Cancel = Flag_Cancel
        self.Value = Value

    def read_seat_list(self):
        liststr = self.lineEdit_2.text()
        try:
            list1 = eval(liststr)
            if len(list1) != 2:
                raise Exception()
            for i in range(2):
                for j in range(25):
                    if list1[i][j] > 51 or list1[i][j] < 1:
                        raise Exception()
                    self.SeatListShare[i][j] = list1[i][j]
            return False
        except:
            return True

    def read_date(self):
        date = self.lineEdit.text()
        try:
            dateclass = datetime.datetime.strptime(date, "%Y-%m-%d")
            datenow = datetime.datetime.now()
            if datenow <= dateclass:
                raise Exception()
            self.SeatImage1.StartDate = date
            return False
        except:
            return True

    def read_value(self):
        value = self.lineEdit_3.text()
        try:
            value = int(value)
            self.Value[0] = value
            return False
        except:
            return True

    def update_seat_list(self, Dialog):
        flag = self.read_seat_list()
        flag1 = self.read_date()
        flag2 = self.read_value()
        self.SeatImage1.UpdateSeatListFromShare()
        if flag:
            QtWidgets.QMessageBox.critical(Dialog, "错误", "输入的SeatList有误",
                                           QtWidgets.QMessageBox.StandardButton.Ok)
        elif flag1:
            QtWidgets.QMessageBox.critical(Dialog, "错误", "输入的StartTime有误",
                                           QtWidgets.QMessageBox.StandardButton.Ok)
        elif flag2:
            QtWidgets.QMessageBox.critical(Dialog, "错误", "输入的偏移量有误",
                                           QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            global Flag_Cancel
            Flag_Cancel = False
            Dialog.close()

    def cancel(self, Dialog):
        self.Flag_Cancel[0] = True
        Dialog.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 187)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置初始座位"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label.setText(_translate("Dialog", "输入由开发者提供的SeatList"))
        self.label_3.setText(_translate("Dialog", "输入偏移量"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.label_2.setText(_translate("Dialog", "输入由开发者提供的StartTime"))

        self.pushButton.setFocus()
        self.lineEdit_2.setText(str(self.SeatListShare))
        self.lineEdit.setText(self.SeatImage1.StartDate)
        self.lineEdit_3.setText(str(self.Value[0]))
        self.pushButton.clicked.connect(lambda: self.update_seat_list(Dialog))
        self.pushButton_2.clicked.connect(lambda: self.cancel(Dialog))
