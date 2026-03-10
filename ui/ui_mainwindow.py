# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        icon = QIcon(QIcon.fromTheme(u"folder-open"))
        self.actionOpen_Folder.setIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon(QIcon.fromTheme(u"system-shutdown"))
        self.actionExit.setIcon(icon1)
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        icon2 = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionInfo.setIcon(icon2)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        icon3 = QIcon(QIcon.fromTheme(u"document-open"))
        self.actionOpen_File.setIcon(icon3)
        self.actionFile_Explorer = QAction(MainWindow)
        self.actionFile_Explorer.setObjectName(u"actionFile_Explorer")
        icon4 = QIcon(QIcon.fromTheme(u"system-file-manager"))
        self.actionFile_Explorer.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabViewers = QTabWidget(self.centralwidget)
        self.tabViewers.setObjectName(u"tabViewers")
        self.tabViewers.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabViewers.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabViewers.setDocumentMode(False)
        self.tabViewers.setTabsClosable(True)
        self.tabViewers.setMovable(True)
        self.tabViewers.setTabBarAutoHide(False)
        self.stackedViewersPage1 = QWidget()
        self.stackedViewersPage1.setObjectName(u"stackedViewersPage1")
        self.tabViewers.addTab(self.stackedViewersPage1, "")
        self.stackedViewersPage2 = QWidget()
        self.stackedViewersPage2.setObjectName(u"stackedViewersPage2")
        self.tabViewers.addTab(self.stackedViewersPage2, "")

        self.verticalLayout_2.addWidget(self.tabViewers)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setSeparatorsCollapsible(False)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileDockWidget = QDockWidget(MainWindow)
        self.fileDockWidget.setObjectName(u"fileDockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnUpFolder = QPushButton(self.dockWidgetContents)
        self.btnUpFolder.setObjectName(u"btnUpFolder")
        icon5 = QIcon(QIcon.fromTheme(u"go-up"))
        self.btnUpFolder.setIcon(icon5)

        self.horizontalLayout.addWidget(self.btnUpFolder)

        self.pathLineEdit = QLineEdit(self.dockWidgetContents)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.pathLineEdit)

        self.btnOpenFolder = QPushButton(self.dockWidgetContents)
        self.btnOpenFolder.setObjectName(u"btnOpenFolder")
        self.btnOpenFolder.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnOpenFolder)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.fileTreeView = QTreeView(self.dockWidgetContents)
        self.fileTreeView.setObjectName(u"fileTreeView")
        self.fileTreeView.header().setProperty(u"showSortIndicator", False)

        self.verticalLayout.addWidget(self.fileTreeView)

        self.fileDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.fileDockWidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFile_Explorer)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInfo)

        self.retranslateUi(MainWindow)

        self.tabViewers.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.actionOpen_Folder.setIconText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_Folder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionFile_Explorer.setText(QCoreApplication.translate("MainWindow", u"File Explorer", None))
        self.tabViewers.setTabText(self.tabViewers.indexOf(self.stackedViewersPage1), "")
        self.tabViewers.setTabText(self.tabViewers.indexOf(self.stackedViewersPage2), "")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.fileDockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"File Explorer", None))
#if QT_CONFIG(tooltip)
        self.btnUpFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Go Up", None))
#endif // QT_CONFIG(tooltip)
        self.btnUpFolder.setText("")
#if QT_CONFIG(tooltip)
        self.btnOpenFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#endif // QT_CONFIG(tooltip)
        self.btnOpenFolder.setText("")
    # retranslateUi

