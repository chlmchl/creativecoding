# get HTML content of a page
import requests
import csv
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

# run selenium headless
chrome_options = Options()
chrome_options.add_argument("--headless")


# #url of the page to scrape
url = "https://emojitracker.com"

# #initiating the webdriver
driver = webdriver.Chrome("/Users/thomas/chromedriver", options=chrome_options)
driver.get(url)

# ensure that the page is loaded
time.sleep(5)

# close pop up epilepsy warning
driver.find_element(By.ID, "okbtn").click()

for i in range(72):
    # this renders the JS code and stores all
    # of the info in static HTML code
    html = driver.page_source

    # apply bs4 to html variable to scrape all emojis scores
    soup = BeautifulSoup(html, "html.parser")
    emoji_numbers = soup.find_all("span", {"class": "score"})
    emoji_name = soup.find_all("li", {"class": "emoji_char"})

    # printing top ten emojis
    count = 0
    print("round : " + str(i))

    # create variable for timestamp and make sure it's readable
    ts = time.time()
    readable_ts = time.ctime(ts)

    # print(csvRow)

    with open("emoji.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if i == 0:
            writer.writerow(["timestamp", "Unicode", "score"])

        for emoji_number in emoji_numbers:
            csvEmoji = emoji_name[count].get("id")
            csvScore = emoji_number.get_text()
            writer.writerow([readable_ts, csvEmoji, csvScore])
            count = count + 1
            if count == 10:
                break
    # scrape again in...
    time.sleep(600)

with open("emoji.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


driver.close()  # closing the webdriver
