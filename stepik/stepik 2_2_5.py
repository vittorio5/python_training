from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text
x = int(num1) + int(num2)
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(x))
browser.find_element_by_tag_name('button').click()
