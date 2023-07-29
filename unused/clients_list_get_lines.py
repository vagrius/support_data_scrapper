"""
Устаревший модуль получения списка идентификаторов активных сессий:
с периодичностью парсил главную страницу, получал из нее список новых сессий и записывал в csv-файл.
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
#     lines_dict = {
#         0: 'sup',
#         # 1: 'sup',
#         2: 'sup',
#         # 5: 'onprem',
#         # 6: 'onprem',
#     }
#
#     driver.get('https://support.elma365.ru/_lines')
#     time.sleep(3)
#
#     login_page_force(driver)
#
#     # получаем список клиентов из сайдбара
#     for key, value in lines_dict.items():
#         general_stack = driver.find_elements_by_class_name('side-nav__scope_departmanet')[key]
#         clients_list = general_stack.find_elements_by_class_name('side-nav__item-user-link')
#         try:
#             for client in clients_list:
#                 clients_list_out.append([str.strip(client.get_attribute('href')[34:]),
#                                          str.strip(client.get_attribute('title')),
#                                          'active',
#                                          value])
#         except Exception as ex:
#             print(f'Не удалось обработать список. Возникла ошибка: {ex}')
#         # finally:
#         #     driver.close()
#
#     # считываем в список то, что лежит в csv - абсолютный путь нужен для запуска по расписанию
#     with open(r'C:\Users\Vadim\PycharmProjects\ScrapMachine\data\clients.csv') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if row:
#                 if row[2] == 'active' and row not in clients_list_out:
#                     row[2] = 'closed'
#                 clients_list_csv.append(row)
#
#     # добавляем новых клиентов в csv-список
#     for row in clients_list_out:
#         if row not in clients_list_csv:
#             clients_list_csv.append(row)
#             print(row)  # выводим в консоль для проверки
#
#     # обновленный список записываем в файл
#     with open(r'C:\Users\Vadim\PycharmProjects\ScrapMachine\data\clients.csv', 'w', newline='') as f:
#         writer = csv.writer(f)
#         for row in clients_list_csv:
#             try:
#                 writer.writerow(row)
#             except Exception as ex:
#                 print(f'Не удалось корректно обработать строку. Возникла ошибка: {ex}')
#
#     # driver.close()
#
#     return clients_list_csv
#
#
# if __name__ == "__main__":
#
#     clients_list_get()
