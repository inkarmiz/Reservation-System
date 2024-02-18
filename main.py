"""
RESERVATION SYSTEM by Inkar Mizambek

Pictures are from https://www.flaticon.com
"""

from reservation import Reservation_Window
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox
from PyQt5 import QtGui
from label_generator import Label_Generator

class Log_In_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log_in_window()

    def log_in_window(self):
        self.setWindowTitle('LOG IN')
        self.setStyleSheet("background-color: #B3CDE3")
        self.setGeometry(400, 300, 400, 300)
        
        # generating labels on the window
        Label_Generator("Enter Username", 15, "#B3CDE3", [50, 65, 300, 50], self).text_on_window()
        Label_Generator("Enter Password", 15, "#B3CDE3", [50, 145, 300, 50], self).text_on_window()
        
        self.username_input = QLineEdit(self)
        self.username_input.setStyleSheet("background-color: #FFFFFF")
        self.username_input.setGeometry(50, 100, 300, 30)
        
        self.password_input = QLineEdit(self)
        self.password_input.setStyleSheet("background-color: #FFFFFF")
        self.password_input.setGeometry(50, 180, 300, 30)
        
        # log in button that opens a reservation system window
        log_in_button = QPushButton("Log In", self)
        log_in_button.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        log_in_button.setStyleSheet("background-color: #A3C1DA; color: black;")
        log_in_button.move(150, 230)
        log_in_button.clicked.connect(self.log_in_executer) 
        
        self.show()
    
    def reservation_window(self):
        self.main = Reservation_Window()
        self.setGeometry(300, 200, 700, 500)
        self.main.show()
        self.hide()
    
    def log_in_executer(self):
        username = self.username_input.text().lower()
        password = self.password_input.text().lower()
        
        if self.check_user_info(username, password):
            self.reservation_window()
        else:
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #B3CDE3")
            msg.setText('Incorrect Username or Password')
            msg.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
            msg.exec_()
    
    def check_user_info(self, username, password):
        # format of user information = "username password"
        user_pass = username + " " + password + "\n"
        
        # total number of lines in "log_in_info" file
        line_count = sum(1 for line in open('txt_files/log_in_info.txt'))
        
        # checking if user input is in "log_in_info" file
        i = 0
        with open("txt_files/log_in_info.txt") as fp:
            for line in fp:
                if  user_pass == line:
                    return True
                i += 1
        
        # if above loop went through all the lines, but didn't find the line that matches user input
        if i == line_count:
            return False
	

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Log_In_Window()
    sys.exit(app.exec())