theirName = "Mat Bimonte"

myLifeFile = "/media/jeff/Storage/CrashTest/DataTextFiles/MyLife.txt"
theirLifeFile = "/media/jeff/Storage/CrashTest/DataTextFiles/TheirLife.txt"

import efl.elementary as elm
from efl.elementary.window import StandardWindow, Window, ELM_WIN_DIALOG_BASIC
from efl.elementary.background import Background
from efl.elementary.entry import Entry
from efl.elementary.box import Box
from efl.elementary.button import Button

from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL, \
    EVAS_CALLBACK_KEY_UP, EVAS_EVENT_FLAG_ON_HOLD
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL
FILL_HORIZ = EVAS_HINT_FILL, 0.5

class MainWindow(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, "lifetracker", "Life Tracker", size=(200, 200))
        self.callback_delete_request_add(lambda o: elm.exit())
        self.elm_event_callback_add(self.eventsCb)

        self.buildSubs()
        self.resetLifeTotals()
    
    def buildSubs(self):
        self.subWin = Window("lifetracker", ELM_WIN_DIALOG_BASIC, self, size=(300, 300))
        self.subWin.title = "Life Tracker Assignment"
        bg = Background(self.subWin, size_hint_weight=EXPAND_BOTH)
        bg.show()
        self.subWin.resize_object_add(bg)
        self.subWin.callback_delete_request_add(lambda o: elm.exit())
        self.ourWin = Window("lifetracker", ELM_WIN_DIALOG_BASIC, self, size=(300, 300))
        self.ourWin.title = "Life Tracker Key Strokes"
        bg = Background(self.ourWin, size_hint_weight=EXPAND_BOTH)
        bg.show()
        self.ourWin.resize_object_add(bg)
        self.ourWin.callback_delete_request_add(lambda o: elm.exit())
        self.ourWin.elm_event_callback_add(self.eventsCb)
        
        self.ourLife = ourLabel = Entry(self.ourWin, editable=False)
        ourLabel.size_hint_weight = EXPAND_BOTH
        ourLabel.size_hint_align = FILL_BOTH
        ourLabel.text_style_user_push("DEFAULT='font_size=20'")
        ourLabel.text = "Up and Down for Their Life, Left and Right for Mine"
        ourLabel.show()
        
        self.ourEntry = ourEntry = Entry(self.subWin)
        ourEntry.size_hint_weight = EXPAND_HORIZ
        ourEntry.size_hint_align = (-1, 0)
        ourEntry.single_line_set(True)
        ourEntry.text_style_user_push("DEFAULT='font_size=50'")
        ourEntry.callback_activated_add(self.ourLifeUpdate)
        ourEntry.text = "20"
        ourEntry.show()
        
        self.theirEntry = theirEntry = Entry(self.subWin)
        theirEntry.size_hint_weight = EXPAND_HORIZ
        theirEntry.size_hint_align = (-1, 0)
        theirEntry.single_line_set(True)
        theirEntry.text_style_user_push("DEFAULT='font_size=50'")
        theirEntry.callback_activated_add(self.theirLifeUpdate)
        theirEntry.text = "20"
        theirEntry.show()
        
        resetBtn = Button(self.subWin)
        resetBtn.text = "Reset life totals"
        resetBtn.callback_pressed_add(self.resetLifeTotals)
        resetBtn.show()
        
        entryBox = Box(self.subWin)
        entryBox.size_hint_weight = EXPAND_HORIZ
        entryBox.pack_end(ourEntry)
        entryBox.pack_end(theirEntry)
        entryBox.pack_end(resetBtn)
        entryBox.show()
        
        self.ourWin.resize_object_add(ourLabel)
        self.subWin.resize_object_add(entryBox)
        
        self.ourWin.show()
        self.subWin.show()
        
        self.ourWin.center(True, True)
        self.subWin.center(True, True)
    
    def resetLifeTotals(self, obj=None):
        self.ourLifeTotal = 20
        self.ourEntry.text = str(self.ourLifeTotal)
        self.updateLifeText("mine")
        self.theirLifeTotal = 20
        self.theirEntry.text = str(self.theirLifeTotal)
        self.updateLifeText("theirs")
    
    def ourLifeUpdate(self, obj):
        self.ourLifeTotal = int(obj.text)
        self.updateLifeText("mine")
    
    def theirLifeUpdate(self, obj):
        self.theirLifeTotal = int(obj.text)
        self.updateLifeText("theirs")
    
    def updateLifeText(self, who):
        if who == "mine":
            lifeText = str(self.ourLifeTotal)
            while len(lifeText) < 3:
                lifeText = " %s"%lifeText
            with open(myLifeFile, 'w') as myfile: #file is a builtin, don't name your file 'file'
                myfile.write(lifeText)
        else:
            lifeText = str(self.theirLifeTotal)
            while len(lifeText) < 3:
                lifeText = " %s"%lifeText
            with open(theirLifeFile,'w') as myfile: #file is a builtin, don't name your file 'file'
                myfile.write(lifeText)
    
    def lifeChange(self, who, direction):
        if direction == "up":
            change = 1
        else:
            change = -1
        
        if who == "mine":
            self.ourLifeTotal += change
            self.ourEntry.text = str(self.ourLifeTotal)
            self.updateLifeText("mine")
        else:
            self.theirLifeTotal += change
            self.theirEntry.text = str(self.theirLifeTotal)
            self.updateLifeText("theirs")
    
    def eventsCb(self, obj, src, event_type, event):
        #print(obj)
        #print(src)
        #print(event.key.lower())
        #print(event_type)
        #print("")

        if not event_type == EVAS_CALLBACK_KEY_UP:
            return False

        if event.keyname == "Up":
            self.lifeChange("mine", "up")
        elif event.keyname == "Down":
            self.lifeChange("mine", "down")
        elif event.keyname == "Right":
            self.lifeChange("thiers", "up")
        elif event.keyname == "Left":
            self.lifeChange("theirs", "down")
            

        event.event_flags = event.event_flags | EVAS_EVENT_FLAG_ON_HOLD
        return True

if __name__ == "__main__":
    elm.init()
    GUI = MainWindow()
    #GUI.show()
    elm.run()
    elm.shutdown()
