# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oneboard_dynamic.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 679)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.square_10 = QPushButton(self.centralwidget)
        self.squares = QButtonGroup(MainWindow)
        self.squares.setObjectName(u"squares")
        self.squares.addButton(self.square_10)
        self.square_10.setObjectName(u"square_10")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.square_10.sizePolicy().hasHeightForWidth())
        self.square_10.setSizePolicy(sizePolicy)
        self.square_10.setMinimumSize(QSize(100, 100))
        self.square_10.setMaximumSize(QSize(500, 500))
        font = QFont()
        font.setPointSize(72)
        self.square_10.setFont(font)

        self.gridLayout.addWidget(self.square_10, 2, 0, 1, 1)

        self.square_01 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_01)
        self.square_01.setObjectName(u"square_01")
        sizePolicy.setHeightForWidth(self.square_01.sizePolicy().hasHeightForWidth())
        self.square_01.setSizePolicy(sizePolicy)
        self.square_01.setMinimumSize(QSize(100, 100))
        self.square_01.setMaximumSize(QSize(500, 500))
        self.square_01.setFont(font)

        self.gridLayout.addWidget(self.square_01, 1, 1, 1, 1)

        self.square_20 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_20)
        self.square_20.setObjectName(u"square_20")
        sizePolicy.setHeightForWidth(self.square_20.sizePolicy().hasHeightForWidth())
        self.square_20.setSizePolicy(sizePolicy)
        self.square_20.setMinimumSize(QSize(100, 100))
        self.square_20.setMaximumSize(QSize(500, 500))
        self.square_20.setFont(font)

        self.gridLayout.addWidget(self.square_20, 3, 0, 1, 1)

        self.square_12 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_12)
        self.square_12.setObjectName(u"square_12")
        sizePolicy.setHeightForWidth(self.square_12.sizePolicy().hasHeightForWidth())
        self.square_12.setSizePolicy(sizePolicy)
        self.square_12.setMinimumSize(QSize(100, 100))
        self.square_12.setMaximumSize(QSize(500, 500))
        self.square_12.setFont(font)

        self.gridLayout.addWidget(self.square_12, 2, 2, 1, 1)

        self.move_label = QLabel(self.centralwidget)
        self.move_label.setObjectName(u"move_label")
        self.move_label.setMaximumSize(QSize(16777215, 70))
        font1 = QFont()
        font1.setPointSize(36)
        self.move_label.setFont(font1)
        self.move_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.move_label, 4, 0, 1, 3)

        self.square_00 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_00)
        self.square_00.setObjectName(u"square_00")
        sizePolicy.setHeightForWidth(self.square_00.sizePolicy().hasHeightForWidth())
        self.square_00.setSizePolicy(sizePolicy)
        self.square_00.setMinimumSize(QSize(100, 100))
        self.square_00.setMaximumSize(QSize(500, 500))
        self.square_00.setFont(font)

        self.gridLayout.addWidget(self.square_00, 1, 0, 1, 1)

        self.square_21 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_21)
        self.square_21.setObjectName(u"square_21")
        sizePolicy.setHeightForWidth(self.square_21.sizePolicy().hasHeightForWidth())
        self.square_21.setSizePolicy(sizePolicy)
        self.square_21.setMinimumSize(QSize(100, 100))
        self.square_21.setMaximumSize(QSize(500, 500))
        self.square_21.setFont(font)

        self.gridLayout.addWidget(self.square_21, 3, 1, 1, 1)

        self.square_11 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_11)
        self.square_11.setObjectName(u"square_11")
        sizePolicy.setHeightForWidth(self.square_11.sizePolicy().hasHeightForWidth())
        self.square_11.setSizePolicy(sizePolicy)
        self.square_11.setMinimumSize(QSize(100, 100))
        self.square_11.setMaximumSize(QSize(500, 500))
        self.square_11.setFont(font)

        self.gridLayout.addWidget(self.square_11, 2, 1, 1, 1)

        self.square_02 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_02)
        self.square_02.setObjectName(u"square_02")
        sizePolicy.setHeightForWidth(self.square_02.sizePolicy().hasHeightForWidth())
        self.square_02.setSizePolicy(sizePolicy)
        self.square_02.setMinimumSize(QSize(100, 100))
        self.square_02.setMaximumSize(QSize(500, 500))
        self.square_02.setFont(font)

        self.gridLayout.addWidget(self.square_02, 1, 2, 1, 1)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 70))
        font2 = QFont()
        font2.setPointSize(48)
        self.title.setFont(font2)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 3)

        self.square_22 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_22)
        self.square_22.setObjectName(u"square_22")
        sizePolicy.setHeightForWidth(self.square_22.sizePolicy().hasHeightForWidth())
        self.square_22.setSizePolicy(sizePolicy)
        self.square_22.setMinimumSize(QSize(100, 100))
        self.square_22.setMaximumSize(QSize(500, 500))
        self.square_22.setFont(font)

        self.gridLayout.addWidget(self.square_22, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 474, 30))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tic-Tac-Toe", None))
        self.square_10.setText("")
        self.square_01.setText("")
        self.square_20.setText("")
        self.square_12.setText("")
        self.move_label.setText(QCoreApplication.translate("MainWindow", u"Move: X", None))
        self.square_00.setText("")
        self.square_21.setText("")
        self.square_11.setText("")
        self.square_02.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Tic-Tac-Toe", None))
        self.square_22.setText("")
    # retranslateUi

