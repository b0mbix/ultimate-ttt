# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oneboard.ui'
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
        MainWindow.resize(619, 695)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(80, 10, 451, 81))
        font = QFont()
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.square_02 = QPushButton(self.centralwidget)
        self.squares = QButtonGroup(MainWindow)
        self.squares.setObjectName(u"squares")
        self.squares.addButton(self.square_02)
        self.square_02.setObjectName(u"square_02")
        self.square_02.setGeometry(QRect(80, 400, 151, 151))
        font1 = QFont()
        font1.setPointSize(72)
        self.square_02.setFont(font1)
        self.square_12 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_12)
        self.square_12.setObjectName(u"square_12")
        self.square_12.setGeometry(QRect(230, 400, 151, 151))
        self.square_12.setFont(font1)
        self.square_22 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_22)
        self.square_22.setObjectName(u"square_22")
        self.square_22.setGeometry(QRect(380, 400, 151, 151))
        self.square_22.setFont(font1)
        self.square_21 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_21)
        self.square_21.setObjectName(u"square_21")
        self.square_21.setGeometry(QRect(380, 250, 151, 151))
        self.square_21.setFont(font1)
        self.square_11 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_11)
        self.square_11.setObjectName(u"square_11")
        self.square_11.setGeometry(QRect(230, 250, 151, 151))
        self.square_11.setFont(font1)
        self.square_01 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_01)
        self.square_01.setObjectName(u"square_01")
        self.square_01.setGeometry(QRect(80, 250, 151, 151))
        self.square_01.setFont(font1)
        self.square_20 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_20)
        self.square_20.setObjectName(u"square_20")
        self.square_20.setGeometry(QRect(380, 100, 151, 151))
        self.square_20.setFont(font1)
        self.square_10 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_10)
        self.square_10.setObjectName(u"square_10")
        self.square_10.setGeometry(QRect(230, 100, 151, 151))
        self.square_10.setFont(font1)
        self.square_00 = QPushButton(self.centralwidget)
        self.squares.addButton(self.square_00)
        self.square_00.setObjectName(u"square_00")
        self.square_00.setGeometry(QRect(80, 100, 151, 151))
        self.square_00.setFont(font1)
        self.move_label = QLabel(self.centralwidget)
        self.move_label.setObjectName(u"move_label")
        self.move_label.setGeometry(QRect(84, 569, 451, 61))
        font2 = QFont()
        font2.setPointSize(36)
        self.move_label.setFont(font2)
        self.move_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 619, 30))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tic-Tac-Toe", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Tic-Tac-Toe", None))
        self.square_02.setText("")
        self.square_12.setText("")
        self.square_22.setText("")
        self.square_21.setText("")
        self.square_11.setText("")
        self.square_01.setText("")
        self.square_20.setText("")
        self.square_10.setText("")
        self.square_00.setText("")
        self.move_label.setText(QCoreApplication.translate("MainWindow", u"Move: X", None))
    # retranslateUi

