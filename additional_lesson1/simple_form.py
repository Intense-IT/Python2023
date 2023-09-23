# Программа, создающая простую форму.
# По нажатию кнопки все данные полей формы сохраняются в базу данных.
import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
# Импортируем класс QDate для работы с датами в PyQt
from PyQt5.QtCore import QDate

# Библиотека для работы с датами
import datetime


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # Импортируем интерфейс form.ui, созданный нами в QtDesigner
        uic.loadUi('ui/form.ui', self)

        # Создаем соединение к нашей базе данных.
        self.con = sqlite3.connect('db/users.db')
        # Необходимо правильно указывать пути к форме и базе данных,
        # учитывая относительные пути и к какой папке обращен терминал.
        self.cursor = self.con.cursor()
        self.create_users_table()

        # Создаем словарь, в который после внесем все данные из полей
        self.context = {}
        # Получим текущую дату и время
        self.currentDate = datetime.datetime.now()

        # Связываем кнопки с соответствующими методами.
        self.saveBtn.clicked.connect(self.save_info)
        self.resetBtn.clicked.connect(self.reset_fields)

    # Метод, создающий базу данных
    def create_users_table(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_fio TEXT,
                user_bio TEXT,
                user_edu TEXT,
                user_birth TEXT,
                user_reg_date TEXT
            );
            ''')
        self.con.commit()

    # Метод, вызываемый при нажатии на кнопку сохранения информации в БД
    def save_info(self):
        self.get_data()
        self.save_to_db()
        self.saveBtn.setText('Пользователь сохранен')
        self.saveBtn.setStyleSheet('background-color: green')

    # Метод, считывающий данные из полей в словарь self.context
    # Данные оттуда после будут перенесены в БД
    def get_data(self):
        self.context = {
            'user_fio': self.userFio.text(),
            'user_bio': self.userBio.toPlainText(),
            'user_edu': self.selectEducation.currentText(),
            'user_birth': self.userBirth.dateTime().toString('dd.MM.yyyy'),
            'user_reg_date': self.currentDate.strftime('%d.%m.%Y %H:%M:%S')
        }

    # Метод, сохраняющий данные из self.context в базу данных
    def save_to_db(self):
        query = (
            """
            INSERT INTO users(
                user_fio,
                user_bio,
                user_edu,
                user_birth,
                user_reg_date
            )
            VALUES(?, ?, ?, ?, ?);
            """
        )
        user_data = (
            self.context['user_fio'],
            self.context['user_bio'],
            self.context['user_edu'],
            self.context['user_birth'],
            self.context['user_reg_date'],
        )
        self.cursor.execute(query, user_data)
        self.con.commit()

    # Метод, очищающий поля формы - вызывается при нажатии на кнопку
    def reset_fields(self):
        self.userFio.clear()
        self.userBio.clear()
        self.selectEducation.setCurrentIndex(0)
        self.userBirth.setDate(QDate.fromString('01.01.2000', 'dd.MM.yyyy'))
        self.saveBtn.setText('Сохранить пользователя')
        self.saveBtn.setStyleSheet('background-color: white')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = MyWidget()
    mainWidget.show()
    sys.exit(app.exec_())
