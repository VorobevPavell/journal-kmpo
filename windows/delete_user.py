from delete_user_window_UI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from database.database_connect import session
from database.models import AuthData
from error_message import success_message


class DeleteUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.delete_push_button.clicked.connect(self.del_usr)

        # добавить пользователей в список на форме
        users = session.query(AuthData.login).all()
        for r in users:
            self.ui.user_list_widget.addItem(*r)

    # удалить выбранного пользователя
    def del_usr(self):
        index = self.ui.user_list_widget.currentRow()
        removed = self.ui.user_list_widget.takeItem(index)
        user = removed.text()
        removed = session.query(AuthData).filter(AuthData.login == user).one()
        session.delete(removed)
        session.commit()
        success_message(self, "Успешно!",
                        f"Пользователь {user} удален")
