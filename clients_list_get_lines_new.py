"""
Актуальный модуль получения списка идентификаторов активных сессий.
"""

import time
from global_settings import webdriver_mode_off, login_page_force


def clients_list_get(check_link):  # функция получает список закрытых сессий, которые еще не были записаны в БД
    # подготовка
    driver = webdriver_mode_off()
    clients_list_out = []
    driver.get('https://portal.elma365.ru/_lines')
    time.sleep(3)
    login_page_force(driver)
    time.sleep(5)
    driver.find_element_by_css_selector("[title='Закрытые сессии']").click()
    time.sleep(3)

    # получаем список сессий из сайдбара
    end_of_list = False
    link_number = 0
    general_stack = driver.find_elements_by_class_name('side-nav__scope_departmanet')[1]
    clients_list = general_stack.find_elements_by_class_name('side-nav__item-user-link')

    # формируем окончательный список сессий для дальнейшей обработки
    while not end_of_list:
        client = clients_list[link_number]
        current_link = str.strip(client.get_attribute('href')[33:])
        current_title = str.strip(client.get_attribute('title'))
        if current_link:  # если ссылка определена, добавляем в список
            clients_list_out.append([current_link,
                                     current_title])
        if current_link == check_link:  # если дошли до контрольной ссылки, ставим признак конца поиска
            end_of_list = True
        if link_number == len(clients_list)-2 and not end_of_list:  # кликаем на Показать еще
            driver.find_element_by_partial_link_text('Показать ещё').click()
            time.sleep(3)
            general_stack = driver.find_elements_by_class_name('side-nav__scope_departmanet')[1]
            clients_list = general_stack.find_elements_by_class_name('side-nav__item-user-link')
        link_number += 1
    clients_list_out.pop(-1)
    #  print(*clients_list_out, sep='\n')  # вывод в консоль для отладки
    driver.close()
    return clients_list_out


# if __name__ == "__main__":
#
#     clients_list_get('90d17228-3fe7-4b57-bb88-1a691b565bc2')
