from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    #Переходим на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    #Находим значение и вводим результат
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    #Нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    
    
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла
