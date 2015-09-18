import os

from PySide.QtGui import *
from PySide.QtCore import *

from ui_lifeWindow import Ui_lifeWindow

class lifeWindow(QDialog, Ui_lifeWindow):
    def __init__(self, parent ):
        super(lifeWindow, self).__init__(parent)
        self.rent = parent
        
        self.setupUi(self)
        self.assignKeys()

    def keyUpPressed( self ):
        #print("Up")
        self.rent.p1Life.setValue(int(self.rent.p1Life.cleanText())+1)
        
    def keyDownPressed( self ):
        #print("Down")
        self.rent.p1Life.setValue(int(self.rent.p1Life.cleanText())-1)
    
    def keyRightPressed( self ):
        #print("Right")
        self.rent.p2Life.setValue(int(self.rent.p2Life.cleanText())+1)
        
    def keyLeftPressed( self ):
        #print("Left")
        self.rent.p2Life.setValue(int(self.rent.p2Life.cleanText())-1)

    def assignKeys( self ):
        self.keyUp = QShortcut(QKeySequence(Qt.Key_Up), self)
        self.keyUp.setContext(Qt.ApplicationShortcut)
        self.keyUp.activated.connect(self.keyUpPressed)
        
        self.keyDown = QShortcut(QKeySequence(Qt.Key_Down), self)
        self.keyDown.setContext(Qt.ApplicationShortcut)
        self.keyDown.activated.connect(self.keyDownPressed)
        
        self.keyRight = QShortcut(QKeySequence(Qt.Key_Right), self)
        self.keyRight.setContext(Qt.ApplicationShortcut)
        self.keyRight.activated.connect(self.keyRightPressed)
        
        self.keyLeft = QShortcut(QKeySequence(Qt.Key_Left), self)
        self.keyLeft.setContext(Qt.ApplicationShortcut)
        self.keyLeft.activated.connect(self.keyLeftPressed)
