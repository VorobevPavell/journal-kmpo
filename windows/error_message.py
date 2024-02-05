from PySide6.QtWidgets import QMessageBox


# окна для сообщений пользователю
def show_error_message(self, title, message):
    """
    Сообщает об ошибке
    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()


def success_message(self, title, message):
    """
    Сообщает об успешном выполнении чего-либо
    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()


def show_error(title, message):
    """
    Сообщает об ошибке, передаем не в класс
    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()


def success_message_(title, message):
    """
    Сообщает об успешном выполнении чего-либо
    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()