from sign_up_window_UI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QLineEdit, QComboBox
from database.database_connect import session
from database.models import AuthData, Role
from delete_user import DeleteUser
from error_message import show_error_message, success_message


# окно для регистрации новых пользователей, доступ только у админов
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sign_up_button.clicked.connect(self.sign_up)
        self.ui.delete_user_button.clicked.connect(self.delete_user)

    def sign_up(self):
        """
        Логика регистрации и удаления пользователей
        """
        # получаем данные пользователя
        login_label = self.findChild(QLineEdit, "login_lineEdit")
        login = login_label.text()
        passw_label = self.findChild(QLineEdit, "password_lineEdit")
        passw = passw_label.text()
        user_role = self.findChild(QComboBox, "role_comboBox")
        _role = user_role.currentText()

        role = session.query(Role).filter_by(name=_role).first()

        user = AuthData(
            login=login,
            password=passw,
            role_id=role.id
        )
        # регистрируем только в случае не пустых строк
        if login and passw:
            session.add(user)
            session.commit()
            success_message(self, "Успешная регистрация",
                            f"Пользователь {user.login} - новый {_role}!")


        # ошибка регистрации
        else:
            show_error_message(self, "Ошибка регистрации", "Введите логин и пароль, укажите нужную роль")

    def delete_user(self):
        window = DeleteUser()
        window.show()
        window.exec()






