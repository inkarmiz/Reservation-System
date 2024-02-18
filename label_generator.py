from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel

class Label_Generator:
    def __init__(self, text, font_size, bg_color, geometry, window):
        super().__init__()
        self.text = text
        self.font_size = font_size
        self.bg_color = bg_color
        self.geometry = geometry
        self.window = window
        
    def text_on_window(self):
        text = QLabel(self.text, self.window)
        text.setFont(QtGui.QFont('Times', self.font_size, QtGui.QFont.Bold))
        text.setStyleSheet("background-color: " + self.bg_color)
        text.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
    
    def text_central(self):
        text = QLabel(self.text, self.window)
        text.setFont(QtGui.QFont('Times', self.font_size, QtGui.QFont.Bold))
        text.setStyleSheet("background-color: " + self.bg_color)
        text.setGeometry(self.geometry[0], self.geometry[1], self.geometry[2], self.geometry[3])
        text.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
    