import json
import requests


# для хранения названия групп
group_list: list = []
days_list: list = []
# дни, по которым нужно получить данные (вводятся в формате ГГГГММДД)
print('Введите дату, начиная с которой нужно получить данные: ГГГГММДД\n')
days_from: str = input()
print('Введите дату, заканчивая которой нужно получить данные: ГГГГММДД\n')
days_to: str = input()
print('\n')


def get_date(days_from: str, days_to: str) -> str:
    '''Формирует строку для передачи в параметры к запросу'''
    return f'{days_from}-{days_to}'


def get_data(group_list: list[str]):
    '''Основная логика программы

    Принимает в аргументы пустой список, в который будут записаны названия групп'''
    with open('result.txt', 'w', encoding='utf_8') as result_file:
        result_file.write(f'Данные c {days_from} по {days_to}\n')
        result_file.write(f'Формат даты: ГГГГММДД\n')

        url = 'https://kmpo.eljur.ru/api'
        # словарь, в котором хранятся параметры по-умолчанию, которые необходимы
        # для любых запросов
        default_params = {
            'devkey': 'djxtosyvney4is87fyycnepl2x91zger',
            'vendor': 'kmpo',
            'out_format': 'json',
            'auth_token': '3173df46b1ac8e40ca81b5d22b315c28079088633af08b825f64a77998dc8___30917'
            }
        try:
            # get-запрос на сервер
            resp = requests.get(url + '/getrules', params= default_params)
            # запись ответа от сервера в формате json
            study_plan = resp.json()
            groups = study_plan['response']['result']['relations']['groups']

            # создаем список всех групп
            for key in groups:
                group_list.append(key)

            for i in range(len(group_list)):
                params = {
                                **default_params,
                                'class': group_list[i],
                                'days': get_date(days_from, days_to)
                            }

                # запрос на сервер
                res = requests.get(url + '/getschedule', params= params)
                days = res.json()
                schedule = days['response']['result']['days']
                # запись результатов в файл
                result_file.write(f'Группа : {group_list[i]}')
                # json.dumps возвращает строку, преобразованную к благоприятному для чтения виду из json
                result_file.write(json.dumps(schedule, indent=4, ensure_ascii=False))
                result_file.write(f'\nДанные по группе {group_list[i]} получены !\n')
        except Exception as err:
            result_file.write(f'Данные не удалось получить в связи с ошибкой: {err}')


