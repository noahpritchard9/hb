from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import time
import json

dc = DesiredCapabilities.CHROME
dc["goog:loggingPrefs"] = {"performance": "ALL"}

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')

service = Service("~/hb/chromedriver/stable/chromedriver")

browser = webdriver.Chrome(service=service, options=options, desired_capabilities=dc);
browser.get("https://www.sparknotes.com/shakespeare/macbeth/")

time.sleep(1)

logs = browser.get_log("performance")

with open("network_log.json", "w", encoding="utf-8") as f:
    f.write("[")

    for log in logs:
        network_log = json.loads(log["message"])["message"]

        if ("Network.response" in network_log["method"] or "Network.request" in network_log["method"] or "Network.webSocket" in network_log["method"]):
            f.write(json.dumps(network_log)+",")
    f.write("{}]")
browser.quit()

