from datetime import date
from PyQt5.QtWidgets import QDialog, QPushButton, QCalendarWidget, QLineEdit, QMessageBox, QListWidgetItem, QListWidget, QAbstractItemView
from label_generator import Label_Generator
from PyQt5 import QtGui

CHECK_IN_DATE = ''
CHECK_IN_DATE = ''
SERVICE = ''

class Calendar_Services(QDialog):
    def __init__(self, title):
        super(Calendar_Services, self).__init__()
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

class Services(QDialog):
    def __init__(self, parent = None):
        super(Services, self).__init__(parent)
        self.setGeometry(450, 300, 400, 300)
        self.setWindowTitle("SERVICES")
        
        Label_Generator("", 0, "#FFFFFF; border: 2px solid black", [25, 50, 350, 225], self).text_on_window()
        
        Label_Generator("CHECK IN", 15, "#FFFFFF", [50, 75, 100, 25], self).text_on_window()
        check_in_button = QPushButton(self)
        check_in_button.setStyleSheet('background-color: #B3CDE3')
        check_in_button.setGeometry(160, 75, 25, 25)
        check_in_button.setIcon(QtGui.QIcon("pictures/calendar.png"))
        check_in_button.clicked.connect(self.check_in_calendar)
        
        Label_Generator("CHECK OUT", 15, "#FFFFFF", [50, 125, 100, 25], self).text_on_window()
        check_out_button = QPushButton(self)
        check_out_button.setStyleSheet('background-color: #B3CDE3')
        check_out_button.setGeometry(160, 125, 25, 25)
        check_out_button.setIcon(QtGui.QIcon("pictures/calendar.png"))
        check_out_button.clicked.connect(self.check_out_calendar)
        
        Label_Generator("ROOM NO.", 15, "#FFFFFF", [50, 175, 125, 25], self).text_on_window()
        self.room_no = QLineEdit(self)
        self.room_no.setStyleSheet("background-color: #FFFFFF")
        self.room_no.setGeometry(150, 175, 50, 25)
        
        Label_Generator("SERVICES", 15, "#FFFFFF", [235, 75, 100, 25], self).text_central()
        self.service = QListWidget(self)
        self.service.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.service.setGeometry(235, 110, 100, 90)
        self.service.setFont(QtGui.QFont('Times', 15))
        self.service.setStyleSheet("background-color: #FFFFFF")
        for option in ["cleaning", "additional bed", "breakfast", "dinner", "laundry"]:
            self.service.addItem(QListWidgetItem(option))
            
        def service_choice():
            global SERVICE
            service_kind = self.service.selectedItems()
            for i in range(len(service_kind)):
                SERVICE = str(self.service.selectedItems()[i].text())
        
        self.last_choice_type = self.service.itemClicked.connect(service_choice)
        
        confirm = QPushButton("Confirm", self)
        confirm.setStyleSheet('background-color: #B3CDE3')
        confirm.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        confirm.setGeometry(150, 230, 100, 25)
        confirm.clicked.connect(self.connect_to_reservation)
        
    
    def check_in_calendar(self):
        dialog = Calendar_Services("CHECK IN")
        dialog.exec_()
    
    def check_out_calendar(self):
        dialog = Calendar_Services("CHECK OUT")
        dialog.exec_()
        
    
    def connect_to_reservation(self):
        check = self.check_user_input()
        msg = QMessageBox()
        success = 'NO'
        if check == 1:
            msg.setText('Fill all the required information.')
        elif check == 2:
            msg.setText('Check-in and check-out cannot be on the same date.')
        elif check == 3:
            msg.setText('Check-out cannot be before check-in date.')
        else:
            with open("txt_files/guest_records.txt", "r") as f:
                lines = f.readlines()   
            found = False
            
            dates_found = CHECK_IN_DATE + '*' + CHECK_OUT_DATE + '*' + self.room_no.text()
           
            
            for line in lines:
                new_line = line.rstrip('\n').split('#')
                if dates_found in new_line[7]:
                    found = True
                    new_line[7] = dates_found + '*' + SERVICE
                    break
            
            if found == True:
                reservation = '#'.join(new_line) + '\n'
                
                for line in lines:
                    if new_line[0] + '#' + new_line[1] in line:
                        lines.remove(line)
                        break
                
                lines.append(reservation)
                
                with open("txt_files/guest_records.txt", "w") as f:
                    for line in lines:
                        f.write(line)
                
                msg.setText('The service is connected to the reservation!')
                success = 'YES'
            else:
                msg.setText('There is no reservation for this room during the selected dates.')
                
        msg.setStyleSheet("background-color: #B3CDE3")
        msg.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        msg.exec_()
        if success == "YES":
            self.close()
    
    def check_user_input(self):
        if CHECK_IN_DATE == "" or CHECK_OUT_DATE == "" or len(self.room_no.text()) == 0 or SERVICE == "":
            return 1
        else:
            # check if dates are valid
            if (CHECK_IN_DATE == CHECK_OUT_DATE):
                return 2
            elif (CHECK_IN_DATE > CHECK_OUT_DATE):
                return 3
            else:
                return 4
            

    