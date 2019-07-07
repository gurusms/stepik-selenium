from selenium import webdriver
import time
import os
import pyperclip
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)

# нажимаем кнопку отправится ...
button_send = browser.find_element_by_tag_name ("button")
button_send.click()

# подтверждаем alert
alert = browser.switch_to.alert
alert.accept()

time.sleep(1)

# находим значение х и вставляем в поле
find_value_x = browser.find_element_by_id("input_value")
x = find_value_x.text
y = calc(x)
send_solution = browser.find_element_by_id("answer")
send_solution.send_keys(y)

# # вставляем в поле ввода
# firstname = browser.find_element_by_name("firstname")
# firstname.send_keys('firstname')

# # вставляем в поле ввода
# lastname = browser.find_element_by_name("lastname")
# lastname.send_keys('lastname')

# # вставляем в поле ввода
# email = browser.find_element_by_name("email")
# email.send_keys('email')

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'history.txt')           # добавляем к этому пути имя файла 
# # print(os.path.abspath(__file__))
# # print(os.path.abspath(os.path.dirname(__file__)))
# # print(file_path)
# sendfile = browser.find_element_by_id('file')
# sendfile.send_keys(file_path)

# нажимаем кнопку отправить
button_send = browser.find_element_by_xpath("//button[text()='Отправить']")
button_send.click()

time.sleep(1)

# копируем результат окна решения в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
