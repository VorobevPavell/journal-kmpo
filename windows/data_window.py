from windows.data_window_UI import Ui_Form
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from error_message import show_error_message
from database.database_connect import session
from database.models import Schedule, Group


# окно с информацией о всех занятиях в колледже
class DataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.hide()
        self.ui.res_button.clicked.connect(self.res)
        self.resize(267, 397)

        # создаем список всех групп и добавляем группы на форму
        group_list = list(session.query(Group.name).all())
        for g in group_list:
            self.ui.comboBox.addItem(str(g)[2:-3])

    # функция для фильтрации данных о занятиях
    def res(self):
        self.resize(981, 397)
        date_from = self.ui.date_from.dateTime().toPython()
        date_to = self.ui.date_to.dateTime().toPython()

        # проверка на корректность введенной даты
        if date_from > date_to:
            show_error_message(self, "Неверный интервал даты", "Введите корректные значения даты!")

        combobox_group = self.ui.comboBox.currentText()

        # поиск группы, выбранной пользователем в БД
        filtered_group = session.query(Group.id).filter(Group.name == combobox_group)
        filtered_group = filtered_group.one()

        # поиск занятий в колледже за определенную дату
        result = session.query(Schedule).filter(Schedule.group_id == int(str(filtered_group)[1:-2]),
                                                Schedule._date >= date_from, Schedule._date <= date_to)

        self.ui.tableWidget.setRowCount(result.count())
        for i, row in enumerate(result):
            # Создаем ячейки таблицы и заполняем их значениями
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(row._date)[:10]))
            query = session.query(Group.name).filter(Group.id == row.group_id)
            group = query.one()
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(group)[2:-3]))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(row.subject_name)))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(row.teacher_name)))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(row.num)))

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.show()
