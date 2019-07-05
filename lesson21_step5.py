from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)

# Ваш код, который заполняет обязательные поля
# input1 = browser.find_element_by_xpath("//input[contains(@placeholder, 'имя')]")
# input1.send_keys("Ivan")

x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
print(f"число х = {x}\nрезультат формулы = {y}")

resultat = browser.find_element_by_xpath("//input[@id='answer']")
resultat.send_keys(y)

checkbox_robot = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
checkbox_robot.click()

radiobutton_robotrul = browser.find_element_by_xpath("//label[@for='robotsRule']")
radiobutton_robotrul.click()

button_send = browser.find_element_by_xpath("//button[text()='Отправить']")
button_send.click()



# # Отправляем заполненную форму
# button = browser.find_element_by_css_selector("button.btn")
# button.click()

# # Проверяем, что смогли зарегистрироваться
# # ждем загрузки страницы
# time.sleep(1)

# # находим элемент, содержащий текст
# welcome_text_elt = browser.find_element_by_tag_name("h1")
# # записываем в переменную welcome_text текст из элемента welcome_text_elt
# welcome_text = welcome_text_elt.text

# # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
