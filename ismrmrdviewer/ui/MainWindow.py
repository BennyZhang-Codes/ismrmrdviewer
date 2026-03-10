import os
import logging
from PySide6 import QtCore, QtWidgets

from ui.ui_mainwindow import Ui_MainWindow
from .FileWidget import FileWidget

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("ISMRMRD Data Viewer")
        self.opened_files = {}

        self.MAX_TAB_LENGTH = 12

        # --- 1. File System Model Configuration ---
        self.file_model = QtWidgets.QFileSystemModel()
        
        # Explicitly set the filter to show all files and directories 
        # (excluding the hidden "." and ".." navigation items)
        self.file_model.setFilter(QtCore.QDir.AllEntries | QtCore.QDir.NoDotAndDotDot)
        
        default_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DesktopLocation)
        self.file_model.setRootPath(default_path)

        self.ui.fileTreeView.setModel(self.file_model)
        
        for i in range(1, 4):
            self.ui.fileTreeView.setColumnHidden(i, True)
        self.ui.fileTreeView.setHeaderHidden(True)

        # --- 2. UI Initialization ---
        self.ui.tabViewers.clear()
        self.default_label = QtWidgets.QLabel("👈 Please select a .h5 or .mrd file from the left panel")
        self.default_label.setAlignment(QtCore.Qt.AlignCenter)
        
        welcome_index = self.ui.tabViewers.addTab(self.default_label, "Welcome")
        self.ui.tabViewers.setTabToolTip(welcome_index, "Welcome")
        self.ui.tabViewers.tabBar().hide()

        # --- 3. Signal Connections ---
        self.ui.fileTreeView.clicked.connect(self.on_file_clicked)
        self.ui.fileTreeView.doubleClicked.connect(self.on_tree_double_clicked)
        
        if hasattr(self.ui, 'actionOpen_Folder'):
            self.ui.actionOpen_Folder.triggered.connect(self.open_workspace_dialog)
        
        if hasattr(self.ui, 'actionOpen_File'):
            self.ui.actionOpen_File.triggered.connect(self.open_file_dialog)
            
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionInfo.triggered.connect(self.show_info_dialog)
        self.ui.tabViewers.tabCloseRequested.connect(self.close_tab)

        self.ui.tabViewers.currentChanged.connect(self.on_tab_changed)

        # [UPDATED] Connect the renamed File Explorer menu action
        if hasattr(self.ui, 'actionFile_Explorer'):
            self.ui.actionFile_Explorer.triggered.connect(self.toggle_file_dock)

        if hasattr(self.ui, 'btnOpenFolder'):
            self.ui.btnOpenFolder.clicked.connect(self.open_workspace_dialog)
        if hasattr(self.ui, 'btnUpFolder'):
            self.ui.btnUpFolder.clicked.connect(self.navigate_up_folder)
        if hasattr(self.ui, 'pathLineEdit'):
            self.ui.pathLineEdit.returnPressed.connect(self.on_path_entered)

        self.set_workspace_path(default_path)

    def set_workspace_path(self, folder_path):
        self.file_model.setRootPath(folder_path) 
        index = self.file_model.index(folder_path)
        self.ui.fileTreeView.setRootIndex(index)
        
        if hasattr(self.ui, 'pathLineEdit'):
            display_path = folder_path if folder_path else "My Computer"
            self.ui.pathLineEdit.setText(display_path)

    @QtCore.Slot()
    def open_file_dialog(self):
        current_path = self.file_model.filePath(self.ui.fileTreeView.rootIndex())
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open ISMRMRD Data File",
            current_path,
            "ISMRMRD Data Files (*.h5 *.mrd);;All Files (*)"
        )

        if file_path:
            folder_path = os.path.dirname(file_path)
            self.set_workspace_path(folder_path)
            self.load_file_to_tab(file_path)

    def load_file_to_tab(self, file_path):
        # Ignore files that are not .h5 or .mrd
        if not file_path.endswith(('.h5', '.mrd')):
            return

        logging.info(f"Opening file: {file_path}")
        self.ui.tabViewers.tabBar().show()

        if file_path in self.opened_files:
            widget = self.opened_files[file_path]
            self.ui.tabViewers.setCurrentWidget(widget)
            self.ui.statusbar.showMessage(f"Switched to: {os.path.basename(file_path)}")
            return

        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            file_widget = FileWidget(self, file_path)
            file_name = os.path.basename(file_path)
            
            tab_index = self.ui.tabViewers.addTab(file_widget, file_name)
            self.ui.tabViewers.setTabToolTip(tab_index, file_name)
            
            self.opened_files[file_path] = file_widget
            self.ui.tabViewers.setCurrentWidget(file_widget)
            
            self.ui.statusbar.showMessage(f"Successfully loaded: {file_name}")
        except Exception as e:
            logging.error(f"Failed to open file {file_path}: {str(e)}")
            QtWidgets.QMessageBox.warning(self, "Load Failed", f"Cannot parse the file:\n{e}")
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    @QtCore.Slot(QtCore.QModelIndex)
    def on_file_clicked(self, index):
        if self.file_model.isDir(index):
            return 
            
        file_path = self.file_model.filePath(index)
        self.load_file_to_tab(file_path)

    @QtCore.Slot(int)
    def on_tab_changed(self, index):
        if index < 0:
            return
            
        for i in range(self.ui.tabViewers.count()):
            full_name = self.ui.tabViewers.tabToolTip(i)
            if not full_name:
                continue
                
            if i == index:
                self.ui.tabViewers.setTabText(i, full_name)
            else:
                if len(full_name) > self.MAX_TAB_LENGTH:
                    short_name = full_name[:self.MAX_TAB_LENGTH] + "..."
                    self.ui.tabViewers.setTabText(i, short_name)
                else:
                    self.ui.tabViewers.setTabText(i, full_name)

    @QtCore.Slot()
    def toggle_file_dock(self):
        if hasattr(self.ui, 'fileDockWidget'):
            is_visible = self.ui.fileDockWidget.isVisible()
            self.ui.fileDockWidget.setVisible(not is_visible)
            if not is_visible:
                self.ui.fileDockWidget.raise_()

    @QtCore.Slot(QtCore.QModelIndex)
    def on_tree_double_clicked(self, index):
        if self.file_model.isDir(index):
            folder_path = self.file_model.filePath(index)
            self.set_workspace_path(folder_path)

    @QtCore.Slot()
    def open_workspace_dialog(self):
        current_path = self.file_model.filePath(self.ui.fileTreeView.rootIndex())
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Data Workspace", current_path
        )
        if folder:
            self.set_workspace_path(folder)
            self.ui.statusbar.showMessage(f"Workspace changed to: {folder}")

    @QtCore.Slot()
    def navigate_up_folder(self):
        current_index = self.ui.fileTreeView.rootIndex()
        parent_index = self.file_model.parent(current_index)
        
        if parent_index.isValid():
            parent_path = self.file_model.filePath(parent_index)
            self.set_workspace_path(parent_path)

    @QtCore.Slot()
    def on_path_entered(self):
        path = self.ui.pathLineEdit.text()
        if os.path.exists(path) and os.path.isdir(path):
            self.set_workspace_path(path)
        else:
            QtWidgets.QMessageBox.warning(self, "Invalid Path", "The specified path does not exist.")
            current_path = self.file_model.filePath(self.ui.fileTreeView.rootIndex())
            self.ui.pathLineEdit.setText(current_path)

    @QtCore.Slot()
    def show_info_dialog(self):
        QtWidgets.QMessageBox.information(
            self, 
            "About ISMRMRD Viewer", 
            "ISMRMRD Data Viewer\n\nA powerful tool for efficient MRI data inspection.\n\nDeveloped by Jinyuan Zhang"
        )

    @QtCore.Slot(int)
    def close_tab(self, index):
        widget = self.ui.tabViewers.widget(index)
        if widget == self.default_label:
            return
        for path, cached_widget in list(self.opened_files.items()):
            if cached_widget == widget:
                del self.opened_files[path]
                break
        self.ui.tabViewers.removeTab(index)
        widget.deleteLater()
        if self.ui.tabViewers.count() == 1:
            self.ui.tabViewers.setCurrentWidget(self.default_label)
            self.ui.tabViewers.tabBar().hide()