from admin_window_UI import Ui_Form
from PySide6.QtWidgets import QWidget
from sign_up_window import SignUp
from data_window import DataWindow
from admin_teacherData_window import AdminTeacherDataWindow
from funcs.request import _request

# окно администратора
class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.signUpButton.clicked.connect(self.get_sign_up)
        self.ui.get_data_button.clicked.connect(self.open_data_window)
        self.ui.teacher_button.clicked.connect(self.open_admin_teacherData_window)
        self.ui.update_database_button.clicked.connect(_request)

    # направляем админа в окно регистрации пользователей
    def get_sign_up(self):
        window = SignUp()
        window.show()
        window.exec()

    # направляем админа в окно Получить данные о занятиях
    def open_data_window(self):
        window = DataWindow()
        window.show()
        window.exec()

    # направляем админа в окно с информацией о преподавателях
    def open_admin_teacherData_window(self):
        window = AdminTeacherDataWindow()
        window.show()
        window.exec()
