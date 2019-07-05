from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
browser.get(link)


valuex = browser.find_element_by_id("input_value")
x = calc(valuex.text)
print(f"x = {valuex.text}\nзначение calc(x) = {x}")

# вставляем результат подсчета в поле ввода
resultat = browser.find_element_by_xpath("//input[@id='answer']")
resultat.send_keys(x)

# скроллим экран до кнопки
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

# щелкаем подтверждаю
checkbox_robot = browser.find_element_by_id('robotCheckbox')
checkbox_robot.click()

# щелкаем роботы рулят
radiobutton_robotrul = browser.find_element_by_id('robotsRule')
radiobutton_robotrul.click()

button.click()
