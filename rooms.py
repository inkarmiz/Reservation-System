from datetime import datetime, date, timedelta
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QPushButton, QCalendarWidget
from PyQt5 import QtGui


class Calendar(QDialog):
    def __init__(self, room_no):
        super(Calendar, self).__init__()
        self.room_no = room_no
        self.setWindowTitle("Room No. " + str(room_no))
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(date.today()) # past dates cannot be chosen
        self.calendar.setGeometry(0, 0, 400, 300)
        self.setStyleSheet("background-color: #B3CDE3")
        self.setGeometry(450, 300, 400, 300)
        
        self.mark_reserved()
    
    def mark_reserved(self):
        
        self.highlight_format = QtGui.QTextCharFormat()
        self.highlight_format.setBackground(self.palette().brush(QtGui.QPalette.Highlight))
        self.highlight_format.setForeground(self.palette().color(QtGui.QPalette.HighlightedText))
        
        with open("txt_files/room_availability.txt", "r") as f:
            lines = f.readlines()
        
        for line in lines:
            room_dates = line.rstrip('\n').split('#') 
            if room_dates[0] == self.room_no:
                break
        
        room_dates = room_dates[1:]
        
        if len(room_dates) != 0:
            
            for res_date in room_dates:
                formated_date = res_date.split('*')
                d0 = datetime.strptime(formated_date[0], '%Y-%m-%d')
                d1 = datetime.strptime(formated_date[1], '%Y-%m-%d')
                while d0 <= d1:
                    self.calendar.setDateTextFormat(d0, self.highlight_format)
                    d0 = d0 + timedelta(days=1)

class Rooms(QDialog):
    def __init__(self, parent = None):
        super(Rooms, self).__init__(parent)
        self.setGeometry(300, 200, 700, 500)
        self.setWindowTitle("ROOMS")
        self.create_room_table()

    def create_room_table(self):
        self.rooms_table = QTableWidget(self)
        
        self.rooms_table.setGeometry(0, 0, 700, 500)
        line_count = sum(1 for line in open('txt_files/rooms_info.txt'))
        self.rooms_table.setRowCount(line_count)
        self.rooms_table.setColumnCount(5)
        self.rooms_table.setHorizontalHeaderLabels(['Room No.', 'Type', 
                                                     'Capacity', 'Price \n(€ per night)', 'Upcoming \nreservations'])
        
        self.place_room_info()
        
    def place_room_info(self):
        with open("txt_files/rooms_info.txt", "r") as f:
            lines = f.readlines()
        
        function_holder = [self.f101_calendar, self.f102_calendar, self.f103_calendar,
                           self.f104_calendar, self.f105_calendar, self.f106_calendar,
                           self.f107_calendar, self.f108_calendar, self.f109_calendar,
                           self.f110_calendar, self.f111_calendar, self.f112_calendar,
                           self.f113_calendar, self.f114_calendar, self.f115_calendar,
                           self.f116_calendar, self.f117_calendar, self.f118_calendar]
        j = 0
        for line in lines:
            line = line.rstrip()
            line = line.split('#')
        
            for i, value in enumerate(line):
                self.rooms_table.setItem(j, i, QTableWidgetItem(value))
                self.rooms_table.setFont(QtGui.QFont('Times', 15))
                self.rooms_table.setColumnWidth(i, 170)
                self.rooms_table.setColumnWidth(i, 125)
                if i == 3:
                    calendar_button = QPushButton()
                    calendar_button.setStyleSheet('background-color: #FFFFFF')
                    calendar_button.setStyleSheet('background-color: #A3C1DA; color: black;')
                    calendar_button.setIcon(QtGui.QIcon("pictures/calendar.png"))
                    calendar_button.clicked.connect(function_holder[j])
                    
                    self.rooms_table.setColumnWidth(4, 130)
                    self.rooms_table.setCellWidget(j, 4, calendar_button)
                    
                
            j = j + 1 # progresses to the next line
    
    # creates the calendar view to check the reservation dates for each room
    def f101_calendar(self):
        dialog = Calendar('101')
        dialog.exec_()
    
    def f102_calendar(self):
        dialog = Calendar('102')
        dialog.exec_()
    
    def f103_calendar(self):
        dialog = Calendar('103')
        dialog.exec_()
    
    def f104_calendar(self):
        dialog = Calendar('104')
        dialog.exec_()
    
    def f105_calendar(self):
        dialog = Calendar('105')
        dialog.exec_()
        
    def f106_calendar(self):
        dialog = Calendar('106')
        dialog.exec_()
    
    def f107_calendar(self):
        dialog = Calendar('107')
        dialog.exec_()
    
    def f108_calendar(self):
        dialog = Calendar('108')
        dialog.exec_()
    
    def f109_calendar(self):
        dialog = Calendar('109')
        dialog.exec_()
    
    def f110_calendar(self):
        dialog = Calendar('110')
        dialog.exec_()
        
    def f111_calendar(self):
        dialog = Calendar('111')
        dialog.exec_()
    
    def f112_calendar(self):
        dialog = Calendar('112')
        dialog.exec_()
    
    def f113_calendar(self):
        dialog = Calendar('113')
        dialog.exec_()
    
    def f114_calendar(self):
        dialog = Calendar('114')
        dialog.exec_()
    
    def f115_calendar(self):
        dialog = Calendar('115')
        dialog.exec_()
        
    def f116_calendar(self):
        dialog = Calendar('116')
        dialog.exec_()
    
    def f117_calendar(self):
        dialog = Calendar('117')
        dialog.exec_()
    
    def f118_calendar(self):
        dialog = Calendar('118')
        dialog.exec_()
    
