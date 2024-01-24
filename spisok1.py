from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(a, b):
        return str(a + b)
    
    
    sel_num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = int(sel_num1.text)
    sel_num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = int(sel_num2.text)
    summ = calc(num1, num2)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(summ) 
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()