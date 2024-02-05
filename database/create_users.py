from database_connect import session
from models import AuthData

# дефолтные пользователи для теста ролей
admin = AuthData(login="admin", password="admin", role_id=3)
teacher = AuthData(login="teacher", password="teacher", role_id=1)
student = AuthData(login="student", password="student", role_id=2)


# добавляем пользователей в БД
session.add(admin)
session.add(teacher)
session.add(student)
session.commit()
