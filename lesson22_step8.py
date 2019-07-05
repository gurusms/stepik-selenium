from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)

# вставляем в поле ввода
firstname = browser.find_element_by_name("firstname")
firstname.send_keys('firstname')

# вставляем в поле ввода
lastname = browser.find_element_by_name("lastname")
lastname.send_keys('lastname')

# вставляем в поле ввода
email = browser.find_element_by_name("email")
email.send_keys('email')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'history.txt')           # добавляем к этому пути имя файла 
# print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(file_path)
sendfile = browser.find_element_by_id('file')
sendfile.send_keys(file_path)

# нажимаем кнопку отправить
button_send = browser.find_element_by_xpath("//button[text()='Отправить']")
button_send.click()
