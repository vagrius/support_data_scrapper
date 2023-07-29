# Проверка возможности работы с БД напрямую

import sqlite3

import datetime

connection = sqlite3.connect(r'C:\Users\Vadim\PycharmProjects\DjangoProjects\365_kpi_web\db.sqlite3')
cursor = connection.cursor()

# cursor.execute("""INSERT INTO kpiapp_request
#                   VALUES (Null,
#                           '2021-07-30 12:35:00',
#                           'Моисеенко Анатолий',
#                           'Добрый день! у вас есть интеграция с amocrm? или api?  ...',
#                           '[2.17]',
#                           2.29,
#                           1,
#                           1,
#                           0,
#                           2.17,
#                           'Blank Company',
#                           'Зорина Ирина',
#                           '5d44732a-a129-402c-afee-afb7acbd180c')""")

date_time = str(datetime.datetime.now())[:-7]

cursor.execute("INSERT INTO kpiapp_update VALUES (Null, ?)", (date_time,))

connection.commit()

connection.close()
