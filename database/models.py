from database.database_connect import engine
from sqlalchemy import MetaData, String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase


metadata = MetaData()


# датакласс для создания таблиц наследованием от него
class Base(DeclarativeBase):
    pass


# таблица с возможными ролями пользователей
class Role(Base):
    __tablename__ = 'role'

    id = Column('id', Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column('name', String(15), nullable=False)


# таблица с данными для авторизации
class AuthData(Base):
    __tablename__ = 'auth'

    id = Column('id', Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    login = Column('login', String(100), unique=True)
    password = Column('passphrase', String(50))
    role_id = Column('role_id', ForeignKey("role.id"), index=True)


# таблица для хранения названия предметов
class Subject(Base):
    __tablename__ = 'subject'

    id = Column('id', Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column('name', String(150), nullable=False, unique=True)


# ФИО преподавателей
class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column('id', Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column('name', String(100), nullable=False)


# таблица для хранения названия групп
class Group(Base):
    __tablename__ = 'group'

    id = Column('id', Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column('name', String(15))


# таблица для хранения информации о расписании
class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column('id', Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    _date = Column('_date', DateTime())
    num = Column('num', Integer)
    group_id = Column('group_id', ForeignKey('group.id'))
    teacher_name = Column('teacher_name', String(150))
    subject_name = Column('subject_name', String(150))


# создание таблиц
Base.metadata.create_all(bind=engine)
#Base.metadata.drop_all(bind=engine)
