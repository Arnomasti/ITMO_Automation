#я честно пыталась сделать без менеджера, но он мне выдавал ошибку на драйвер, хотя путь вроде верный указывала... нашла, что можно так)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
button = driver.find_element(By.ID, "login-button")

print("Элементы найдены!")

driver.quit()
