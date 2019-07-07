from selenium import webdriver
import time
import pyperclip
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)

# нажимаем летающую кнопку 
button_send = browser.find_element_by_tag_name ("button")
button_send.click()

# переключаемся на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# # подтверждаем alert
# alert = browser.switch_to.alert
# alert.accept()

time.sleep(1)

# находим значение х и вставляем в поле
find_value_x = browser.find_element_by_id("input_value")
x = find_value_x.text
y = calc(x)
send_solution = browser.find_element_by_id("answer")
send_solution.send_keys(y)

# нажимаем кнопку отправить
button_send = browser.find_element_by_xpath("//button[text()='Отправить']")
button_send.click()

time.sleep(1)

# копируем результат окна решения в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
