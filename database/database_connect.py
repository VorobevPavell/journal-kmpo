from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# создание движка и подключение к БД
engine = create_engine('mysql+pymysql://root:root@localhost/kmpo_journal', echo=True)
engine.connect()


# создание класса и экземпляра класса сессии
session = Session(bind=engine)

