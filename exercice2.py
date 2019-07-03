from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')

# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
driver.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")