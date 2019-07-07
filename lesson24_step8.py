from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyperclip
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe', chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

button = WebDriverWait(browser, 25).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
book = browser.find_element_by_id("book")
book.click()

# находим значение х и вставляем в поле
find_value_x = browser.find_element_by_id("input_value")
x = find_value_x.text
y = calc(x)
send_solution = browser.find_element_by_id("answer")
send_solution.send_keys(y)

# нажимаем кнопку отправить
button_send = browser.find_element_by_xpath("//button[text()='Отправить']")
button_send.click()

# time.sleep(1)

# копируем результат окна решения в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)

# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "check"))
#     )
# button.click()
# message = browser.find_element_by_id("check_message")

# assert "успешно" in message.text
