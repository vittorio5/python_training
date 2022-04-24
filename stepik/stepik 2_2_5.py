from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
num1 = browser.find_element(By.ID, 'num1').text
num2 = browser.find_element(By.ID, 'num2').text
x = int(num1) + int(num2)
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(x))
browser.find_element(By.TAG_NAME, 'button').click()
