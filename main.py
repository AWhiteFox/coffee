import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.update_table()

        self.add_btn.pressed.connect(self.on_add)
        self.edit_btn.pressed.connect(self.on_edit)

        self.form = None

    def update_table(self):
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

    def on_add(self):
        if self.form:
            self.statusBar.showMessage('Форма уже открыта!', 2000)
            return
        self.form = AddEditForm(self, self.con, self.cur)
        self.form.show()

    def on_edit(self):
        if self.form:
            self.statusBar.showMessage('Форма уже открыта!', 2000)
            return
        cell = self.tableWidget.item(self.tableWidget.currentRow(), 0)
        if not cell:
            self.statusBar.showMessage('Выберите строку!', 2000)
            return
        self.form = AddEditForm(self, self.con, self.cur, int(cell.text()))
        self.form.show()


class AddEditForm(QWidget):
    def __init__(self, main, db_connection, db_cursor, row_id=None):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.main = main
        self.con = db_connection
        self.cur = db_cursor
        self.row_id = row_id

        self.btn.pressed.connect(self.on_btn)
        if self.row_id:
            self.load_data()

    def closeEvent(self, *args):
        self.main.form = None
        self.main.update_table()

    def load_data(self):
        data = self.cur.execute('SELECT * FROM coffee WHERE id=?', (self.row_id, )).fetchone()
        self.lineEdit_sort.setText(data[1])
        self.lineEdit_roast.setText(data[2])
        self.checkBox_ground.setChecked(data[3])
        self.lineEdit_description.setText(data[4])
        self.spinBox_price.setValue(data[5])
        self.spinBox_grams.setValue(data[6])

    def on_btn(self):
        values = [
            self.lineEdit_sort.text(),
            self.lineEdit_roast.text(),
            self.checkBox_ground.isChecked(),
            self.lineEdit_description.text(),
            self.spinBox_price.value(),
            self.spinBox_grams.value()
        ]
        if self.row_id:
            self.edit(values)
        else:
            self.add(values)
        self.con.commit()
        self.close()

    def add(self, values):
        cmd = 'INSERT INTO coffee (name, roast, ground, description, price, grams) ' \
              'VALUES (?, ?, ?, ?, ?, ?)'
        self.cur.execute(cmd, values)

    def edit(self, values):
        cmd = 'UPDATE coffee SET name=?, roast=?, ground=?, description=?, price=?, grams=? ' \
              'WHERE id=?'
        self.cur.execute(cmd, values + [self.row_id])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
