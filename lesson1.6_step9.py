from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

#Cоздаем экземпляр Faker
fake = Faker() 

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

     # Находим все поля ввода в первом блоке
    elements = browser.find_elements(By.CSS_SELECTOR, ".first_block input")
    for element in elements:
        placeholder = element.get_attribute("placeholder")
        if placeholder == "Input your first name":
            element.send_keys(fake.first_name())
        elif placeholder == "Input your last name":
            element.send_keys(fake.last_name())
        elif placeholder == "Input your email":
            element.send_keys(fake.email())

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла