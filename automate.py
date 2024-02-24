from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://demoqa.com/login")

user = browser.find_element(By.ID, 'userName')
passw = browser.find_element(By.ID, 'password')

user.send_keys('udit123')
passw.send_keys('Udit@2003')

login = browser.find_element(By.ID, 'login')
login.click()

while True:
    pass
