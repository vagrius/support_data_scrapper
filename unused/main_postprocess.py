# Дозапись в файл с запросами вычисляемых колонок
# Устаревший скрипт, теперь все происходит разом в основном скрипте

# import csv
#
#
# def add_calc_fields_to_csv():
#     # функция дозаписи в csv файл вычисляемых полей
#
#     new_list = []
#
#     with open('data\\requests\\requests_2021-07.csv') as f:
#         reader = csv.reader(f, delimiter=';')
#         for row in reader:
#             if row:
#
#                 row[5] = row[5].replace(',', '.')
#
#                 if float(row[5]) <= 16.0:  # decision in time
#                     row.append(1)
#                 else:
#                     row.append(0)
#
#                 row.append(len(row[4][1:-1].split(',')))  # reactions count
#
#                 r_c = 0
#                 for r in row[4][1:-1].split(','):
#                     if r != '':
#                         if float(r) <= 2.0:
#                             r_c += 1
#                 row.append(r_c)  # reactions in time count
#
#                 row.append(round(float(row[5]) / row[8], 2))  # reactions average
#
#                 print(row)
#
#                 new_list.append(row)
#
#     with open('data\\requests\\requests_2021-07_.csv', 'w', newline='') as f:
#         writer = csv.writer(f, delimiter=';')
#         for row in new_list:
#             writer.writerow(row)
#
#
# add_calc_fields_to_csv()
