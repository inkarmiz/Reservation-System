from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5 import QtGui, QtCore
from user import User
from label_generator import Label_Generator

class Settings(QDialog):
    def __init__(self, parent = None):
        super(Settings, self).__init__(parent)
        self.setGeometry(450, 300, 400, 300)
        self.setWindowTitle("SETTINGS")
        
        Label_Generator("", 0, "#FFFFFF; border: 2px solid black", [25, 25, 350, 250], self).text_on_window()
        
        buttons = [ (" ADD USER", 'pictures/add_user.png', 50, 50, self.add_user),
                   (" REMOVE USER", 'pictures/remove_user.png', 50, 125, self.remove_user),
                   (" SHOW USER LIST", 'pictures/user_list.png', 50, 200, self.show_list)]
        
        # placing the buttons on "SETTINGS"
        for desc in buttons:
            button = QPushButton(desc[0], self)
            button.setStyleSheet('QPushButton {background-color: #B3CDE3; color: black;}')
            button.setFont(QtGui.QFont('Times', 15))
            button.setIcon(QtGui.QIcon(desc[1]))
            button.setIconSize(QtCore.QSize(30, 30))
            button.setGeometry(desc[2], desc[3], 300, 50)
            button.clicked.connect(desc[4])
    
    def add_user(self):
        dialog = User("ADD USER")
        dialog.user_input()
        dialog.add_button()
        dialog.exec_()
    
    def remove_user(self):
        dialog = User("REMOVE USER")
        dialog.user_input()
        dialog.remove_button()
        dialog.exec_()
    
    def show_list(self):
        dialog = User("SHOW USER LIST")
        dialog.show_list_executer()
        dialog.exec_()
            
        
        