# Программа, создающая простое приложение на PyQt5
# Функционал приложения - кнопка, при нажатии на которую меняется текст поля.
import sys

# Импортируем из библиотеки PyQt5, модуля QtWidgets два класса:
# QApplication - отвечает за ход выполнения приложения и основные настройки.
# QMainWindow - это главное окно приложения.
from PyQt5.QtWidgets import QApplication, QMainWindow
# uic - модуль для работы с файлами интерфейса формата .ui
# Мы эти файлы создаем в редакторе QtDesigner.
from PyQt5 import uic


# Создается класс-наследник QMainWindow для расширения базового функционала
# главного окна приложения.
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загружаем созданный нами интерфейс simple_app.ui
        uic.loadUi('ui/simple_app.ui', self)

        # Создаем событие нажатия на кнопку pushButton,
        # связав клик по ней с методом run_button
        self.pushButton.clicked.connect(self.run_button)

    # Описание метода, вызывааемого при нажатии на кнопку.
    def run_button(self):
        self.pushButton.setText('Нажали')
        self.label.setText('ДА')


# Исполняемая часть программы
if __name__ == '__main__':
    # Создается объект приложения
    app = QApplication(sys.argv)

    # Создается объект главного окна приложения
    mainWidget = MyWidget()

    # Вызывается команда на отрисовку главного окна.
    mainWidget.show()

    # Запускается само приложение через команду app.exec_().
    # При закрытии окна приложения завершается исполнение
    # всей нашей программы через sys.exit()
    sys.exit(app.exec_())
