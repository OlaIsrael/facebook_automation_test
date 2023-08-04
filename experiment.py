import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# enterUsername = driver.find_element("id", "user-name")
enterUsername  = driver.find_element(By.XPATH, '//*[@id="user-name"]')
enterUsername.send_keys("standard_user")
time.sleep(1)

# enterPassword = driver.find_element("id", "password")
enterPassword = driver.find_element(By.ID, "password")
enterPassword.send_keys("secret_sauce")
time.sleep(1)

login = driver.find_element("id", "login-button")

login.click()
time.sleep(1)
print("login sucessful")

homePage = driver.find_element(By.CLASS_NAME,"app_logo")
assert driver.homePage == "Swag Labs"

time.sleep(7)
