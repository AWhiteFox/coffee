import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.load_table()

    def load_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for row in self.cur.execute('SELECT * FROM coffee'):
            c = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(c + 1)
            for j, elem in enumerate(row):
                if j == 3:
                    elem = 'Да' if elem else 'Нет'
                self.tableWidget.setItem(c, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
