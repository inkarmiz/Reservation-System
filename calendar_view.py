from datetime import date
from PyQt5.QtWidgets import QCalendarWidget, QDialog, QLabel, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui
from label_generator import Label_Generator

""" Global variables that store dates and room type/capacity chosen by the user """
DATE = date.today().strftime("%Y-%m-%d")
CHECK_INS = []
CHECK_OUTS = []

class Calendar_View(QDialog):
    def __init__(self):
        super(Calendar_View, self).__init__()
        self.setWindowTitle('CALENDAR')
        self.setStyleSheet("background-color: #B3CDE3")
        self.setGeometry(450, 250, 400, 400)
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(50, 25, 300, 200)
        self.calendar.setStyleSheet("background-color: #FFFFFF")
        self.calendar.selectionChanged.connect(self.save_date)
        self.calendar.clicked[QtCore.QDate].connect(self.showDate)
		
        self.date_print = QLabel(self)
        selected_date = self.calendar.selectedDate()
        self.date_print.setText(selected_date.toString())
        self.date_print.setFont(QtGui.QFont('Times', 15))
        self.date_print.setAlignment(QtCore.Qt.AlignCenter)
        self.date_print.setGeometry(125, 250, 150, 25)
        
        button = QPushButton('EVENTS', self)
        button.setStyleSheet('background-color: #FFFFFF; color: black;')
        button.setFont(QtGui.QFont('Times', 15))
        button.setGeometry(150, 325, 100, 25)
        
        button.clicked.connect(self.day_all_info)
    
    
    def save_date(self):
        global DATE
        selected_date = self.calendar.selectedDate()
        DATE = selected_date.toString("yyyy-MM-dd")
    
    def showDate(self, date):
        self.date_print.setText(date.toString())
    
    
    """ Checks if there are any events (check-in or check-out) on that day"""
    def day_all_info(self):
        with open("txt_files/guest_records.txt", "r") as f:
            lines = f.readlines()
            
        check_ins = []
        check_outs = []
        for line in lines:
            if '#' + DATE + '*' in line:
                check_ins.append(line)
            elif '*' + DATE + '*' in line:
                check_outs.append(line)    
                
        if len(check_ins) == 0 and len(check_outs) == 0:
            self.error_info('There is no event on that date.')
        else:
            global CHECK_INS
            CHECK_INS = check_ins
            global CHECK_OUTS
            CHECK_OUTS = check_outs
            self.stats_window()
        
    def error_info(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.setStyleSheet("background-color: #B3CDE3")
        msg.setFont(QtGui.QFont('Times', 15, QtGui.QFont.Bold))
        msg.exec_()
        
    """ Reports """
    def stats_window(self):
        dialog = Reports(self)
        dialog.exec_()


class Reports(QDialog):
    def __init__(self, parent = None):
        super(Reports, self).__init__(parent)
        self.setGeometry(450, 250, 400, 400)
        self.setWindowTitle("Reports")
        self.print_info()
    
    def print_info(self):
        
        def inner(infos):
            check_in_out = '' # stores the customer info who checked in\out that day
            if len(infos) != 0:
                dates = '' # stores the check in + check out + room information
                for info in infos:
                    new_line = info.rstrip('\n').split('#')
                    dates = new_line[-1].split('*')
                    dates = new_line[-1].split('*')
                    str_dates = 'CHECK IN: ' + dates[0] + '\n' + 'CHECK OUT: ' + dates[1] + '\n' + 'ROOM NO: ' + dates[2]
                    check_in_out = check_in_out + '\n' + new_line[0].capitalize() + ' ' + new_line[1].capitalize() + '\n' +  str_dates + '\n'
            return check_in_out
            
        Label_Generator('CHECK-IN', 13, "#B3CDE3", [25, 25, 150, 25], self).text_on_window()
        Label_Generator(inner(CHECK_INS) + '\n' + str(len(CHECK_INS)) + ' checked-in guests', 13, "#B3CDE3", [25, 50, 150, 325], self).text_on_window()
        
        Label_Generator('CHECK-OUT', 13, "#B3CDE3", [225, 25, 150, 25], self).text_on_window()
        Label_Generator(inner(CHECK_OUTS) + '\n' + str(len(CHECK_OUTS)) + ' checked-out guests', 13, "#B3CDE3", [225, 50, 150, 325], self).text_on_window()
        
        
        
        
    
 