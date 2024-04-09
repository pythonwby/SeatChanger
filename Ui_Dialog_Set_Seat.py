# Ui_Dialog_Set_Seat of SeatChanger v1.0.2
import datetime

from PyQt6 import QtCore, QtWidgets


class Ui_Dialog_Set_Seat(object):
    def __init__(self,SeatListShare,SeatImage1,Flag_Cancel):
        self.SeatListShare=SeatListShare
        self.SeatImage1=SeatImage1
        self.Flag_Cancel=Flag_Cancel
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

    def update_seat_list(self, Dialog):
        flag = self.read_seat_list()
        flag1 = self.read_date()
        self.SeatImage1.UpdateSeatListFromShare()
        if flag:
            QtWidgets.QMessageBox.critical(Dialog, "错误", "输入的SeatList有误",
                                           QtWidgets.QMessageBox.StandardButton.Ok)
        elif flag1:
            QtWidgets.QMessageBox.critical(Dialog, "错误", "输入的StartTime有误",
                                           QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            global Flag_Cancel
            Flag_Cancel = False
            Dialog.close()

    def cancel(self, Dialog):
        self.Flag_Cancel[0]=True
        Dialog.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置初始座位"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton.setFocus()
        self.label_2.setText(_translate("Dialog", "输入由开发者提供的StartTime"))
        self.label.setText(_translate("Dialog", "输入由开发者提供的SeatList"))
        self.lineEdit_2.setText(str(self.SeatListShare))
        self.lineEdit.setText(self.SeatImage1.StartDate)
        self.pushButton.clicked.connect(lambda: self.update_seat_list(Dialog))
        self.pushButton_2.clicked.connect(lambda: self.cancel(Dialog))
