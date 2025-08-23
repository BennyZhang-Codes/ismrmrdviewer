import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from ismrmrdviewer.ui.MainWindow import MainWindow
from icon import icon_rc

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowIcon(QIcon(":icon.ico"))
    mainWindow.setWindowTitle('ISMRMRD Viewer - Jinyuan Zhang')
    mainWindow.resize(1200, 800)
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()