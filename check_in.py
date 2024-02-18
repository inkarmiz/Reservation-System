from datetime import datetime, date
from PyQt5.QtWidgets import QMessageBox, QCalendarWidget, QDialog, QLineEdit, QPushButton, QListWidget, QAbstractItemView, QListWidgetItem
from PyQt5 import QtGui
from label_generator import Label_Generator

""" Global variables that store dates and room type/capacity chosen by the user """
CHECK_IN_DATE = ""
CHECK_OUT_DATE = ""
TYPE = ""
CAPACITY = ""
ROOM_NO = ""
ROOMS = [['101', 'economy', 'single'], ['102', 'economy', 'single'], ['103', 'economy', 'single'], 
         ['104', 'economy', 'double'], ['105', 'economy', 'double'], ['106', 'economy', 'double'], 
         ['107', 'economy', 'double'], ['108', 'economy', 'family'], ['109', 'economy', 'family'], 
         ['110', 'economy', 'family'], ['111', 'normal', 'single'], ['112', 'normal', 'single'], 
         ['113', 'normal', 'double'], ['114', 'normal', 'double'], ['115', 'normal', 'family'], 
         ['116', 'VIP', 'single'], ['117', 'VIP', 'double'], ['118', 'VIP', 'family']]

""" Calendar view for choosing check in/out dates """
class Calendar_Reserve(QDialog):
    def __init__(self, title):
        super(Calendar_Reserve, self).__init__()
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
     
    


""" Prints the check in/out dates, and calculates the days of stay and price """
class Summary(QDialog):
    def __init__(self, parent = None):
        super(Summary, self).__init__(parent)
        self.setGeometry(450, 300, 400, 300)
        self.setWindowTitle("SUMMARY")
    
    def summary_window(self):
        Label_Generator("", 0, "#FFFFFF; border: 2px solid black", [25, 50, 350, 225], self).text_on_window()
        Label_Generator("CHECK IN", 15, "#FFFFFF", [75, 75, 100, 25], self).text_on_window()
        Label_Generator("CHECK OUT", 15, "#FFFFFF", [75, 100, 100, 25], self).text_on_window()
        Label_Generator("ROOM TYPE", 15, "#FFFFFF", [75, 125, 100, 25], self).text_on_window()
        Label_Generator("CAPACITY", 15, "#FFFFFF", [75, 150, 100, 25], self).text_on_window()
        Label_Generator("ROOM NO.", 15, "#FFFFFF", [75, 175, 100, 25], self).text_on_window()
        Label_Generator("STAY DURATION", 15, "#FFFFFF", [75, 200, 125, 25], self).text_on_window()
        Label_Generator("TOTAL COST", 15, "#FFFFFF", [75, 225, 125, 25], self).text_on_window()
        
        Label_Generator(CHECK_IN_DATE, 15, "#FFFFFF", [225, 75, 100, 25], self).text_on_window()
        Label_Generator(CHECK_OUT_DATE, 15, "#FFFFFF", [225, 100, 100, 25], self).text_on_window()
        Label_Generator(TYPE, 15, "#FFFFFF", [225, 125, 100, 25], self).text_on_window()
        Label_Generator(CAPACITY, 15, "#FFFFFF", [225, 150, 100, 25], self).text_on_window()
        Label_Generator(ROOM_NO, 15, "#FFFFFF", [225, 175, 100, 25], self).text_on_window()
        
        nights = self.calculate_nights(CHECK_IN_DATE, CHECK_OUT_DATE)
        Label_Generator(nights + " nights", 15, "#FFFFFF", [225, 200, 125, 25], self).text_on_window()
        cost = self.calculate_price(TYPE, CAPACITY, int(nights))
        Label_Generator(str(cost) + "€", 15, "#FFFFFF", [225, 225, 125, 25], self).text_on_window()

    def calculate_nights(self, check_in, check_out):
        check_in_converted = datetime.strptime(check_in, '%Y-%m-%d')
        check_out_converted = datetime.strptime(check_out, '%Y-%m-%d')
        return str(check_out_converted - check_in_converted).split(' ', 1)[0]
    
    def calculate_price(self, room_type, room_capacity, nights):
        types = ["economy", "normal", "VIP"]
        capacities = ["single", "double", "family"]
        prices = [[10, 15, 20], [25, 30, 35], [40, 45,50]] # price of stay in euros per night
        return prices[types.index(room_type)][capacities.index(room_capacity)] * nights
    

""" Check-in dialog window """
class Check_in(QDialog):
    def __init__(self, parent = None):
        super(Check_in, self).__init__(parent)
        self.setGeometry(300, 200, 700, 500)
        self.setWindowTitle("CHECK IN")
        
        Label_Generator("", 0, "#A3C1DA; border: 2px solid black", [25, 75, 325, 350], self).text_on_window()
        Label_Generator("", 0, "#A3C1DA; border: 2px solid black", [400, 75, 275, 175], self).text_on_window()
        Label_Generator("", 0, "#A3C1DA; border: 2px solid black", [400, 300, 275, 125], self).text_on_window()
        Label_Generator("PERSONAL INFORMATION", 15, "#FFFFFF; border: 2px solid black", [75, 50, 225, 50], self).text_central()
        Label_Generator("ROOM", 15, "#FFFFFF; border: 2px solid black", [475, 50, 125, 50], self).text_central()
        Label_Generator("DATES", 15, "#FFFFFF; border: 2px solid black", [475, 275, 125, 50], self).text_central()
        
        self.empty_variables()
        self.personal_info()
        self.room()
        self.dates()
        
        submit_button = QPushButton("SUBMIT", self)
        submit_button.setStyleSheet('background-color: #FFFFFF; color: black')
        submit_button.setFont(QtGui.QFont('Times', 15))
        submit_button.setGeometry(575, 450, 100, 25)
        submit_button.clicked.connect(self.guest_record)
    
    """ Clears global variables every time this dialog window is opened """
    def empty_variables(self):
        global CHECK_IN_DATE
        CHECK_IN_DATE = ""
        global CHECK_OUT_DATE
        CHECK_OUT_DATE = ""
        global TYPE
        TYPE = ""
        global CAPACITY
        CAPACITY = ""
        global ROOM_NO
        ROOM_NO = ""
    
    """ Records the personal information of the guest """
    def personal_info(self):
        
        Label_Generator("Name", 15, "#A3C1DA", [50, 125, 100, 25], self).text_on_window()
        self.name = QLineEdit(self)
        self.name.setStyleSheet("background-color: #FFFFFF")
        self.name.setGeometry(175, 125, 150, 25)
        
        Label_Generator("Surname", 15, "#A3C1DA", [50, 175, 100, 25], self).text_on_window()
        self.surname = QLineEdit(self)
        self.surname.setStyleSheet("background-color: #FFFFFF")
        self.surname.setGeometry(175, 175, 150, 25)
        
        Label_Generator("Phone", 15, "#A3C1DA", [50, 225, 100, 25], self).text_on_window()
        self.phone = QLineEdit(self)
        self.phone.setStyleSheet("background-color: #FFFFFF")
        self.phone.setGeometry(175, 225, 150, 25)
        
        Label_Generator("Email", 15, "#A3C1DA", [50, 275, 100, 25], self).text_on_window()
        self.email = QLineEdit(self)
        self.email.setStyleSheet("background-color: #FFFFFF")
        self.email.setGeometry(175, 275, 150, 25)
        
        Label_Generator("Nationality", 15, "#A3C1DA", [50, 325, 100, 25], self).text_on_window()
        self.nationality = QLineEdit(self)
        self.nationality.setStyleSheet("background-color: #FFFFFF")
        self.nationality.setGeometry(175, 325, 150, 25)
        
        Label_Generator("Passport No.", 15, "#A3C1DA", [50, 375, 100, 25], self).text_on_window()
        self.passport = QLineEdit(self)
        self.passport.setStyleSheet("background-color: #FFFFFF")
        self.passport.setGeometry(175, 375, 150, 25)
        
    
    """ Records the choice of room type and capacity """
    def room(self):
        
        # choosing the room type (from the list ["economy", "normal", "VIP"])
        
        Label_Generator("TYPE", 15, "#A3C1DA", [425, 125, 100, 25], self).text_central()
        self.room_type = QListWidget(self)
        self.room_type.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.room_type.setGeometry(425, 150, 100, 55)
        self.room_type.setFont(QtGui.QFont('Times', 15))
        self.room_type.setStyleSheet("background-color: #FFFFFF")
        for option in ["economy", "normal", "VIP"]:
            self.room_type.addItem(QListWidgetItem(option))
        
        def room_type_choice():
            global TYPE
            room = self.room_type.selectedItems()
            for i in range(len(room)):
                TYPE = str(self.room_type.selectedItems()[i].text())
        
        self.last_choice_type = self.room_type.itemClicked.connect(room_type_choice)
        
        # choosing the room capacity (from the list ["single", "double", "family"])
        Label_Generator("CAPACITY", 15, "#A3C1DA", [550, 125, 100, 25], self).text_central()
        self.room_capacity = QListWidget(self)
        self.room_capacity.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.room_capacity.setGeometry(550, 150, 100, 55)
        self.room_capacity.setFont(QtGui.QFont('Times', 15))
        self.room_capacity.setStyleSheet("background-color: #FFFFFF")
        for option in ["single", "double", "family"]:
            self.room_capacity.addItem(QListWidgetItem(option))
        
        def room_capacity_choice():
            global CAPACITY
            room = self.room_capacity.selectedItems()
            for i in range(len(room)):
                CAPACITY = str(self.room_capacity.selectedItems()[i].text())
        
        self.room_capacity.itemClicked.connect(room_capacity_choice)
        
    """ Records the check in/out dates """    
    def dates(self):
        
        Label_Generator("CHECK IN", 15, "#A3C1DA", [460, 330, 100, 25], self).text_on_window()
        Label_Generator("CHECK OUT", 15, "#A3C1DA", [460, 370, 100, 25], self).text_on_window()
        
        check_in_button = QPushButton(self)
        check_in_button.setStyleSheet('background-color: #FFFFFF')
        check_in_button.setGeometry(590, 330, 25, 25)
        check_in_button.setIcon(QtGui.QIcon("pictures/calendar.png"))
        check_in_button.clicked.connect(self.check_in_calendar)
        
        check_out_button = QPushButton(self)
        check_out_button.setStyleSheet('background-color: #FFFFFF')
        check_out_button.setGeometry(590, 370, 25, 25)
        check_out_button.setIcon(QtGui.QIcon("pictures/calendar.png"))
        check_out_button.clicked.connect(self.check_out_calendar)
    
    """ Calls the Calendar Dialog Window """
    def check_in_calendar(self):
        dialog = Calendar_Reserve("CHECK IN")
        dialog.exec_()
    
    def check_out_calendar(self):
        dialog = Calendar_Reserve("CHECK OUT")
        dialog.exec_()
    
    """ Calls the Summary Dialog Window """
    def print_summary(self):
        dialog = Summary(self)
        dialog.summary_window()
        dialog.exec_()
 
    """ Writes the user input to the file """
    def guest_record(self):
        
        check = self.check_user_input()
        status = ''
        msg = QMessageBox()
        
        if check == 0:
            msg.setText('Fill all the lines.')
        elif check == 1:
            msg.setText('Name is invalid.')
        elif check == 2:
            msg.setText('Surname is invalid.')
        elif check == 3:
            msg.setText('Please enter the phone number with country code.')
        elif check == 4:
            msg.setText('Phone number is invalid.')
        elif check == 5:
            msg.setText('Email is invalid.')
        elif check == 6:
            msg.setText('Entered nationality does not exist.')
        elif check == 7:
            msg.setText('Check-in and check-out cannot be on the same date.')
        elif check == 8:
            msg.setText('Check-out cannot be before check-in date.')
        else:
            # guest_id is the total number of guests when this guest made a reservation
            guest_id = sum(1 for line in open('txt_files/guest_records.txt')) + 1
            
            # recording the dates and connecting the guest_id to the room
            selected_rooms = [] # stores the rooms that fulfill type and capacity choices of the guest
            for room in ROOMS:
                if room[1] == TYPE and room[2] == CAPACITY:
                    selected_rooms.append(room[0])
            
            with open("txt_files/room_availability.txt", "r") as f:
                lines = f.readlines()
            
            new_reserve_rooms = [] # stores the desired rooms with their reserved dates
            for line in lines:
                for room in selected_rooms:
                    if line.rstrip('\n').split('#')[0] == room:
                        new_reserve_rooms.append(line)
            
            room_dates = {} # dict for room and its reserved dates
            
            for line in new_reserve_rooms:
                new_line = line.rstrip('\n').split("#")
                room_dates[new_line[0]] = new_line[1:]
            
            
            
            def nested_loop():
                for room in room_dates: # room with unseparate date info
                    room_info = room_dates.get(room)
                    overlap_or_ok = []
                    for dates in room_info: # unseparate date info
                        if len(dates) == 1: # if room does not have any reservation
                            return (room, '#' + CHECK_IN_DATE + '*' + CHECK_OUT_DATE + '*' + str(guest_id))
                        
                        dates_split = dates.split("*")
                        if len(dates_split) != 1:
                            overlap_or_ok.append( self.check_date(CHECK_IN_DATE, CHECK_OUT_DATE, dates_split[0], dates_split[1]) )
                    
                    if 'OVERLAP' not in overlap_or_ok:
                        return (room, '#' + CHECK_IN_DATE + '*' + CHECK_OUT_DATE + '*' + str(guest_id) + '\n')
                return 'NO ROOM'
            
            pair = nested_loop()
            
            if pair != 'NO ROOM':
                global ROOM_NO
                ROOM_NO = pair[0]
                # reserving the room and connecting the guest id to it in "room_availability.txt"
                line_copy = []
                for line in lines:
                    if line.rstrip('\n').split('#')[0] == pair[0]:
                        line_copy.append(line)
                        lines.remove(line)
                        break
                
                lines.append((line_copy[0].rstrip('\n') + pair[1]))          
                
                with open("txt_files/room_availability.txt", "w") as f:
                    for line in lines:
                        f.write(line)
                
                # recording the information of guest in the file "guest_records.txt"
                with open("txt_files/guest_records.txt", "a") as f:
                    f.write(self.name.text().lower() + "#" + self.surname.text().lower() + "#" + 
                            self.phone.text() + "#" + self.email.text().lower() + "#" + 
                            self.nationality.text() + "#" + self.passport.text().lower() + "#" + 
                            str(guest_id) + "#" + CHECK_IN_DATE + '*' + CHECK_OUT_DATE + '*' + ROOM_NO + "\n")
                
                # executed when guest information is recorded and desirable room is reserved
                status = "SUCCESS"
                msg.setText('The room is successfully reserved!')
                # prints the summary of the order
                self.print_summary()
            else:
                msg.setText('No available rooms for this date!')
         
        msg.setStyleSheet("background-color: #B3CDE3")
        msg.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        msg.exec_()
        if status == "SUCCESS":
            self.close()
    
    """ Checks the user input """
    def check_user_input(self):
        user_input = [self.name.text(), self.surname.text(), 
                      self.phone.text(), self.email.text(), 
                      self.nationality.text(), self.passport.text(),
                      TYPE, CAPACITY, CHECK_IN_DATE, CHECK_OUT_DATE]
        
        # checking if none of the user input is empty
        for input in user_input:
            if len(input) == 0:
                return 0
        
        # checking if name and surname are valid
        name = self.name.text()
        surname = self.surname.text()
        if name.isalpha() != True:  
            return 1
        
        if surname.isalpha() != True:
            return 2
        
        # checking if phone number is valid
        phone = self.phone.text()
        if phone[0] != "+":
            return 3
        
        phone = phone.lstrip("+")
        if phone.isnumeric() != True:
            return 4
        
        # checking the email
        email = self.email.text()
        if "@" not in email:
            return 5
        
        # checking if the nationality is valid
        nationality = self.nationality.text()
        with open("txt_files/nationalities.txt", "r") as f:
            lines = f.readlines()
        if nationality + '\n' not in lines:
            return 6
        
        # check if dates are valid
        if (CHECK_IN_DATE == CHECK_OUT_DATE):
            return 7
        elif (CHECK_IN_DATE > CHECK_OUT_DATE):
            return 8
    
    
    
    def check_date(self, check_in_str, check_out_str, other_check_in_str, other_check_out_str):
        
        check_in = datetime.strptime(check_in_str, '%Y-%m-%d')
        check_out = datetime.strptime(check_out_str, '%Y-%m-%d')
        other_check_in = datetime.strptime(other_check_in_str, '%Y-%m-%d')
        other_check_out = datetime.strptime(other_check_out_str, '%Y-%m-%d')
        
        if check_out < other_check_in or (check_out == other_check_in and check_in < other_check_in) or other_check_out < check_in or (check_in == other_check_out and other_check_in < check_in):
            return "OK"
        else:
            return "OVERLAP"
    
        
    