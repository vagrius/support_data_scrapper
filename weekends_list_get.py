# модуль получения базового списка выходных дней

import calendar
import csv


def get_weekends_general_list(y):
    cal = calendar.Calendar()  # получаем список выходных дней
    weekends_general_list = []
    for m in range(1, 13):
        for x in cal.itermonthdates(y, m):
            if x.isoweekday() in (6, 7):
                weekends_general_list.append(str(x))  # для запись в csv - [str(x)]

    # with open(f'data\\weekends_{y}.csv', 'w', newline='') as f:  # записываем его в файл
    #     writer = csv.writer(f)
    #     for row in weekends_general_list:
    #         writer.writerow(row)

    # return weekends_general_list


print(get_weekends_general_list(2021))
