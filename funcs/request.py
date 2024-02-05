import datetime
import traceback
import requests
from windows.error_message import show_error, success_message_
from database.database_connect import session
from database.models import Group, Schedule, Subject, Teacher
from funcs.date_formatter import get_date, date_formatting
from sqlalchemy import func


def _request():
    # получаем последнюю дату в БД, если БД пустая, то начальная дата - 20240112
    date_from = session.query(func.max(Schedule._date)).scalar()
    session.commit()
    if date_from is None:
        date_from = "20240112"
    else:
        date_from = date_formatting(str(date_from)[:10])

    date_to = date_formatting(str(datetime.date.today() - datetime.timedelta(days=1)))
    # список для записи в него групп
    group_list = []

    url = 'https://kmpo.eljur.ru/api'

    # словарь, в котором хранятся параметры по-умолчанию, которые необходимы
    # для любых запросов
    default_params = {
        'devkey': 'djxtosyvney4is87fyycnepl2x91zger',
        'vendor': 'kmpo',
        'out_format': 'json',
        'auth_token': '3173df46b1ac8e40ca81b5d22b315c28079088633af08b825f64a77998dc8___30917'
    }

    with session.begin():
        try:
            # get-запрос на сервер
            resp = requests.get(url + '/getrules', params=default_params)
            # запись ответа от сервера в формате json
            study_plan = resp.json()
            groups = study_plan['response']['result']['relations']['groups']

            # добавляем группы в БД
            for key in groups:
                group_list.append(key)
                # если группы нет в БД, добавляем
                group = session.query(Group).filter_by(name=key).first()
                if not group:
                    g = Group(name=key)
                    session.add(g)

            for i in range(len(group_list)):
                params = {
                    **default_params,
                    'class': group_list[i],
                    'days': get_date(date_from, date_to)
                }


                # запрос на сервер
                res = requests.get(url + '/getschedule', params=params)
                days = res.json()
                schedule = days['response']['result']['days']

                for key, value in schedule.items():
                    date = key
                    gr_id = session.query(Group.id).filter(Group.name == group_list[i]).scalar_subquery()
                    if 'items' not in value:
                        continue

                    # заполнение БД
                    for item in value['items']:
                        subject = item['name']
                        vsubject = session.query(Subject).filter_by(name=subject).first()
                        if not vsubject:
                            s = Subject(name=subject)
                            session.add(s)

                        teacher = item['teacher']
                        cteacher = session.query(Teacher).filter_by(name=teacher).first()
                        if not cteacher:
                            t = Teacher(name=teacher)
                            session.add(t)
                        number = item['num']

                        d = Schedule(
                            _date=date,
                            num=number,
                            group_id=gr_id,
                            teacher_name=teacher,
                            subject_name=subject
                        )
                        session.add(d)
            success_message_(f"Обновление выполнено", f"Загрузка данных прошла успешно!")

        except Exception as err:
            traceback.print_exc()
            session.rollback()
            success_message_(f"{err}", f"Не удалось получить данные!")