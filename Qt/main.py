"""
A tool for quickly and easily updating information on live MTG Streams

By: Jeff Hoogland
"""

import sys, os
from PySide.QtGui import *
from PySide.QtCore import *
from ui_mainWindow import Ui_mainWindow

##Dialog windows broken out into seperate files to manage things easier
from lifeWindow import lifeWindow

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        if not os.path.isdir("DataFiles"):
            os.makedirs("DataFiles")
        
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL("timeout()"), self.update)
        self.timer.start(1500)
        
        self.lifeWindow = lifeWindow( self )
        self.lifeWindow.show()
        
        self.show()
    
    def update(self):
        #print("Tick")
        self.writeToFile("DataFiles/p1Name.txt", self.p1Name.displayText())
        self.writeToFile("DataFiles/p1Deck.txt", self.p1Deck.displayText())
        self.writeToFile("DataFiles/p1Life.txt", self.p1Life.cleanText())
        self.writeToFile("DataFiles/p1Infect.txt", self.p1Infect.cleanText())
        self.writeToFile("DataFiles/p1GameWins.txt", self.p1GameWins.cleanText())
        
        self.writeToFile("DataFiles/p2Name.txt", self.p2Name.displayText())
        self.writeToFile("DataFiles/p2Deck.txt", self.p2Deck.displayText())
        self.writeToFile("DataFiles/p2Life.txt", self.p2Life.cleanText())
        self.writeToFile("DataFiles/p2Infect.txt", self.p2Infect.cleanText())
        self.writeToFile("DataFiles/p2GameWins.txt", self.p2GameWins.cleanText())
    
    def writeToFile(self, targetFile, writeText):
        if writeText:
            with open(targetFile, 'w') as myfile: #file is a builtin, don't name your file 'file'
                myfile.write(writeText)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
