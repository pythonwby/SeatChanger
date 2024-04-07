# version:1.0.1

import sys
import datetime
from PyQt6 import QtCore, QtGui, QtWidgets

Font_UI = QtGui.QFont("等线", 11)
Font_Table = QtGui.QFont("等线", 12)
SeatListShare = [[0 for i in range(25)], [0 for j in range(25)]]
Flag_Cancel = False


def count_thursdays(start_date):
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    end = datetime.datetime.today()
    delta = (end - start).days
    thursdays = 0
    for i in range(delta):
        date = start + datetime.timedelta(i)
        if date.weekday() == 3:
            thursdays += 1
    return thursdays


class SeatImageClass:
    SeatList = [[48, 4, 27, 16, 17, 42, 1, 49, 38, 45, 15, 33, 25, 36, 7, 24, 41, 21, 51, 40, 28, 6, 10, 3, 12],
                # 靠左列，第五组靠后
                [46, 50, 47, 9, 22, 31, 18, 29, 19, 14, 20, 30, 26, 32, 5, 34, 13, 23, 39, 35, 37, 2, 11, 43,
                 8]]  # 靠右列，第五组靠前
    SeatListNew = [[0] * 25, [0] * 25]
    NumberToName = ["", "蔡宇轩", "陈锦轩", "陈怡杉", "代宇彤", "丁艺贝", "丁屹城", "丁梓馨", "冯浚", "高千惠",
                    "郭俊雄",
                    "韩呈奕", "华婧朵", "晋熙儿", "冷宣澄", "李欣蔓", "李育涵", "刘瑞琦", "刘雅雯",
                    "刘姿雨", "柳子慧", "罗梓涵", "毛家盼", "毛琳悦", "孟雨禾", "潘志杰", "彭悦", "秦树成", "邱宣博",
                    "宋修仪", "宋雅静", "孙浩涵", "汤文博", "汪君瑜", "王淑涵", "魏晋宇", "魏熠宸",
                    "吴博远", "吴谦益", "夏康洋", "向宏博", "熊梓煊", "徐艺轩", "杨惜婷", "姚熙子正", "易峻熙",
                    "詹晨旺",
                    "张峻豪", "赵艺涵", "周子君", "熊通", "左恩森"]
    SeatImage = [[-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, ]
    StartDate = "2024-4-4"

    def __init__(self):
        self.SeatImage[1][0] = 44
        for i in range(2):
            for j in range(25):
                SeatListShare[i][j] = self.SeatList[i][j]
        self.ListToImage()

    def UpdateSeatListFromShare(self):
        for i in range(2):
            for j in range(25):
                self.SeatList[i][j] = SeatListShare[i][j]
        self.ListToImage()

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


SeatImage1 = SeatImageClass()


class Ui_Dialog_Set_Seat(object):
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
                    SeatListShare[i][j] = list1[i][j]
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
            SeatImage1.StartDate = date
            return False
        except:
            return True

    def update_seat_list(self, Dialog):
        flag = self.read_seat_list()
        flag1 = self.read_date()
        SeatImage1.UpdateSeatListFromShare()
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
        global Flag_Cancel
        Flag_Cancel = True
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
        self.lineEdit_2.setText(str(SeatListShare))
        self.lineEdit.setText(SeatImage1.StartDate)
        self.pushButton.clicked.connect(lambda: self.update_seat_list(Dialog))
        self.pushButton_2.clicked.connect(lambda: self.cancel(Dialog))


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


class Ui_MainWindow(object):
    week_cnt = 0
    SeatImageItem = [[QtWidgets.QTableWidgetItem for j in range(7)] for i in range(8)]

    def refresh_table_widget(self):
        self.update_table_widget(True)
        self.update_table_widget(False)

    def next_week(self):
        self.week_cnt += 1
        if self.week_cnt == 0:
            self.label.setText("当前周")
        elif self.week_cnt < 0:
            self.label.setText(f"{abs(self.week_cnt)}周前")
        else:
            self.label.setText(f"{self.week_cnt}周后")
        print("Next Week Pressed.")
        self.update_table_widget(True)

    def last_week(self):
        self.week_cnt -= 1
        if self.week_cnt == 0:
            self.label.setText("当前周")
        elif self.week_cnt < 0:
            self.label.setText(f"{abs(self.week_cnt)}周前")
        else:
            self.label.setText(f"{self.week_cnt}周后")
        print("Last Week Pressed.")
        self.update_table_widget(False)

    def update_table_widget(self, flag):  # 更新表格，flag=True，下一周
        self.tableWidget.removeColumn(2)
        self.tableWidget.removeColumn(6)
        if flag:
            SeatImage1.NextWeek()
            SeatImage1.ListToImage()
        else:
            SeatImage1.LastWeek()
            SeatImage1.ListToImage()
        for i in range(8):
            for j in range(7):
                tempitem = QtWidgets.QTableWidgetItem()
                if SeatImage1.SeatImage[j][i] == -1:
                    tempitem.setText('')
                else:
                    tempitem.setText(SeatImage1.NumberToName[SeatImage1.SeatImage[j][i]])
                tempitem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                tempitem.setFont(Font_Table)
                self.tableWidget.setItem(i, j, tempitem)
        self.tableWidget.insertColumn(2)
        self.tableWidget.insertColumn(6)

    def open_seat_set_dialog(self):
        print("Seat Set Dialog Opened.")
        dialog = QtWidgets.QDialog(parent=Window)
        dialog_ui = Ui_Dialog_Set_Seat()
        dialog_ui.setupUi(dialog)
        dialog.show()
        dialog.exec()
        if Flag_Cancel:
            return
        thurs = count_thursdays(SeatImage1.StartDate)
        self.refresh_table_widget()
        for i in range(thurs):
            self.update_table_widget(True)
        self.label.setText("当前周")
        self.week_cnt = 0

    def open_about_dialog(self):
        print("About Dialog Opened.")
        dialog = QtWidgets.QDialog(parent=Window)
        dialog_ui = Ui_Dialog_About()
        dialog_ui.setupUi(dialog)
        dialog.show()
        dialog.exec()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 459)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(-1, 17, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
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
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 16777215, 21))
        self.menuBar.setObjectName("menuBar")
        self.set_seat_action = QtGui.QAction("设置初始座位", self.menuBar)
        self.about_action = QtGui.QAction("关于", self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "座位计算器"))
        MainWindow.resize(700, 500)
        self.label.setText(_translate("MainWindow", f"当前周"))
        self.pushButton.setText(_translate("MainWindow", "上一周"))
        self.pushButton_2.setText(_translate("MainWindow", "下一周"))
        self.pushButton.clicked.connect(self.last_week)
        self.pushButton_2.clicked.connect(self.next_week)
        self.menuBar.addAction(self.set_seat_action)
        self.menuBar.addAction(self.about_action)
        self.set_seat_action.triggered.connect(self.open_seat_set_dialog)
        self.about_action.triggered.connect(self.open_about_dialog)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.refresh_table_widget()

        thurs = count_thursdays(SeatImage1.StartDate)
        self.refresh_table_widget()
        for i in range(thurs):
            self.update_table_widget(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(Font_UI)
    Window = QtWidgets.QMainWindow()
    UI = Ui_MainWindow()
    UI.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
