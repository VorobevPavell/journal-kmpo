def date_formatting(date: str) -> str:
    """
    Принимает дату в виде строки формата ГГГГ-ММ-ДД

    """
    return f"{date[:4]}{date[5:7]}{date[8:10]}"


def get_date(days_from: str, days_to: str) -> str:
    """
    Формирует строку для передачи в параметры к запросу
    """
    return f'{days_from}-{days_to}'
