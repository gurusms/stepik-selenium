from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)

# human_radio = browser.find_element_by_id("humanRule")
# human_checked = human_radio.get_attribute("checked")
# print("value of human radio: ", human_checked)
# # assert human_checked is not None, "Human radio is not selected by default"
# assert human_checked == "true", "Human radio is not selected by default"

find_valuex = browser.find_element_by_tag_name("img")
valuex = find_valuex.get_attribute("valuex")
print(f"valuex = {valuex}\ntype valuex = {type(valuex)} ")
# assert human_checked is not None, "Human radio is not selected by default"
# assert human_checked == "true", "Human radio is not selected by default"
# x_element = browser.find_element_by_xpath("//span[@id='input_value']")
# x = valuex.text
# y = calc(x)
y = calc(valuex)

print(f"число х = {valuex}\nрезультат формулы = {y}")

resultat = browser.find_element_by_xpath("//input[@id='answer']")
resultat.send_keys(y)

checkbox_robot = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
checkbox_robot.click()

radiobutton_robotrul = browser.find_element_by_xpath("//input[@id='robotsRule']")
radiobutton_robotrul.click()

# robots_radio = browser.find_element_by_id("robotsRule")
# robots_checked = robots_radio.get_attribute("checked")
# assert robots_checked is None

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
