# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(834, 600)
        self.action_open_source = QAction(MainWindow)
        self.action_open_source.setObjectName(u"action_open_source")
        self.action_save_target = QAction(MainWindow)
        self.action_save_target.setObjectName(u"action_save_target")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.preview_frame = QFrame(self.centralwidget)
        self.preview_frame.setObjectName(u"preview_frame")
        self.preview_frame.setFrameShape(QFrame.StyledPanel)
        self.preview_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.preview_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.left_spacer = QSpacerItem(2, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.left_spacer, 1, 0, 1, 1)

        self.preview = QGraphicsView(self.preview_frame)
        self.preview.setObjectName(u"preview")
        self.preview.setFocusPolicy(Qt.NoFocus)
        self.preview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.preview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.preview, 1, 1, 1, 1)

        self.top_spacer = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.top_spacer, 0, 1, 1, 1)

        self.right_spacer = QSpacerItem(2, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.right_spacer, 1, 2, 1, 1)

        self.bottom_spacer = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.bottom_spacer, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.preview_frame, 0, 2, 1, 3)

        self.previous = QPushButton(self.centralwidget)
        self.previous.setObjectName(u"previous")

        self.gridLayout.addWidget(self.previous, 0, 0, 1, 1)

        self.aspect = QLineEdit(self.centralwidget)
        self.aspect.setObjectName(u"aspect")

        self.gridLayout.addWidget(self.aspect, 2, 3, 1, 1)

        self.next = QPushButton(self.centralwidget)
        self.next.setObjectName(u"next")

        self.gridLayout.addWidget(self.next, 0, 5, 1, 1)

        self.progress = QProgressBar(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(24)
        self.progress.setTextVisible(False)

        self.gridLayout.addWidget(self.progress, 2, 4, 1, 1)

        self.aspect_label = QLabel(self.centralwidget)
        self.aspect_label.setObjectName(u"aspect_label")
        self.aspect_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.aspect_label, 2, 2, 1, 1)

        self.bar_slider = QSlider(self.centralwidget)
        self.bar_slider.setObjectName(u"bar_slider")
        self.bar_slider.setMaximum(9)
        self.bar_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.bar_slider, 1, 3, 1, 2)

        self.bar_label = QLabel(self.centralwidget)
        self.bar_label.setObjectName(u"bar_label")
        self.bar_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.bar_label, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 834, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.previous, self.preview)
        QWidget.setTabOrder(self.preview, self.next)
        QWidget.setTabOrder(self.next, self.bar_slider)
        QWidget.setTabOrder(self.bar_slider, self.aspect)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open_source)
        self.menuFile.addAction(self.action_save_target)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_open_source.setText(QCoreApplication.translate("MainWindow", u"&Open Source...", None))
#if QT_CONFIG(shortcut)
        self.action_open_source.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_target.setText(QCoreApplication.translate("MainWindow", u"Open Target...", None))
#if QT_CONFIG(shortcut)
        self.action_save_target.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.previous.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.previous.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.aspect.setInputMask("")
        self.aspect.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.next.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.aspect_label.setText(QCoreApplication.translate("MainWindow", u"Aspect:", None))
        self.bar_label.setText(QCoreApplication.translate("MainWindow", u"Bars:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

