from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_xpath("//input[contains(@placeholder, 'имя')]")
input1.send_keys("Ivan")
input2 = browser.find_element_by_xpath("//input[contains(@placeholder, 'фамилию')]")
input2.send_keys("Petrov")
input3 = browser.find_element_by_xpath("//input[contains(@placeholder, 'Email')]")
input3.send_keys("1@Smolensk.ru")
input4 = browser.find_element_by_xpath("//input[contains(@placeholder, 'телефон')]")
input4.send_keys("12345")
input5 = browser.find_element_by_xpath("//input[contains(@placeholder, 'адрес')]")
input5.send_keys("город, улица, дом")


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
