# MainProgram of SeatChanger version:1.0.3
# Updated on 2024.5.12

import sys

from PyQt6 import QtGui, QtWidgets

from SeatImageClass import SeatImageClass
from MainWindow import Ui_MainWindow

Font_UI = QtGui.QFont("等线", 11)
Font_Table = QtGui.QFont("等线", 12)
SeatListShare = [[0 for i in range(25)], [0 for j in range(25)]]
Flag_Cancel = [False]
SeatImage1 = SeatImageClass(SeatListShare)
Value = [-2]  # 座位偏移量：正数为向后偏移，负数为向前偏移

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(Font_UI)
    Window = QtWidgets.QMainWindow()
    UI = Ui_MainWindow(SeatImage1, Flag_Cancel, SeatListShare, Window, Font_Table, Value)
    UI.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
