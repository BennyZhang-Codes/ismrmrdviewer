import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from ismrmrdviewer.ui.MainWindow import MainWindow
from icon import icon_rc

def main():
    app = QApplication(sys.argv)
    
    app_icon = QIcon(":icon.ico")
    app.setWindowIcon(app_icon)

    mainWindow = MainWindow()
    mainWindow.setWindowIcon(app_icon)
    mainWindow.setWindowTitle('ISMRMRD Viewer - Jinyuan Zhang')
    mainWindow.resize(1200, 800)
    
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        if os.path.exists(target_file) and os.path.isfile(target_file):
            folder_path = os.path.dirname(target_file)
            mainWindow.set_workspace_path(folder_path)
            mainWindow.load_file_to_tab(target_file)

    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()