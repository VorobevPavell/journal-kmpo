from admin_teacherData_window_UI import Ui_Form
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from database.database_connect import session
from database.models import Teacher, Group, Subject, Schedule


# окно с информацией об отработанных часах преподавателей
class AdminTeacherDataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.hide()
        self.ui.res_button.clicked.connect(self.teacher_query)
        self.ui.select_teacher_pushButton.clicked.connect(self.submit_teacher)
        self.ui.select_subject_pushButton.clicked.connect(self.submit_subject)
        self.resize(365, 398)

        # получаем список всех учителей и добавляем их на форму
        teachers = list(session.query(Teacher.name).order_by(Teacher.name).all())
        for teacher in teachers:
            self.ui.teacher_comboBox.addItem(str(teacher)[2:-3])

        # получаем список всех предметов и добавляем их на форму
        subjects = list(session.query(Subject.name).all())
        for s in subjects:
            self.ui.subject_comboBox.addItem(str(s)[2:-3])

    # функция-обработчик выбранного учителя
    def submit_teacher(self):
        self.ui.subject_comboBox.clear()
        teacher = self.ui.teacher_comboBox.currentText()

        # добавляем на форму список предметов, которые преподает выбранный учитель
        teachers_subject = session.query(Schedule.subject_name).group_by(Schedule.subject_name).filter(Schedule.teacher_name == teacher)
        for subject in teachers_subject:
            self.ui.subject_comboBox.addItem(subject.subject_name)

        self.ui.group_comboBox.clear()
        self.ui.group_comboBox.addItem('Все')
        # получаем группы, которым преподает учитель и добавляем их на форму
        group_from_id = list(session.query(Group.name).distinct().join(Schedule).filter(Schedule.teacher_name == teacher))
        for g in group_from_id:
            self.ui.group_comboBox.addItem(str(g)[2:-3])

    def teacher_query(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderLabels(['Преподаватель', 'Группа', 'Дисциплина', 'Часов'])
        teacher = self.ui.teacher_comboBox.currentText()
        group = self.ui.group_comboBox.currentText()
        current_subject = self.ui.subject_comboBox.currentText()
        if group != 'Все':
            id_group = session.query(Schedule.group_id).join(Group).filter(Group.name == group)
            for i in id_group:
                gr_id = i.group_id
            # количество часов, которые отработал преподаватель у каждой группы
            hours = session.query(Schedule).filter(Schedule.teacher_name == teacher,
                                                   Schedule.subject_name == current_subject,
                                                   Schedule.group_id == gr_id).count()
            # заполняем таблицу
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(teacher)))
            self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(group)))
            self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(current_subject)))
            self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(str(hours)))
            self.resize(979, 398)
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.show()
        else:
            groups = session.query(Schedule.teacher_name, Group.name, Schedule.subject_name, Schedule.group_id).distinct().join(Schedule).filter(
                Schedule.teacher_name == teacher,
                Schedule.subject_name == current_subject
            )

            self.ui.tableWidget.setRowCount(len(list(groups)))
            for j, data in enumerate(groups):
                hours = session.query(Schedule).filter(Schedule.teacher_name == teacher,
                                                       Schedule.subject_name == current_subject,
                                                       Schedule.group_id == data.group_id).count()
                self.ui.tableWidget.setItem(j, 0, QTableWidgetItem(str(data.teacher_name)))
                self.ui.tableWidget.setItem(j, 1, QTableWidgetItem(str(data.name)))
                self.ui.tableWidget.setItem(j, 2, QTableWidgetItem(str(data.subject_name)))
                self.ui.tableWidget.setItem(j, 3, QTableWidgetItem(str(hours)))
                self.resize(979, 398)
                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.show()

    def submit_subject(self):
        self.ui.group_comboBox.clear()
        teacher = self.ui.teacher_comboBox.currentText()
        subject = self.ui.subject_comboBox.currentText()

        query = session.query(Group.name).distinct().join(Schedule).filter(Schedule.subject_name == subject,
                                                                Schedule.teacher_name == teacher)

        for g in query:
            self.ui.group_comboBox.addItem(g.name)

