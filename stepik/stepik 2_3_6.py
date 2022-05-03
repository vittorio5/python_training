import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла