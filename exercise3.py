from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.XPATH, "//button")
print(button)