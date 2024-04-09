# Ui_MainWindow of SeatChanger v1.0.2
from PyQt6 import QtCore, QtGui, QtWidgets

from Ui_Dialog_About import Ui_Dialog_About
from Ui_Dialog_Set_Seat import Ui_Dialog_Set_Seat


class Ui_MainWindow(object):
    def __init__(self, SeatImage1, Flag_Cancel, SeatListShare, Window, Font_Table):
        self.SeatImage1 = SeatImage1
        self.Flag_Cancel = Flag_Cancel
        self.SeatListShare = SeatListShare
        self.Window = Window
        self.Font_Table = Font_Table

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
            self.SeatImage1.NextWeek()
            self.SeatImage1.ListToImage()
        else:
            self.SeatImage1.LastWeek()
            self.SeatImage1.ListToImage()
        for i in range(8):
            for j in range(7):
                tempitem = QtWidgets.QTableWidgetItem()
                if self.SeatImage1.SeatImage[j][i] == -1:
                    tempitem.setText('')
                else:
                    tempitem.setText(self.SeatImage1.NumberToName[self.SeatImage1.SeatImage[j][i]])
                tempitem.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                tempitem.setFont(self.Font_Table)
                self.tableWidget.setItem(i, j, tempitem)
        self.tableWidget.insertColumn(2)
        self.tableWidget.insertColumn(6)

    def open_seat_set_dialog(self):
        print("Seat Set Dialog Opened.")
        dialog = QtWidgets.QDialog(parent=self.Window)
        dialog_ui = Ui_Dialog_Set_Seat(self.SeatListShare, self.SeatImage1, self.Flag_Cancel)
        dialog_ui.setupUi(dialog)
        dialog.show()
        dialog.exec()
        if self.Flag_Cancel[0]:
            self.Flag_Cancel[0] = False
            return
        thurs = self.SeatImage1.count_thursdays(self.SeatImage1.StartDate)
        self.refresh_table_widget()
        for i in range(thurs):
            self.update_table_widget(True)
        self.label.setText("当前周")
        self.week_cnt = 0

    def open_about_dialog(self):
        print("About Dialog Opened.")
        dialog = QtWidgets.QDialog(parent=self.Window)
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

        thurs = self.SeatImage1.count_thursdays(self.SeatImage1.StartDate)
        self.refresh_table_widget()
        for i in range(thurs):
            self.update_table_widget(True)
