from requests import get
import datetime
from datetime import date
from datetime import timedelta
import json

delta1 = timedelta(days=1)
delta8 = timedelta(days=8)
delta15 = timedelta(days=15)

today = datetime.date.today()
yesterday = today - delta1
week = today - delta8
fortnight = today - delta15


def connection(date):
    endpoint = (
            'https://api.coronavirus.data.gov.uk/v1/data?'
            'filters=areaType=nation;date=' + date.strftime("%Y-%m-%d") + ';areaName=england&'
                                                                          'structure={"date":"date","CasesXYZ":"cumCasesByPublishDate","NewXYZ":"newCasesByPublishDate","DeathsXYZ":"newDeaths28DaysByPublishDate"}'
    )

    response = get(endpoint, timeout=10)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: {response.text}')

    return response.json()


def get_cum_cases(date):
    data = json.dumps(connection(date))

    A = data.index("CasesXYZ")
    B = data.index("NewXYZ")
    output = int(data[A + 11:B - 3])
    return output


def get_new_cases():
    date = yesterday
    data = json.dumps(connection(date))

    A = data.index("NewXYZ")
    B = data.index("DeathsXYZ")
    output = int(data[A + 9:B - 3])
    return output


def get_new_deaths():
    date = yesterday
    data = json.dumps(connection(date))

    A = data.index("DeathsXYZ")
    B = data.index("}],")
    output = int(data[A + 12:B])
    return output


def percent_change():
    yesterday2 = get_cum_cases(yesterday)
    week_ago = get_cum_cases(week)
    fortnight_ago = get_cum_cases(fortnight)

    d1 = yesterday2 - week_ago
    d2 = week_ago - fortnight_ago

    p_change = (d1 / d2) - 1
    return p_change


def data_test(date):
    data = connection(date)
    # print(data)
    ccases = get_cum_cases(date)
    print(ccases)
    ncases = get_new_cases()
    print(ncases)
    dcases = get_new_deaths()
    print(dcases)
    pchange = percent_change()
    print(pchange)