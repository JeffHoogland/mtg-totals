# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lifeWindow.ui'
#
# Created: Fri Sep 18 12:36:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_lifeWindow(object):
    def setupUi(self, lifeWindow):
        lifeWindow.setObjectName("lifeWindow")
        lifeWindow.resize(400, 250)
        self.verticalLayout = QtGui.QVBoxLayout(lifeWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtGui.QTextEdit(lifeWindow)
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(lifeWindow)
        QtCore.QMetaObject.connectSlotsByName(lifeWindow)

    def retranslateUi(self, lifeWindow):
        lifeWindow.setWindowTitle(QtGui.QApplication.translate("lifeWindow", "Fast Life Changer", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("lifeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">While you are focused on this window </span><span style=\" font-size:14pt; font-weight:600;\">arrow up</span><span style=\" font-size:14pt;\"> and </span><span style=\" font-size:14pt; font-weight:600;\">arrow down</span><span style=\" font-size:14pt;\"> will adjust player one\'s life total and </span><span style=\" font-size:14pt; font-weight:600;\">arrow right</span><span style=\" font-size:14pt;\"> and </span><span style=\" font-size:14pt; font-weight:600;\">arrow left</span><span style=\" font-size:14pt;\"> will adjust player two\'s life total.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

