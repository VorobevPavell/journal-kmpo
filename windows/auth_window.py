import sys
from admin_window import AdminWindow
from teacher_window import TeacherWindow
from student_window import StudentWindow
from database.database_connect import session
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QComboBox
from auth_window_UI import Ui_MainWindow
from database.models import AuthData, Role
from error_message import show_error_message, success_message


# окно авторизации в приложении
class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sign_in_button.clicked.connect(self.get_auth)

    # функция авторизации
    def get_auth(self):
        # получаем данные, которые ввел пользователь
        login_label = window.findChild(QLineEdit, "login_lineEdit")
        login = login_label.text()

        passw_label = window.findChild(QLineEdit, "password_lineEdit")
        passw = passw_label.text()

        user_role = window.findChild(QComboBox, "role_comboBox")
        _role = user_role.currentText()

        # запрос к БД, результат - все зарегистрированные пользователи
        _users = session.query(AuthData.login, AuthData.password, Role.name).join(Role).filter(Role.name == _role).all()
        match _role:
            case "Администратор":
                new_window = AdminWindow()
            case "Преподаватель":
                new_window = TeacherWindow(login)
            case "Студент":
                group = login.split()[-1]
                new_window = StudentWindow(group)

        # проверка на корректность введенных данных
        success = 0
        for r in _users:
            if login == r.login and passw == r.password and _role == r.name:
                success = 1
                success_message(self, "Успешная авторизация",
                                   "Добро пожаловать в журнал КМПО!")
                self.close()
                new_window.show()
                new_window.exec()

        if not success:
            show_error_message(self, "Ошибка авторизации",
                                    "Укажите верные данные или обратитесь к администратору.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec())
