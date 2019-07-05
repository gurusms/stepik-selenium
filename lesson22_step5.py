from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path='D:/Program Files/_Inet/ChromeDriver/chromedriver.exe')
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# button = browser.find_element_by_tag_name("button")
# button.click()
assert True