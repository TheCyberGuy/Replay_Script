import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from fx_sign_up import signup


options = Options()


# options.add_argument('--headless')

MAIL_URL = 'https://www.ghostlymail.com/'

driver = webdriver.Firefox(options=options)


def accept_cookies():
    btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[1]'))
    )
    btn.click()


def mail_and_verification():
    driver.get(MAIL_URL)
    mail = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/main/section[2]/div[1]/div/div/div/span'))
    )

    time.sleep(1.5)
    # accept_cookies()
    signup(mail.text)

    incoming = WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/main/section[2]/div[2]/div/div[3]/div'))
    )
    incoming.find_element(By.TAG_NAME, 'a').click()
    driver.close()
    print('Email és a jelszó elmentve az accounts.txt állományban a kreáció idejável bélyegezve (email:pass - idő)')



    