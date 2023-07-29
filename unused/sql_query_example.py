# Пример простого запроса к базе

import sqlite3

connection = sqlite3.connect(r'C:\Users\Vadim\PycharmProjects\DjangoProjects\365_kpi_web\db.sqlite3')
cursor = connection.cursor()
cursor.execute("SELECT first_link FROM kpiapp_update WHERE id=(SELECT max(id) FROM kpiapp_update)")
res = cursor.fetchone()
connection.commit()
connection.close()

print(res[0])
