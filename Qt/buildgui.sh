#!/bin/bash
rm ui_*.py
rm ui_*.pyc
pyside-uic mainWindow.ui > ui_mainWindow.py
pyside-uic settingsWindow.ui > ui_settingsWindow.py
pyside-uic lifeWindow.ui > ui_lifeWindow.py
