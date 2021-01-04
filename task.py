# get HTML content of a page
import requests
import csv
import os
from flask import jsonify

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import datetime

# config selenium headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# #url of the page to scrape
url = "https://emojitracker.com"

def refresh():
    # #initiating the webdriver
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url)

    #ensure that the page is loaded
    time.sleep(1)

    #close pop up epilepsy warning
    driver.find_element(By.ID, "okbtn").click()

    # this renders the JS code and stores all 
    # of the info in static HTML code
    html = driver.page_source

    # apply bs4 to html variable to scrape all emojis scores
    soup = BeautifulSoup(html, "html.parser")
    emoji_numbers = soup.find_all('span', {'class' : 'score'})
    emoji_name = soup.find_all('li', {'class' : 'emoji_char'})

    i = 0

    #create variable for timestamp and make sure it's readable
    date = datetime.datetime.now()

    usage = []

    for emoji_number in emoji_numbers:
        emoji = emoji_name[i].get("id")
        count = emoji_number.get_text()
        usage.append((date, emoji, count))
        i = i + 1

    driver.close() #closing the webdriver

    return jsonify(usage)
