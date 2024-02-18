from datetime import date
from PyQt5.QtWidgets import QDialog, QCalendarWidget, QPushButton, QMessageBox
from label_generator import Label_Generator
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtGui

CHECK_IN_DATE = ""
CHECK_OUT_DATE = ""

class Calendar_Check_Out(QDialog):
    def __init__(self, title):
        super(Calendar_Check_Out, self).__init__()
        self.title = title
        self.setWindowTitle(title)
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(date.today()) # past dates cannot be chosen
        self.calendar.setGeometry(0, 0, 400, 300)
        self.setStyleSheet("background-color: #B3CDE3")
        self.setGeometry(450, 300, 400, 300)
        self.calendar.selectionChanged.connect(self.date)
    
    def date(self):
        global CHECK_IN_DATE
        global CHECK_OUT_DATE
        selected_date = self.calendar.selectedDate()
        
        if self.title == "CHECK IN":
            CHECK_IN_DATE = selected_date.toString("yyyy-MM-dd")
            
        else:
            CHECK_OUT_DATE = selected_date.toString("yyyy-MM-dd")


class Check_out(QDialog):
    def __init__(self, parent = None):
        super(Check_out, self).__init__(parent)
        self.setGeometry(450, 300, 400, 300)
        self.setWindowTitle("CHECK OUT")
    
        Label_Generator("", 0, "#FFFFFF; border: 2px solid black", [25, 50, 350, 225], self).text_on_window()
        
        Label_Generator("CHECK IN", 15, "#FFFFFF", [100, 75, 100, 25], self).text_on_window()
        check_in_button = QPushButton(self)
        check_in_button.setStyleSheet('background-color: #B3CDE3')
        check_in_button.setGeometry(250, 75, 25, 25)
        check_in_button.setIcon(QtGui.QIcon("pictures/calendar.png"))
        check_in_button.clicked.connect(self.check_in_calendar)
        
        Label_Generator("CHECK OUT", 15, "#FFFFFF", [100, 125, 100, 25], self).text_on_window()
        check_out_button = QPushButton(self)
        check_out_button.setStyleSheet('background-color: #B3CDE3')
        check_out_button.setGeometry(250, 125, 25, 25)
        check_out_button.setIcon(QtGui.QIcon("pictures/calendar.png"))
        check_out_button.clicked.connect(self.check_out_calendar)
        
        Label_Generator("ROOM NO.", 15, "#FFFFFF", [100, 175, 125, 25], self).text_on_window()
        self.room_no = QLineEdit(self)
        self.room_no.setStyleSheet("background-color: #FFFFFF")
        self.room_no.setGeometry(225, 175, 75, 25)
        
        
        remove_button = QPushButton("REMOVE RESERVATION", self)
        remove_button.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        remove_button.setStyleSheet("background-color: #B3CDE3; color: black;")
        remove_button.setGeometry(100, 225, 200, 25)
        remove_button.clicked.connect(self.remove_reservation)

    def check_in_calendar(self):
        dialog = Calendar_Check_Out("CHECK IN")
        dialog.exec_()
    
    def check_out_calendar(self):
        dialog = Calendar_Check_Out("CHECK OUT")
        dialog.exec_()
        
    def remove_reservation(self):
        check = self.check_user_input()
        msg = QMessageBox()
        if check == 1:
            msg.setText('Fill all the required information.')
        elif check == 2:
            msg.setText('Check-in and check-out cannot be on the same date.')
        elif check == 3:
            msg.setText('Check-out cannot be before check-in date.')
        else:
            with open("txt_files/room_availability.txt", "r") as f:
                lines = f.readlines()
            
            reservation = []
            found = False
            
            for line in lines:
                new_line = line.rstrip('\n').split('#')
                if new_line[0] == self.room_no.text():
                    for dates in new_line:
                        if CHECK_IN_DATE + '*' + CHECK_OUT_DATE in dates:
                            found = True
                        else:
                            if self.room_no.text() != dates:
                                reservation.append(dates)
                            
            if found == True:
                
                new_line = self.room_no.text() # holds the updated information for the room
                for el in reservation:
                    new_line = new_line + '#' + el
                new_line = new_line + '\n'
                
                for line in lines:
                    if line.rstrip('\n').split('#')[0] == self.room_no.text():
                        lines.remove(line)
                        break
                
                lines.append(new_line)
                
                with open("txt_files/room_availability.txt", "w") as f:
                    for line in lines:
                        f.write(line)
                
                msg.setText('The guest is successfully checked out!')
            else:
                msg.setText('There is no reservation for this room during the selected dates.')
            
        msg.setStyleSheet("background-color: #B3CDE3")
        msg.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        msg.exec_()
    
    def check_user_input(self):
        if CHECK_IN_DATE == "" or CHECK_OUT_DATE == "" or len(self.room_no.text()) == 0:
            return 1
        else:
            # check if dates are valid
            if (CHECK_IN_DATE == CHECK_OUT_DATE):
                return 2
            elif (CHECK_IN_DATE > CHECK_OUT_DATE):
                return 3
            else:
                return 4
                
                
            
            
                
                
        
        
        