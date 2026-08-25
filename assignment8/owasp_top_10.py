from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)


driver.get("https://owasp.org/Top10/2025/")

top_ten_list = driver.find_element(By.CSS_SELECTOR,'[id=top-102025-list]')
ol = top_ten_list.find_element(By.XPATH, 'following-sibling::ol')
list_items = ol.find_elements(By.TAG_NAME, 'li')
links = []

for li in list_items:
    link = li.find_element(By.CSS_SELECTOR, 'a')
    name = link.text.strip()
    url = link.get_attribute("href")
    if name and url:
        links.append({"Title": name, "Href": url})
print(links)


with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Href"])
    for link in links:
        writer.writerow([link["Title"], link["Href"]])




driver.quit()