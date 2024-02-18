from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt5 import QtGui

class Guests(QDialog):
    def __init__(self, parent = None):
        super(Guests, self).__init__()
        self.setWindowTitle('GUESTS')
        self.setStyleSheet("background-color: #B3CDE3")
        self.setGeometry(300, 200, 700, 500)
        self.create_guest_table()
        
    def create_guest_table(self):
        self.guests_table = QTableWidget(self)
        
        self.guests_table.setGeometry(0, 0, 700, 500)
        line_count = sum(1 for line in open('txt_files/guest_records.txt'))
        self.guests_table.setRowCount(line_count)
        self.guests_table.setColumnCount(7)
        self.guests_table.setHorizontalHeaderLabels(['Name', 'Surname', 
                                                     'Phone', 'Email', 
                                                     'Nationality', 'Passport', 
                                                     'Guest ID'])
        self.place_guest_info()
        
    def place_guest_info(self):
        with open("txt_files/guest_records.txt", "r") as f:
            lines = f.readlines()
        
        j = 0
        for line in lines:
            line = line.rstrip()
            line = line.split('#')
            
            for i, value in enumerate(line):
                if i == 7:
                    break
                self.guests_table.setItem(j, i, QTableWidgetItem(value))
                self.guests_table.setFont(QtGui.QFont('Times', 15))
            
            j = j + 1 # progresses to the next line
            
        # resizing the table according to the content width
        self.guests_table.resizeColumnsToContents()
        self.guests_table.setColumnWidth(6, 70)