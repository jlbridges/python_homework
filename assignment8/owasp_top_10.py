from xml.etree.ElementTree import indent

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import csv
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)


driver.get("https://owasp.org/Top10/2025/")

see_also_h3 = driver.find_element(By.CSS_SELECTOR,'[id=top-102025-list]') # our starting point
links = []
if see_also_h3:
    parent_div = see_also_h3.find_element(By.XPATH, '..') # up to the parent div
    if parent_div:
        see_also_div = parent_div.find_element(By.XPATH,'ol' ) # over to the div with all the links
        link_elements = see_also_div.find_elements(By.CSS_SELECTOR, 'a')
        for link in link_elements:
            # print(f"{link.text}: {link.get_attribute('href')}")
            name = link.text.strip()
            url = link.get_attribute("href")
            if name and url:
                links.append({"name": name, "url": url})
print(links)


with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Link"])
    for link in links:
        writer.writerow([link["name"], link["url"]])




driver.quit()