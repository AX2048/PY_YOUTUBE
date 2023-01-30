from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common import exceptions
import sys, time, json

#
# https://skolo.online/documents/webscrapping/#step-1-download-chrome
# https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/
#

def test_chromedriver():

    options = Options()

    options.headless = True

    s = Service(executable_path="/usr/bin/chromedriver") # Фиксит варнинг "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
    driver = webdriver.Chrome(service=s, options=options)

    driver.get("https://google.com/")
    print(driver.title)

    driver.quit()
    return()


def scrape(url):

    options = Options()

    options.headless = False

    #All are optional
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-Advertisement")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument("--disable-gpu")
    #options.add_argument("--window-size=1920x1080")
    #options.add_argument("start-maximized")

    # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")

    s = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=s, options=options)


    print('GET ::\n')
    driver.get(url)

    try:
        print('TRY ::\n')
        #title = driver.find_elements(By.CLASS_NAME, "news__list__item__link__text")
        comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

        #print(comments)
        i = 1
        for c in comments:
            t = c.text
            print(f'N :: {i} | COMM :: {t} |\n')
            i = i + 1

        driver.quit()

    except exceptions.NoSuchElementException:
        error = "Err excep 1"
        print(error)
        driver.quit()

    return()


def main():

    url = "https://www.youtube.com/watch?v=tcHiprXQMmk"

    #test_chromedriver()

    scrape(url)


if __name__ == "__main__":
    main()
