from teacher_window_UI import Ui_Form
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from database.database_connect import session
from database.models import Schedule, Group
from sqlalchemy import func


# окно с информацией для учителя
class TeacherWindow(QWidget):
    def __init__(self, login):
        self.login = login
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # получаем информацию о  проведенных занятиях у учителя для каждой группы
        query = session.query(Schedule.subject_name,
                               Group.name,
                               func.count(Schedule.subject_name).label('hours')). \
            join(Group). \
            group_by(Schedule.subject_name,
                     Group.name). \
            filter(Schedule.teacher_name == self.login)

        self.ui.tableWidget.setRowCount(len(list(query)))

        # заполняем таблицу
        for i, task in enumerate(query):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(task.subject_name)))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(task.name)))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(task.hours)))

        self.ui.tableWidget.resizeColumnsToContents()
