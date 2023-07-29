"""
Устаревший главный модуль, для работы с линиями.
"""


# import csv
# import datetime
# import sqlite3
# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
#
# from aux_functions import string_to_datetime, is_client, reaction_time, unacceptable_chars_delete
# from global_settings import webdriver_mode_off, login_page_force
#
# REQUESTS_PATH = r'C:\Users\Vadim\PycharmProjects\ScrapMachine\data\requests.csv'
# CLIENTS_PATH = r'C:\Users\Vadim\PycharmProjects\ScrapMachine\data\clients.csv'
#
#
# def chat_parsing(url, driver):
#
#     list_global = []
#
#     try:
#         driver.get(url)
#         time.sleep(3)
#
#         login_page_force(driver)
#
#         WebDriverWait(driver, 600).until(ec.visibility_of_element_located((By.CLASS_NAME, 'chat')))
#
#         dts = driver.find_elements_by_css_selector('.chat > .chat__date')
#         org_nm = driver.find_element_by_css_selector('.page-header__title .title').text[:-19]
#         cht = driver.find_element_by_css_selector('.chat')
#         message_groups = cht.find_elements_by_css_selector('.chat > app-chat-message-group')
#
#         for i in range(len(dts)):
#             dt = dts[i].text
#             message_stacks = message_groups[i].find_elements_by_css_selector('.chat-message-stack')
#             for j in range(len(message_stacks)):
#                 try:
#                     usr = message_stacks[j].find_element_by_css_selector('.user-name-block').text
#                 except Exception:
#                     usr = 'System'
#                 msgs = message_stacks[j].find_elements_by_css_selector('.chat-message__text-inner')
#                 tms = message_stacks[j].find_elements_by_css_selector('.chat-message__time')
#                 for k in range(len(msgs)):
#                     if tms[k].text != '':
#                         tm = tms[k].text
#                     msg = unacceptable_chars_delete(str(msgs[k].text[:81] + '...'))
#                     actual_dt_tm = string_to_datetime(dt, tm)
#                     new_list = [actual_dt_tm, org_nm, usr, msg]
#                     if usr != 'System':
#                         list_global.append(new_list)
#
#     except Exception as ex:
#         print(f'Не удалось обработать ссылку. Возникла ошибка: {ex}')
#         list_global = []
#     finally:
#         return list_global
#
#
# def get_requests_data(uid, line, chat_strings_list):
#     request = []
#     client_message_time = ''
#     spec_message_time = ''
#
#     try:
#         for i in range(0, len(chat_strings_list)):
#
#             # print(chat_strings_list[i])  # вывод чата в консоль
#
#             """
#             В этом блоке вычисляем основные показатели по запросу, записываем их в список
#             """
#             if i == 0:
#                 request = chat_strings_list[i]  # время 1-го сообщения [0] - орг-я [1] - имя [2] - первое сообщение [3]
#                 request.append([])  # список реакций [4]
#                 request.append(0)  # время решения [5]
#             if is_client(chat_strings_list[i][2]) and client_message_time == '':  # здесь будем считать время реакции
#                 client_message_time = chat_strings_list[i][0]
#                 spec_message_time = ''
#             if not is_client(chat_strings_list[i][2]):
#                 if spec_message_time == '' and client_message_time != '':
#                     spec_message_time = chat_strings_list[i][0]
#                     request[4].append(reaction_time(client_message_time, spec_message_time))
#                     request[5] += request[4][-1]  # инкрементим время решения
#                     if len(request) == 6:  # заодно определим специалиста [6]
#                         request.append(chat_strings_list[i][2])
#                     client_message_time = ''
#                 else:  # учитываем во времени решения, что спец мог ответить несколько раз
#                     request[5] += reaction_time(spec_message_time, chat_strings_list[i][0])
#                     spec_message_time = chat_strings_list[i][0]
#
#         """
#         Вычисляем вспомогательные показатели для вывода в веб
#         """
#         if request[5] <= 16.0:  # decision in time (признак, решено ли вовремя) [7]
#             request.append(1)
#         else:
#             request.append(0)
#
#         request.append(len(request[4]))  # reactions count (количество реакций) [8]
#
#         r_c = 0  # reactions in time count (количество реакций вовремя) [9]
#         for r in request[4]:
#             if r != '':
#                 if r <= 2.0:
#                     r_c += 1
#         request.append(r_c)
#
#         request.append(round(sum(request[4]) / request[8], 2))  # reactions average (ср. время реакции) [10]
#
#         request.append(uid)  # uid чата [11]
#         request.append(line)  # линия [12]
#
#     except Exception as ex:
#         print(f'Не удалось получить запросы из чата. Возникла ошибка: {ex}')
#         request = []
#
#     finally:
#         return request
#
#
# if __name__ == "__main__":
#
#     list_of_links = []
#     new_list_of_links = []
#
#     with open(CLIENTS_PATH) as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if row:
#                 list_of_links.append(row)
#
#     count = 0
#
#     wdriver = webdriver_mode_off()
#
#     connection = sqlite3.connect(r'C:\Users\Vadim\PycharmProjects\DjangoProjects\365_kpi_web\db.sqlite3')
#     cursor = connection.cursor()
#
#     with open(REQUESTS_PATH, 'a', newline='') as f:
#         writer = csv.writer(f, delimiter=';')
#         for link in list_of_links:
#             if link[2] == 'closed':
#                 link_full = 'https://support.elma365.ru/_lines/' + link[0]
#                 print(f'Обработка ссылки #{count}: {link_full}')
#                 requests_data = get_requests_data(link_full[34:], link[3], chat_parsing(link_full, wdriver))
#                 if requests_data:
#                     writer.writerow(requests_data)  # пишем данные в csv-файл
#                     # также пишем данные в БД
#                     cursor.execute("INSERT INTO kpiapp_request VALUES (Null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
#                         str(requests_data[0][:-6]),
#                         str(requests_data[2]),
#                         str(requests_data[3]),
#                         str(requests_data[4]),
#                         requests_data[5],
#                         requests_data[7],
#                         requests_data[8],
#                         requests_data[9],
#                         requests_data[10],
#                         str(requests_data[1]),
#                         str(requests_data[6]),
#                         str(requests_data[11]),
#                         str(requests_data[12]),
#                     ))
#                     connection.commit()
#                 else:
#                     print(link)
#                     new_list_of_links.append(link)
#                 count += 1
#             else:
#                 new_list_of_links.append(link)
#         print('Обработка ссылок завершена')
#
#     date_time = str(datetime.datetime.now())[:-7]  # добавляем в БД дату и время последнего обновления
#     cursor.execute("INSERT INTO kpiapp_update VALUES (Null, ?)", (date_time,))
#     connection.commit()
#
#     connection.close()
#
#     # переписываем csv-файл со списком запросом, оставляя там только необработанные
#     with open(CLIENTS_PATH, 'w', newline='') as f:
#         writer = csv.writer(f)
#         for row in new_list_of_links:
#             writer.writerow(row)
