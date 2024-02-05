from database_connect import session
from models import Role


# роли, которые могут быть у пользователей
roles = ['Преподаватель', 'Студент', 'Администратор']

# добавляем в бд роли
for role in range(len(roles)):
    obj = Role(name=roles[role])
    session.add(obj)

# сохраняем изменения
session.commit()
