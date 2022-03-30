import psycopg2
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QAbstractScrollArea, 
QVBoxLayout, QHBoxLayout, QTableWidget, QGroupBox, QTableWidgetItem, QPushButton, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Список группы")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="mtuci_group", user="postgres", password="3682597sos", host="localhost", port="5432")
        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Студенты")

        self.record_gbox = QGroupBox("Студенты БОС1901")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.record_gbox)

        self._create_record_table()

        self.update_shedule_button = QPushButton("Обновить")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_record_table(self):
        self.record_table = QTableWidget()
        self.record_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self._update_record_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.record_table)
        self.record_gbox.setLayout(self.mvbox)
    def _update_record_table(self):

        self.record_table.setColumnCount(5)
        self.record_table.setHorizontalHeaderLabels(["Номер СБ", "ФИО", "Паспорт", "", ""])

        self.cursor.execute("SELECT * FROM students ORDER BY name")
        records = list(self.cursor.fetchall())

        self.record_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)

            self.record_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.record_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.record_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            joinButton = QPushButton("Join")
            self.record_table.setCellWidget(i, 3, joinButton)
            deleteButton = QPushButton("Delete") 
            self.record_table.setCellWidget(i, 4, deleteButton)
            addButton = QPushButton("Add") 
            self.record_table.setCellWidget(i+1, 3, addButton)

            joinButton.clicked.connect(lambda ch, num=i: self._change_record_from_table(num))
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_record_from_table(num, self.record_table)) 
            addButton.clicked.connect(lambda ch, num=i: self._add_record_table(num+1, self.record_table))

            self.record_table.resizeRowsToContents()
            
    def _change_record_from_table(self, rowNum):
        row = list()
        for i in range(self.record_table.columnCount()):
            try:
                row.append(self.record_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE students SET id=%s, name=%s, passport=%s",(str(row[0]),str(row[1]),str(row[2])))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
    
    def _delete_record_from_table(self, rowNumb, table):  
        row = list()  
        for i in range(table.columnCount()):  
            try:  
                row.append(table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        #print(row)
        try:
            self.cursor.execute("DELETE FROM students WHERE id=%s AND name=%s AND passport=%s",(str(row[0]),str(row[1]),str(row[2])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
    
    def _add_record_table(self, rowNumb, table):
        row = list()  
        for i in range(table.columnCount()):  
            try:  
                row.append(table.item(rowNumb, i).text())  
            except:  
                row.append(None) 
        #print(row) 
        try:
            self.cursor.execute("INSERT INTO students (id, name, passport) VALUES (%s, %s, %s)",(str(row[0]),str(row[1]),str(row[2])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
    
    def _update_shedule(self):
        self.record_table.clear()
        self._update_record_table()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())