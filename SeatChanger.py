# MainProgram of SeatChanger version:1.0.2

import sys

from PyQt6 import QtGui, QtWidgets

from SeatImageClass import SeatImageClass
from MainWindow import Ui_MainWindow

Font_UI = QtGui.QFont("等线", 11)
Font_Table = QtGui.QFont("等线", 12)
SeatListShare = [[0 for i in range(25)], [0 for j in range(25)]]
Flag_Cancel=[False]
SeatImage1 = SeatImageClass(SeatListShare)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(Font_UI)
    Window = QtWidgets.QMainWindow()
    UI = Ui_MainWindow(SeatImage1,Flag_Cancel,SeatListShare,Window,Font_Table)
    UI.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
