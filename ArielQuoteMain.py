import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from AuthorizationDataForGithub import ariel_password
from AuthorizationDataForGithub import ariel_login
import pandas as pd
import glob

start_time = time.time()


# Using Selenium
url = 'https://account.arielcorp.com/Identity/Account/Login'

# set webdriver options
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\hp\\GitHubProjects\\ArielSparePartsDatabase\\Downloads"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
# headless mode
# chromeOptions.headless = True
driver = webdriver.Chrome(options=chromeOptions)


try:
    print('Login Ariel Website...')
    # Open and login  Ariel website
    driver.get(url=url)

    # entering a email
    email_input = driver.find_element(By.ID,'Input_UserName')
    email_input.clear()
    email_input.send_keys(ariel_login)
    driver.implicitly_wait(10)

    # entering a password
    password_input = driver.find_element(By.ID,'Input_Password')
    password_input.clear()
    password_input.send_keys(ariel_password)
    driver.implicitly_wait(10)

    # press login button
    login_button_click = driver.find_element(By.XPATH, '//button[contains(@class, "")]').click()
    driver.implicitly_wait(20)
    time.sleep(10)

    # Open ariel parts page
    driver.get(url='https://www.arielcorp.com/parts/portal/')
    driver.implicitly_wait(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
