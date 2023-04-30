from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import json

# Due by May 1

hb_files = ["hb", "bid", "prebid", "auction", "hbjson", "hb-multi"]
hb_list = {}

websites = [
    "https://yahoo.com",
    "https://msn.com",
    "https://www.washingtonpost.com",
    "https://www.huffpost.com",
    "https://www.usmagazine.com",
    "https://www.buzzfeed.com",
    "https://www.nytimes.com",
    "https://www.forbes.com",
    "https://www.tmz.com",
    "https://www.eonline.com",
]

dc = DesiredCapabilities.CHROME
dc["goog:loggingPrefs"] = {"performance": "ALL"}

options = webdriver.ChromeOptions()

options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

service = Service("~/hb/chromedriver/stable/chromedriver")

browser = webdriver.Chrome(service=service, options=options, desired_capabilities=dc)

for website in websites:
    print(f"checking {website}")
    browser.get(website)

    # wait for data on page
    time.sleep(5)
    # record how long it takes for the ads to show up/page to load
    # how significant is the latency

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    html_ads = soup.select("[class*='ad' i]")
    html_bids = soup.select("[class*='bid' i]")

    id_ads = soup.select("[id*='ad' i]")
    id_bids = soup.select("[id*='bid' i]")

    print(f"div ads from bs4: {len(html_ads)}")
    print(f"div bids from bs4: {len(html_bids)}")

    print(f"id ads from bs4: {len(id_ads)}")
    print(f"id bids from bs4: {len(id_bids)}")

    logs_raw = browser.get_log("performance")
    logs = [json.loads(log["message"])["message"] for log in logs_raw]

    # only check logs we received that have js files
    website_is_hb = False
    for log in logs:
        if (
            log["method"] == "Network.responseReceived"
            and "javascript" in log["params"]["response"]["mimeType"]
        ):
            for file in hb_files:
                curr_log_url = log["params"]["response"]["url"]
                if file in curr_log_url:
                    print(f"found {file}")
                    website_is_hb = True
            hb_list[website] = website_is_hb

print(hb_list)
browser.quit()
