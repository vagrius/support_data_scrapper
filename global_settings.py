import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Функция отключения режима вебдрайвера, чтобы сайты воспринимали его как обычный пользовательский браузер
def webdriver_mode_off():

    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.set_preference("dom.webdriver.enabled", False)
    driver = webdriver.Firefox(executable_path="C:\\GeckoDriver\\geckodriver.exe", options=options)

    return driver


# Функция залогинивания на сайте, если нужно
def login_page_force(driver):

    try_to_find = driver.find_elements_by_name('emailOrLogin')

    if try_to_find:
        email_elem = driver.find_element_by_name('emailOrLogin')
        email_elem.send_keys('email')
        pass_elem = driver.find_element_by_name('password')
        pass_elem.send_keys('password') 
        pass_elem.send_keys(Keys.ENTER)
        time.sleep(7)
    else:
        pass
