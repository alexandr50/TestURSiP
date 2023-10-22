import pandas as pd
from datetime import date, timedelta
from random import randint


def get_random_date():
    """Функция генерирует рандомню дату"""

    start, end = date(2022, 1, 1), date(2022, 12, 31)
    delta = end - start
    return start + timedelta(randint(0, delta.days))


def parse_table(path: str):
    """Функция парсит excel и создает объект DataFrame"""

    df = pd.read_excel(path, header=[0, 2], engine='openpyxl')

    df.columns = [
        'id',
        'company',
        'fact_qliq_data1',
        'fact_qliq_data2',
        'fact_qoil_data1',
        'fact_qoil_data2',
        'forecast_qliq_data1',
        'forecast_qliq_data2',
        'forecast_qoil_data1',
        'forecast_qoil_data2'
    ]
    data = df.drop(columns=['id'])
    return data
