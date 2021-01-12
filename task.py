# get HTML content of a page
import csv
import datetime
import os
import time
import unicodedata

from flask import jsonify
import requests

from bs4 import BeautifulSoup
import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# config selenium headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# #url of the page to scrape
url = "https://emojitracker.com"

# connect database
conn = psycopg2.connect(os.environ.get("TWITTER_DIARY_DB_URI"))


def refresh():
    # #initiating the webdriver
    driver = webdriver.Chrome(
        executable_path=os.environ.get("TWITTER_DIARY_CHROMEDRIVER_PATH"),
        chrome_options=chrome_options,
    )
    driver.get(url)

    # ensure that the page is loaded
    time.sleep(1)

    # close pop up epilepsy warning
    driver.find_element(By.ID, "okbtn").click()

    # this renders the JS code and stores all
    # of the info in static HTML code
    html = driver.page_source

    # apply bs4 to html variable to scrape all emojis scores
    soup = BeautifulSoup(html, "html.parser")
    emoji_numbers = soup.find_all("span", {"class": "score"})
    emoji_name = soup.find_all("li", {"class": "emoji_char"})

    index = 0

    # create variable for timestamp and make sure it's readable
    date = datetime.datetime.now()

    sql = "SELECT * FROM history"

    # get data and store it in before
    cur = conn.cursor()
    cur.execute(sql)
    before = cur.fetchall()

    # empty history tab
    sql = "TRUNCATE history"
    cur.execute(sql)

    after = []

    # if length of before = 0, initialiaze database
    if len(before) == 0:
        for emoji_number in emoji_numbers:
            emoji = emoji_name[index].get("data-title")
            count = emoji_number.get_text()
            after.append((date, emoji, count))

            index = index + 1

        # store everything
        sql = "INSERT INTO history(date, emoji, count) VALUES(%s, %s, %s)"
        cur.executemany(sql, after)
        conn.commit()

        cur.close()

        return "database initialized"

    delta = 0
    line = (0, 0, 0)

    for emoji_number in emoji_numbers:
        emoji = emoji_name[index].get("id")
        count = emoji_number.get_text()
        after.append((date, emoji, count))

        diff = int(after[index][2]) - int(before[index][2])
        if diff > delta:
            delta = diff
            line = emoji, delta, before[index][0], after[index][0]

        index = index + 1

    sql = "INSERT INTO history(date, emoji, count) VALUES(%s, %s, %s)"
    cur.executemany(sql, after)

    sql = "INSERT INTO delta (emoji, delta, before, after) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, line)
    conn.commit()

    cur.close()

    driver.close()  # closing the webdriver

    return "success"


def diary():
    sql = "SELECT * FROM delta"

    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()

    return jsonify(result)