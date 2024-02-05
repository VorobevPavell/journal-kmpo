from student_window_UI import Ui_Form
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from database.database_connect import session
from database.models import Schedule, Group


# окно с информацией для студента
class StudentWindow(QWidget):
    def __init__(self, group):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # запрос к БД для получения информации о преподавателях и дисциплинах
        query = session.query(Schedule.subject_name, Schedule.teacher_name, Group.id).distinct().join(Group).filter(
            Group.name == group)

        row_count = len(list(query))
        self.ui.tableWidget.setRowCount(row_count)

        # заполняем таблицу
        for i, subjects in enumerate(query):
            if str(subjects.subject_name).split()[-1] != 'урока)':
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(subjects.subject_name)))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(subjects.teacher_name)))
            else:
                row_count -= 1
                self.ui.tableWidget.setRowCount(row_count)

        self.ui.tableWidget.resizeColumnsToContents()