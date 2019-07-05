from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)


num1 = browser.find_element_by_id("num1")
x = int(num1.text)
num2 = browser.find_element_by_id("num2")
y = int(num2.text)
print(f"х = {x}\ny = {y}\nx + y ={x + y}")

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(x + y))

button_send = browser.find_element_by_xpath("//button[@type='submit']")
button_send.click()
