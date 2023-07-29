"""
Устаревший главный модуль (для работы с чатами)
"""

# import csv
# import time
# from aux_functions import string_to_datetime, is_client, time_passed, reaction_time, unacceptable_chars_delete
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from global_settings import webdriver_mode_off, login_page_force
# from datetime import datetime, date
#
#
# def chat_parsing(url, driver):
#
#     list_global = []
#     scroll = True
#
#     try:
#         driver.get(url)
#         time.sleep(3)
#
#         login_page_force(driver)
#
#         WebDriverWait(driver, 600).until(ec.visibility_of_element_located((By.CLASS_NAME, 'chat')))
#
#         scroll_element = driver.find_element_by_class_name('content-body__inner')
#         dts = driver.find_elements_by_xpath(".//div[@class='chat__date']")
#         stks = driver.find_elements_by_xpath(".//div[@class='chat-message-stack']")
#
#         while scroll:
#             sought_dt = datetime.strptime(string_to_datetime(dts[0].text, '00:00'), "%Y-%m-%d %H:%M:%S.%f").date()
#             for _ in range(2):
#                 driver.execute_script("return arguments[0].scrollIntoView(true);", scroll_element)
#                 time.sleep(3)
#             stks_new = driver.find_elements_by_xpath(".//div[@class='chat-message-stack']")
#             if len(stks) == len(stks_new) or sought_dt < date(2021, 6, 1):
#                 scroll = False
#             else:
#                 stks = stks_new
#                 dts = driver.find_elements_by_xpath(".//div[@class='chat__date']")
#
#         org_nm = driver.find_element_by_css_selector('.page-header__title .title').text
#
#         cht = driver.find_element_by_xpath(".//div[@class='chat']")
#         message_groups = cht.find_elements_by_tag_name('app-chat-message-group')
#
#         for i in range(len(dts)):
#             dt = dts[i].text
#             message_stacks = message_groups[i].find_elements_by_xpath(".//div[@class='chat-message-stack']")
#             for j in range(len(message_stacks)):
#                 usr = message_stacks[j].find_element_by_class_name('user-name-block').text
#                 msgs = message_stacks[j].find_elements_by_xpath(".//div[@class='chat-message__text-inner']")
#                 tms = message_stacks[j].find_elements_by_xpath(".//div[@class='chat-message__time']")
#                 for k in range(len(msgs)):
#                     if tms[k].text != '':
#                         tm = tms[k].text
#                     msg = str(msgs[k].text[:81] + '...')
#                     msg = unacceptable_chars_delete(msg)
#                     actual_dt_tm = string_to_datetime(dt, tm)
#                     if actual_dt_tm > '2021-06-01 00:00:00.00000':
#                         new_list = [actual_dt_tm, org_nm, usr, msg]  # Не добавлять если дата меньше sought
#                         print(new_list)  # !!! вывод чата в консоль при отладке  !!!
#                         list_global.append(new_list)
#
#     except Exception as ex:
#         print(f'Не удалось обработать ссылку. Возникла ошибка: {ex}')
#         list_global = []
#     finally:
#         return list_global
#
#
# def get_requests_data(chat_strings_list):
#     requests_list = []
#     client_message_time = ''
#     spec_message_time = ''
#
#     try:
#
#         for i in range(0, len(chat_strings_list)):
#             # определяем начало нового запроса
#             # параметр period - сколько часов прошло, что мы можем выделить новый запрос
#             # NB! предусмотреть, что клиент может написать несколько сообщений подряд
#             print(chat_strings_list[i])
#             if is_client(chat_strings_list[i][2]):
#                 if i == 0:
#                     requests_list.append(chat_strings_list[i])  # время 1-го сообщения - орг-я - имя - первое сообщение
#                     requests_list[-1].append([])  # список реакций
#                     requests_list[-1].append(0)  # время решения
#                 else:
#                     if time_passed(chat_strings_list[i][0], chat_strings_list[i-1][0], 2):
#                         requests_list.append(chat_strings_list[i])
#                         requests_list[-1].append([])
#                         requests_list[-1].append(0)
#
#             if is_client(chat_strings_list[i][2]) and client_message_time == '':  # здесь будем считать время реакции
#                 client_message_time = chat_strings_list[i][0]
#                 spec_message_time = ''
#             if not is_client(chat_strings_list[i][2]) and spec_message_time == '' and client_message_time != '':
#                 spec_message_time = chat_strings_list[i][0]
#                 requests_list[-1][4].append(reaction_time(client_message_time, spec_message_time))
#                 requests_list[-1][5] += requests_list[-1][4][-1]  # инкрементим время решения
#                 if len(requests_list[-1]) == 6:  # заодно определим специалиста
#                     requests_list[-1].append(chat_strings_list[i][2])
#                 client_message_time = ''
#
#     except Exception as ex:
#         print(f'Не удалось получить запросы из чата. Возникла ошибка: {ex}')
#         requests_list = []
#     finally:
#         return requests_list
#
#
# if __name__ == "__main__":
#
#     list_of_links = []
#
#     with open('data\\clients\\clients_2021-07.csv') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if row:
#                 list_of_links.append(row)
#
#     count = 0
#
#     wdriver = webdriver_mode_off()
#
#     with open('data\\requests\\requests_2021-07.csv', 'a') as f:
#         writer = csv.writer(f)
#         for link in list_of_links:
#             link = 'https://support.elma365.ru/_lines/' + link[0]
#             print(f'Обработка ссылки #{count}: {link}')
#             for row in get_requests_data(chat_parsing(link, wdriver)):
#                 writer.writerow(row)
#             count += 1
#         print('Обработка ссылок завершена')
