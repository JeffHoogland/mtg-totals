# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Sep 25 14:24:01 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(474, 557)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtGui.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.p1Label = QtGui.QLabel(self.frame_2)
        self.p1Label.setObjectName("p1Label")
        self.verticalLayout_7.addWidget(self.p1Label)
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.p1Name = QtGui.QLineEdit(self.frame)
        self.p1Name.setObjectName("p1Name")
        self.verticalLayout_2.addWidget(self.p1Name)
        self.verticalLayout_7.addWidget(self.frame)
        self.frame_4 = QtGui.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.p1Deck = QtGui.QLineEdit(self.frame_4)
        self.p1Deck.setObjectName("p1Deck")
        self.verticalLayout_3.addWidget(self.p1Deck)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.frame_14 = QtGui.QFrame(self.frame_2)
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtGui.QLabel(self.frame_14)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.p1Life = QtGui.QSpinBox(self.frame_14)
        self.p1Life.setMaximum(10000)
        self.p1Life.setProperty("value", 20)
        self.p1Life.setObjectName("p1Life")
        self.verticalLayout_8.addWidget(self.p1Life)
        self.verticalLayout_7.addWidget(self.frame_14)
        self.frame_16 = QtGui.QFrame(self.frame_2)
        self.frame_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtGui.QLabel(self.frame_16)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.p1Infect = QtGui.QSpinBox(self.frame_16)
        self.p1Infect.setMaximum(10000)
        self.p1Infect.setObjectName("p1Infect")
        self.verticalLayout_10.addWidget(self.p1Infect)
        self.verticalLayout_7.addWidget(self.frame_16)
        self.frame_11 = QtGui.QFrame(self.frame_2)
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtGui.QLabel(self.frame_11)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.p1GameWins = QtGui.QSpinBox(self.frame_11)
        self.p1GameWins.setMaximum(1000)
        self.p1GameWins.setObjectName("p1GameWins")
        self.verticalLayout.addWidget(self.p1GameWins)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_5 = QtGui.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.p2Label = QtGui.QLabel(self.frame_5)
        self.p2Label.setObjectName("p2Label")
        self.verticalLayout_9.addWidget(self.p2Label)
        self.frame_6 = QtGui.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtGui.QLabel(self.frame_6)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.p2Name = QtGui.QLineEdit(self.frame_6)
        self.p2Name.setObjectName("p2Name")
        self.verticalLayout_4.addWidget(self.p2Name)
        self.verticalLayout_9.addWidget(self.frame_6)
        self.frame_7 = QtGui.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtGui.QLabel(self.frame_7)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.p2Deck = QtGui.QLineEdit(self.frame_7)
        self.p2Deck.setObjectName("p2Deck")
        self.verticalLayout_5.addWidget(self.p2Deck)
        self.verticalLayout_9.addWidget(self.frame_7)
        self.frame_15 = QtGui.QFrame(self.frame_5)
        self.frame_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_12 = QtGui.QLabel(self.frame_15)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.p2Life = QtGui.QSpinBox(self.frame_15)
        self.p2Life.setMaximum(10000)
        self.p2Life.setProperty("value", 20)
        self.p2Life.setObjectName("p2Life")
        self.verticalLayout_11.addWidget(self.p2Life)
        self.verticalLayout_9.addWidget(self.frame_15)
        self.frame_17 = QtGui.QFrame(self.frame_5)
        self.frame_17.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtGui.QLabel(self.frame_17)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)
        self.p2Infect = QtGui.QSpinBox(self.frame_17)
        self.p2Infect.setMaximum(10000)
        self.p2Infect.setObjectName("p2Infect")
        self.verticalLayout_12.addWidget(self.p2Infect)
        self.verticalLayout_9.addWidget(self.frame_17)
        self.frame_12 = QtGui.QFrame(self.frame_5)
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtGui.QLabel(self.frame_12)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.p2GameWins = QtGui.QSpinBox(self.frame_12)
        self.p2GameWins.setMaximum(1000)
        self.p2GameWins.setObjectName("p2GameWins")
        self.verticalLayout_6.addWidget(self.p2GameWins)
        self.verticalLayout_9.addWidget(self.frame_12)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout_13.addWidget(self.frame_3)
        self.frame_8 = QtGui.QFrame(self.centralwidget)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resetLifeButton = QtGui.QPushButton(self.frame_8)
        self.resetLifeButton.setObjectName("resetLifeButton")
        self.horizontalLayout_2.addWidget(self.resetLifeButton)
        self.swapPlayersButton = QtGui.QPushButton(self.frame_8)
        self.swapPlayersButton.setObjectName("swapPlayersButton")
        self.horizontalLayout_2.addWidget(self.swapPlayersButton)
        self.verticalLayout_13.addWidget(self.frame_8)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Meadery MTG Stream Dashboard", None, QtGui.QApplication.UnicodeUTF8))
        self.p1Label.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Player One</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Name</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Deck Name</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Life Total</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Infect Counter</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Game Wins</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.p2Label.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Player Two</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Name</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Deck Name</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Life Total</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Infect Counter</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("mainWindow", "<html><head/><body><p align=\"center\">Game Wins</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.resetLifeButton.setText(QtGui.QApplication.translate("mainWindow", "Reset Life", None, QtGui.QApplication.UnicodeUTF8))
        self.swapPlayersButton.setText(QtGui.QApplication.translate("mainWindow", "Swap Players", None, QtGui.QApplication.UnicodeUTF8))

