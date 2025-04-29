from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Говорим Selenium ждать, пока цена не станет равна $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Теперь находим саму кнопку и нажимаем её
    button = browser.find_element(By.ID, "book")
    button.click()

    # Прокручиваем немного страницу вниз, чтобы увидеть поле ввода
    browser.execute_script("window.scrollBy(150, 0);")
    
    # Далее считаем значение и отправляем форму
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Заполняем поле и отправляем форму
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    # Нажимаем кнопку отправки формы
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла

