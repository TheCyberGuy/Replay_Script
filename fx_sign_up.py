import requests
import random
import string
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

SIGNUP_URL = "https://app.fxreplay.com/sign-up"


options = Options()

options.add_argument('--headless')

driver = webdriver.Firefox(options=options)


def signup(scraped_mail):
    res = requests.get("https://api.namefake.com/")
    full_name = res.json()["name"]


    # user_mail = str(input("Adja meg a megadandó ideiglenes emailt: "))


    driver.get(SIGNUP_URL)

    generated_pass = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

    try:
        
        name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/layout/empty-layout/div/div/auth-sign-up/div/div[1]/div/form/mat-form-field[1]/div/div[1]/div/input'))
        )

        mail = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/layout/empty-layout/div/div/auth-sign-up/div/div[1]/div/form/mat-form-field[2]/div/div[1]/div/input'))
        )

        passwd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/layout/empty-layout/div/div/auth-sign-up/div/div[1]/div/form/mat-form-field[3]/div/div[1]/div[1]/input'))
        )

        checkbox_1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/layout/empty-layout/div/div/auth-sign-up/div/div[1]/div/form/div[1]/mat-checkbox/label/span[1]'))
        )

        checkbox_2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/layout/empty-layout/div/div/auth-sign-up/div/div[1]/div/form/div[2]/mat-checkbox/label/span[1]'))
        )

        form_submit = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/layout/empty-layout/div/div/auth-sign-up/div/div[1]/div/form/button'))
        )
    except:
        print("Elements not found or timed out.")
        driver.quit() 



    name.send_keys(full_name)
    mail.send_keys(scraped_mail)
    passwd.send_keys(generated_pass)
    checkbox_1.click()
    checkbox_2.click()

    form_submit.click()

    with open('accounts.txt', 'a') as f:
        f.write(f'{scraped_mail}:{generated_pass}:{date.today()}\n')

    # driver.close()