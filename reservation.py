"""
RESERVATION SYSTEM by Inkar Mizambek

Pictures are from https://www.flaticon.com
"""

from check_in import Check_in
from check_out import Check_out
from rooms import Rooms
from guests import Guests
from calendar_view import Calendar_View
from settings import Settings
from services import Services
from label_generator import Label_Generator

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton

class Reservation_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HOME PAGE")
        self.setStyleSheet("background-color: #B3CDE3")
        
        Label_Generator("RESERVATION SYSTEM", 25, "#FFFFFF; border: 2px solid black", 
                        [175, 50, 350, 50], self).text_central()
        
        """ 
        description for each button:
            - Button name
            - Picture in a png format
            - Arguments for setGeometry function
            - Connect the button to dialog window
        """
        
        buttons = [ (" CHECK IN", 'pictures/check_in.png', 50, 150, 175, 100, self.check_in_window),
                   (" CHECK OUT", 'pictures/check_out.png', 50, 300, 175, 100, self.check_out_window),
                   (" ROOMS", 'pictures/rooms.png', 275, 150, 175, 100, self.rooms_window),
                   (" GUESTS", 'pictures/guests.png', 275, 300, 175, 100, self.guests_window),
                   ("", 'pictures/settings.png', 650, 10, 40, 40, self.settings_window),
                   ("", 'pictures/calendar.png', 500, 150, 150, 100, self.calendar_view),
                   (" SERVICES", 'pictures/services.png', 500, 300, 150, 100, self.add_services)]
        
        # placing the buttons on "HOME PAGE"
        i = 0
        for desc in buttons:
            button = QPushButton(desc[0], self)
            button.setStyleSheet('background-color: #A3C1DA; color: black;')
            button.setFont(QtGui.QFont('Times', 15))
            button.setIcon(QtGui.QIcon(desc[1]))
            button.setGeometry(desc[2], desc[3], desc[4], desc[5])
            
            if i == 4: 
                button.setIconSize(QtCore.QSize(30, 30))
            elif i == 6:
                button.setIconSize(QtCore.QSize(50, 50))
            else: 
                button.setIconSize(QtCore.QSize(65, 65))
            
            button.clicked.connect(desc[6])
            
            i = i + 1
        
    """ CHECK IN """
    def check_in_window(self):
        dialog = Check_in(self)
        dialog.exec_()
    
    """ CHECK OUT """
    def check_out_window(self):
        dialog = Check_out(self)
        dialog.exec_()
    
    """ ROOMS """
    def rooms_window(self):
        dialog = Rooms(self)
        dialog.exec_()
    
    """ GUESTS """
    def guests_window(self):
        dialog = Guests()
        dialog.exec_()
    
    """  SETTING """
    def settings_window(self):
        dialog = Settings(self)
        dialog.exec_()
    
    """ CALENDAR """
    def calendar_view(self):
        dialog = Calendar_View()
        dialog.exec_()
    
    """ CALENDAR """
    def add_services(self):
        dialog = Services(self)
        dialog.exec_()