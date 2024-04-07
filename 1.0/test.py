import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.fileMenu = QMenu(self.menuBar, "&File")
        self.editMenu = QMenu(self.menuBar, "&Edit")

        self.openAction = QAction("&Open", self.fileMenu)
        self.saveAction = QAction("&Save", self.fileMenu)
        self.exitAction = QAction("&Exit", self.fileMenu)

        self.cutAction = QAction("Cu&t", self.editMenu)
        self.copyAction = QAction("&Copy", self.editMenu)
        self.pasteAction = QAction("&Paste", self.editMenu)

        self.openAction.triggered.connect(self.on_openAction_triggered)
        self.saveAction.triggered.connect(self.on_saveAction_triggered)
        self.exitAction.triggered.connect(self.on_exitAction_triggered)

        self.cutAction.triggered.connect(self.on_cutAction_triggered)
        self.copyAction.triggered.connect(self.on_copyAction_triggered)
        self.pasteAction.triggered.connect(self.on_pasteAction_triggered)

    def on_openAction_triggered(self):
        print("Open action triggered")

    def on_saveAction_triggered(self):
        print("Save action triggered")

    def on_exitAction_triggered(self):
        print("Exit action triggered")

    def on_cutAction_triggered(self):
        print("Cut action triggered")

    def on_copyAction_triggered(self):
        print("Copy action triggered")

    def on_pasteAction_triggered(self):
        print("Paste action triggered")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())