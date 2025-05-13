from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        assert username_field is not None
        assert password_field is not None
        assert login_button is not None


        if username_field and password_field and login_button:
            print("Элементы найдены")

    except Exception as e:

        print("Ошибка при поиске элементов:", e)

    time.sleep(5)
    driver.quit()

open_saucedemo()
