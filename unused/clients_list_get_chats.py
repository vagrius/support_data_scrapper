"""
Старая версия модуля получения списка клиентов, использовавшаяся до появления линий.
"""

# import csv
# import time
# from global_settings import webdriver_mode_off, login_page_force
#
#
# def clients_list_get():
#     # функция получает актуальный список клиентов на сайте и записывает их в csv-файл
#
#     driver = webdriver_mode_off()
#
#     clients_list_csv = []
#     clients_list_out = []
#
#     driver.get('https://support.elma365.ru/support/clients')
#     time.sleep(3)
#
#     login_page_force(driver)
#
#     # получаем список клиентов из сайдбара
#     general_stack = driver.find_element_by_class_name('side-nav__scope')
#     clients_list = general_stack.find_elements_by_class_name('side-nav__item-link')
#
#     for client in clients_list:
#         clients_list_out.append([str.strip(client.get_attribute('href')[43:]),
#                                  str.strip(client.get_attribute('title'))])
#
#     # считываем в список то, что лежит в csv
#     with open('../data/clients/clients_2021-07.csv') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if row:
#                 clients_list_csv.append(row)
#
#     # добавляем новых клиентов
#     for row in clients_list_out:
#         if row not in clients_list_csv:
#             clients_list_csv.append(row)
#             print(row)
#
#     # обновленный список записываем в файл
#     with open('../data/clients/clients_2021-07.csv', 'w', newline='') as f:
#         writer = csv.writer(f)
#         for row in clients_list_csv:
#             writer.writerow(row)
#
#     driver.close()
#
#     return clients_list_csv
#
#
# if __name__ == "__main__":
#
#     clients_list_get()
