from PyQt5.QtGui import QFontDatabase
import os

def load_fonts():
    for font in os.listdir("fonts"):
        QFontDatabase.addApplicationFont(os.path.join("fonts", font))

def load_stylesheet(filename="style.qss"):
    with open(filename) as file:
        return file.read()

def set_stylesheet(app):
    load_fonts()
    app.setStyleSheet(load_stylesheet("style.qss"))
