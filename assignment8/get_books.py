from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

title = driver.title

body = driver.find_element(By.CSS_SELECTOR, 'body')

results_list = driver.find_elements(By. CLASS_NAME, 'cp-search-result-item')

result_title = results_list[0].find_element(By. CLASS_NAME, 'title-content')
print(result_title.text)

author = driver.find_element(By.CLASS_NAME, 'author-link')

print(author.text)

published = driver.find_element(By.CLASS_NAME, 'display-info-primary')

results = []


for item in results_list:
    title = item.find_element(By.CLASS_NAME, 'title-content')
    authors = item.find_elements(By.CLASS_NAME, 'author-link')
    author_text = ';'.join([a.text for a in authors])

    format_year = item.find_element(By.CLASS_NAME, 'display-info-primary')

    book_dict = {
        "Title": title.text,
        "Author": author_text,
        "Format Year": format_year.text
    }

    results.append(book_dict)
results_df = pd.DataFrame(results)

print(results_df)

results_df.to_csv('get_books.csv')

with open('assignment8/get_books.json', 'w') as f:
    json.dump(results, f, indent=4)

driver.quit()


