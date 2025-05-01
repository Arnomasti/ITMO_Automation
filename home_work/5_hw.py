from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


username = driver.find_element(By.ID, 'user-name')

if username is None:
    print('Элементы не найдены')
else:
    print('Элемент найден')


password = driver. find_element(By. ID, 'password')

if password is None:
    print('Элементы не найдены')
else:
    print('Элемент найден')


submit = driver.find_element(By.ID, 'login-button')

if submit is None:
    print('Элементы не найдены')
else:
    print('Элемент найден')

#спасибо за хорошую проверку! Переделала! Я час возилась не понимала, почему делая все строго по уроку все равно не находит элемент!
#А оказывается все дело во внимательности... ахахха, одна деталь не так и ничего уже не работает! Но так смешно, когда ее находишь спустя столько потраченного времени!:)