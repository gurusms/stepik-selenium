from selenium import webdriver
import time

link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)

browser.implicitly_wait(5)

button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")
if "прошла" in message.text:
    print("!!! Задание выполнено")
assert "успешно" in message.text
