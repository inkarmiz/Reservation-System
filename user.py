from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QMessageBox
from PyQt5 import QtGui
from label_generator import Label_Generator

class User(QDialog):
    def __init__(self, title):
        super(User, self).__init__()
        self.setWindowTitle(title)
        self.setStyleSheet("background-color: #B3CDE3")
        self.setGeometry(425, 300, 450, 350)
    
    def user_input(self):
        # generating labels on the window
        Label_Generator("Enter Username", 15, "#B3CDE3", [75, 50, 300, 50], self).text_on_window()
        Label_Generator("Enter Password", 15, "#B3CDE3", [75, 115, 300, 50], self).text_on_window()
        Label_Generator("Verify Password", 15, "#B3CDE3", [75, 180, 300, 50], self).text_on_window()
        
        # generating QLineEdit for user input
        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(75, 85, 300, 30)
        self.username_input.setStyleSheet("background-color: #FFFFFF")
                
        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(75, 150, 300, 30)
        self.password_input.setStyleSheet("background-color: #FFFFFF")
        
        self.verify_input = QLineEdit(self)
        self.verify_input.setGeometry(75, 215, 300, 30)
        self.verify_input.setStyleSheet("background-color: #FFFFFF")
    
    
    """ 
    Checks the user input:
        - returns 0, if input is empty
        - returns 1, if password confirmation failed
        - returns 2, if username and password are already in the system
        - returns 3, if username and password have not been found.
        - returns 4, if username contains spaces.
    """
    
    def check_new_user(self, username, password, re_enter):
        
        if len(username) == 0 or len(password) == 0 or len(re_enter) == 0:
            return 0
        
        if " " in username:
            return 4
        
        if password != re_enter:
            return 1
        else:
            # format of user information = "username password"
            user_pass = username + " " + password + "\n"
            
            # total number of lines in "log_in_info" file
            line_count = sum(1 for line in open('txt_files/log_in_info.txt'))
            
            # checking if user input is in "log_in_info" file
            i = 0
            with open("txt_files/log_in_info.txt") as fp:
                for line in fp:
                    if  user_pass == line:
                        return 2
                    i += 1
            
            # if above loop went through all the lines, but didn't find the line that matches user input
            if i == line_count:
                return 3
    
    """ 
    The function that executes the "REMOVE USER" 
    """
    
    def remove_button(self):    
        self.remove_button = QPushButton("REMOVE", self)
        self.remove_button.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        self.remove_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.remove_button.setGeometry(175, 275, 100, 50)
        self.remove_button.clicked.connect(self.remove_user_executer)
    
    def remove_user_executer(self):
        
        username = self.username_input.text()
        password = self.password_input.text()
        re_enter = self.verify_input.text()
        
        msg = QMessageBox()
        remove_user = self.check_new_user(username, password, re_enter)
        
        if remove_user == 0:
            msg.setText('Fill all the lines.')
        elif remove_user == 1:
            msg.setText('Passwords do not match. Try again.')
        elif remove_user == 2:
            # removing the username and password from the file
            with open("txt_files/log_in_info.txt", "r") as f:
                lines = f.readlines()
            with open("txt_files/log_in_info.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != username + " " + password:
                        f.write(line)
            msg.setText('The user was successfully removed from the system!')
        
        else:
            msg.setText('This user is not in the system.')
        
        msg.setStyleSheet("background-color: #B3CDE3")
        msg.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        msg.exec_()
    
    
    """ 
    The function that executes the "ADD USER" 
    """
    
    def add_button(self):    
        # adding the "ADD" button
        self.add_button = QPushButton("ADD", self)
        self.add_button.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        self.add_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
        self.add_button.setGeometry(175, 275, 100, 50)
        self.add_button.clicked.connect(self.add_user_executer)
    
    def add_user_executer(self):
        
        username = self.username_input.text()
        password = self.password_input.text()
        re_enter = self.verify_input.text()
        
        msg = QMessageBox()
        add_user = self.check_new_user(username, password, re_enter)
        
        if add_user == 0:
            msg.setText('Fill all the lines.')
        elif add_user == 1:
            msg.setText('Passwords do not match. Try again.')
        elif add_user == 2:
            msg.setText('This user is already in the system.')
        elif add_user == 4:
            msg.setText('Username cannot contain spaces.')
        else:
            line_count = sum(1 for line in open('txt_files/log_in_info.txt'))
            if line_count >= 14:
                msg.setText('Too many users in the system.')
            else:
                with open("txt_files/log_in_info.txt", "r") as f:
                    lines = f.readlines()
                usernames = []
            
                for line in lines:
                    usernames.append(line.split()[0])
            
                if username in usernames:
                    msg.setText("This username is already taken.")
                else:
                    # adding the user to the system
                    with open("txt_files/log_in_info.txt", "a") as f:
                        f.write(username + " " + password + "\n")
                    msg.setText('The user was successfully added to the system!')
            
        
        msg.setStyleSheet("background-color: #B3CDE3")
        msg.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        msg.exec_()
        
        
        
    """ The function that executes the "SHOW USER LIST" """
    
    def show_list_executer(self):
        with open("txt_files/log_in_info.txt", "r") as f:
            lines = f.readlines()
        
        username = ""
        password = ""
        for line in lines:
            username = username + line.split()[0] + "\n"
            password = password + len(line.split()[1]) * "*" + "\n"
        
        Label_Generator(username, 17, "#B3CDE3", [100, 65, 100, 260], self).text_on_window()
        Label_Generator(password, 17, "#B3CDE3", [250, 65, 100, 260], self).text_on_window()
        Label_Generator("USERNAME", 20, "#B3CDE3", [50, 25, 175, 25], self).text_on_window()
        Label_Generator("PASSWORD", 20, "#B3CDE3", [250, 25, 175, 25], self).text_on_window()
        
        
        
        
        