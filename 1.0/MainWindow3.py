# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
from typing import Any

from PyQt6 import QtCore, QtGui, QtWidgets
class SeatImageClass:
    SeatList = [[8,47,7, 22, 6, 10, 23, 37, 14, 5, 27, 46, 12, 51, 39, 15, 49, 3, 2, 18, 50, 43, 41, 19, 1],
            # 靠左列，第五组靠后
            [9,40,29, 30, 48, 25, 34, 31, 36, 33, 16, 45, 11, 35, 28, 32, 21, 13, 24, 38, 20, 4, 42, 17, 26]]  # 靠右列，第五组靠前
    SeatListNew = [[0] * 25, [0] * 25]
    NumberToName = ["", "蔡宇轩", "陈锦轩", "陈怡杉", "代宇彤", "丁艺贝", "丁屹城", "丁梓馨", "冯浚", "高千惠", "郭俊雄",
                "韩呈奕", "华婧朵", "晋熙儿", "冷宣澄", "李欣蔓", "李育涵", "刘瑞琦", "刘雅雯",
                "刘姿雨", "柳子慧", "罗梓涵", "毛家盼", "毛琳悦", "孟雨禾", "潘志杰", "彭悦", "秦树成", "邱宣博",
                "宋修仪", "宋雅静", "孙浩涵", "汤文博", "汪君瑜", "王淑涵", "魏晋宇", "魏熠宸",
                "吴博远", "吴谦益", "夏康洋", "向宏博", "熊梓煊", "徐艺轩", "杨惜婷", "姚熙子正", "易峻熙", "詹晨旺",
                "张峻豪", "赵艺涵", "周子君", "熊通", "左恩森"]
    SeatImage = [[-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, ]
    def __init__(self):
        self.SeatImage[1][0] = 44
    def NextWeek(self):
        self.SeatListNew[0][0] = self.SeatList[0][23]
        self.SeatListNew[0][1] = self.SeatList[0][24]
        self.SeatListNew[1][0] = self.SeatList[1][23]
        self.SeatListNew[1][1] = self.SeatList[1][24]
        for i in range(2, 25):
            self.SeatListNew[0][i] = self.SeatList[0][i - 2]
            self.SeatListNew[1][i] = self.SeatList[1][i - 2]

        for i in range(0, 25):
            self.SeatList[0][i] = self.SeatListNew[0][i]
            self.SeatList[1][i] = self.SeatListNew[1][i]
    def LastWeek(self):
        self.SeatListNew[0][23] = self.SeatList[0][0]
        self.SeatListNew[0][24] = self.SeatList[0][1]
        self.SeatListNew[1][23] = self.SeatList[1][0]
        self.SeatListNew[1][24] = self.SeatList[1][1]
        for i in range(0, 23):
            self.SeatListNew[0][i] = self.SeatList[0][i + 2]
            self.SeatListNew[1][i] = self.SeatList[1][i + 2]
        for i in range(0, 25):
            self.SeatList[0][i] = self.SeatListNew[0][i]
            self.SeatList[1][i] = self.SeatListNew[1][i]
    def ListToImage(self):
        for i in range(1, 7):
            self.SeatImage[6][i] = self.SeatList[1][i - 1]
            self.SeatImage[5][i] = self.SeatList[0][i - 1]
        for i in range(0, 8):
            self.SeatImage[4][i] = self.SeatList[1][i + 6]
            self.SeatImage[3][i] = self.SeatList[0][i + 6]
        for i in range(0, 4):
            self.SeatImage[2][i * 2 + 1] = self.SeatList[0][i + 14]
            self.SeatImage[2][i * 2] = self.SeatList[1][i + 14]
        for i in range(0, 7):
            self.SeatImage[1][i + 1] = self.SeatList[1][i + 18]
            self.SeatImage[0][i + 1] = self.SeatList[0][i + 18]

    def PrintImage(self):  # for debug
        for i in range(0, 8):
            for j in range(0, 7):
                if self.SeatImage[j][i] == -1:
                    print('      ', end='')
                    continue
                tmp = self.NumberToName[self.SeatImage[j][i]]
                if tmp == '彭悦':
                    tmp = '彭  悦'
                if tmp == '熊通':
                    tmp = '熊  通'
                if tmp == '冯浚':
                    tmp = '冯  浚'
                if tmp == '姚熙子正':
                    tmp1 = "\b\b" + tmp
                    tmp = tmp1
                tmp += " "
                print(tmp, end="")
                if j == 1 or j == 4:
                    print("|", end="")
            print("\n", end="")
        print('''
        ------------------------------------------
        ''')
SeatImage1=SeatImageClass()

class Ui_MainWindow(object):
    week_cnt=0
    # SeatImage1=SeatImageClass()
    SeatImageItem=[[QtWidgets.QTableWidgetItem for j in range(7)] for i in range(8)]
    Font=QtGui.QFont("等线",12)
    def next_week(self):
        self.week_cnt+=1
        self.label.setText(f"第{self.week_cnt}周后")
        print("Next Week Pressed.")
        self.update_table_widget(False)
    def last_week(self):
        self.week_cnt-=1
        self.label.setText(f"第{self.week_cnt}周后")
        print("Last Week Pressed.")
        self.update_table_widget(True)
    def update_table_widget(self,flag):  # 更新表格，flag=True，下一周
        self.tableWidget.removeColumn(2)
        self.tableWidget.removeColumn(6)
        if not flag:
            SeatImage1.NextWeek()
            SeatImage1.ListToImage()
        else:
            SeatImage1.LastWeek()
            SeatImage1.ListToImage()
        for i in range(8):
            for j in range(7):
                tempitem=QtWidgets.QTableWidgetItem()
                if SeatImage1.SeatImage[j][i]==-1:
                    tempitem.setText('')
                else:
                    tempitem.setText(SeatImage1.NumberToName[SeatImage1.SeatImage[j][i]])
                tempitem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                tempitem.setFont(self.Font)
                self.tableWidget.setItem(i,j,tempitem)
        self.tableWidget.insertColumn(2)
        self.tableWidget.insertColumn(6)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 459)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 5)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "座位计算器"))
        MainWindow.resize(700,500)
        self.label.setText(_translate("MainWindow", f"第{self.week_cnt}周后"))
        self.pushButton.setText(_translate("MainWindow", "上一周"))
        self.pushButton_2.setText(_translate("MainWindow", "下一周"))
        self.pushButton.clicked.connect(self.last_week)
        self.pushButton_2.clicked.connect(self.next_week)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.update_table_widget(True)
        self.update_table_widget(False)

if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Window=QtWidgets.QMainWindow()
    UI=Ui_MainWindow()
    UI.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
