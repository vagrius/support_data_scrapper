from datetime import datetime, timedelta
import re


# преобразование даты и времени к стандартному виду
def string_to_datetime(d, t):
    dic = {'января': '01',
           'февраля': '02',
           'марта': '03',
           'апреля': '04',
           'мая': '05',
           'июня': '06',
           'июля': '07',
           'августа': '08',
           'сентября': '09',
           'октября': '10',
           'ноября': '11',
           'декабря': '12'
           }
    lst = d.split()
    string_out = f"{lst[2]}-{dic[lst[1]]}-{(lambda x: '0' + x if len(x) == 1 else x)(lst[0])} " \
                 f"{(lambda x: '0' + x if len(x) == 4 else x)(t)}:00.00000"
    return string_out


# расчет времени реакции
def reaction_time(datetime1, datetime2):

    if datetime1 == '':
        datetime1 = datetime2

    def nonworking_hours(dt):  # если время нерабочее, для корректного расчет приводим к нужному виду
        if dt[11:] < '09:00:00.00000':
            return dt[:10] + ' 09:00:00.00000'
        elif dt[11:] > '18:00:00.00000':
            return dt[:10] + ' 18:00:00.00000'
        else:
            return dt

    dt1 = datetime.strptime(nonworking_hours(datetime1), "%Y-%m-%d %H:%M:%S.%f")
    dt2 = datetime.strptime(nonworking_hours(datetime2), "%Y-%m-%d %H:%M:%S.%f")

    # print(f'{str(dt1)}   {str(dt2)}')

    if dt2.day - dt1.day == 0:  # если сообщения в один день

        delta = dt2 - dt1
        delta_in_hours = round(abs(delta.days) * 24 + delta.seconds / 3600, 2)
        if datetime1[11:] < '12:30:00.00000' and datetime2[11:] > '13:30:00.00000':  # учитываем обеденное время
            delta_in_hours -= 1.0

    else:  # если сообщения в разные дни

        buffer_day = dt1.date()  # считаем, есть ли выходные между двумя датами
        weekend_count = 0
        while buffer_day < dt2.date():
            buffer_day += timedelta(days=1)
            if buffer_day == dt2.date():
                break
            if is_weekend(str(buffer_day)):
                weekend_count += 1

        sub_delta0 = ((dt2 - dt1).days - weekend_count) * 8  # дельта в рабочих часах между датами

        work_day_end = datetime1[:10] + ' 18:00:00.00000'  # дельты по каждой дате
        if is_weekend(str(dt1.date())):
            sub_delta1 = 0
        else:
            sub_delta1 = reaction_time(datetime1, work_day_end)

        work_day_start = datetime2[:10] + ' 09:00:00.00000'
        if is_weekend(str(dt2.date())):
            sub_delta2 = 0
        else:
            sub_delta2 = reaction_time(work_day_start, datetime2)

        delta_in_hours = round(sub_delta0 + sub_delta1 + sub_delta2, 2)  # складываем все дельты

    return round(delta_in_hours, 2)


# удаление из текста нежелательных символов - эмодзи и символов переноса строки
def unacceptable_chars_delete(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u'\U00010000-\U0010ffff'
                               u"\u200d"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\ufe0f"
                               u"\u0306"
                               "]+", flags=re.UNICODE)
    new_string = emoji_pattern.sub(r'', string)
    new_string = re.sub(r'[\n\r]', ' ', new_string)  # символы переноса строк
    return new_string


# является ли пользователь клиентом
def is_client(username):
    specs_list = [
        'Главный Оператор',
    ]
    if username not in specs_list:
        return True
    return False


# является ли день выходным
def is_weekend(day):
    weekend_base_list = []
    weekend_add_list = []
    if day in weekend_base_list or day in weekend_add_list:
        return True
    else:
        return False
