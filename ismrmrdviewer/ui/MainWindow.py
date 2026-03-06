
import os
import logging
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, QStandardPaths
from PySide6.QtGui import QAction

from .FileWidget import FileWidget


class MainWindow(QtWidgets.QMainWindow):

    open = Signal(str)

    def __init__(self):
        super().__init__()

        self.last_dir = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)

        self.setUnifiedTitleAndToolBarOnMac(True)

        self.fileMenu = super().menuBar().addMenu("&File")
        open_action = QAction("&Open", self)
        open_action.setShortcut("Ctrl+O") 
        open_action.triggered.connect(self.open_file_dialog)
        self.fileMenu.addAction(open_action)

        self.fileMenu.addSeparator()

        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q") 
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.close) 
        self.fileMenu.addAction(exit_action)

        self.open.connect(self.open_file)

    @Slot()
    def open_file_dialog(self):

        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open ISMRMRD Data File",
            self.last_dir,
            "ISMRMRD Data Files (*.h5 *.mrd);;All Files (*)"
        )

        if file_name:
            self.last_dir = os.path.dirname(file_name) 
            self.open.emit(file_name)

    def open_file(self, file_name):
        logging.info(f"Opening file: {file_name}")
        self.setWindowFilePath(file_name)
        self.setCentralWidget(FileWidget(self, file_name))


