# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

# chrome_path = r'/usr/local/bin/chromedriver'  # path from 'which chromedriver'
# driver = webdriver.Chrome(executable_path=chrome_path)

firefox_path = r'/usr/local/bin/geckodriver'  # path from 'which chromedriver'
driver = webdriver.Firefox(executable_path=firefox_path)

driver.get('https://free-proxy-list.net')
driver.implicitly_wait(100)
num_links = len(driver.find_elements_by_link_text('Next'))

for i in range(num_links):
    # navigate to link
    button = driver.find_elements_by_class_name("fg-button ui-button ui-state-default next")[i]
    button.click()
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('proxylisttable_wrapper'))
    tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')
    tutorial_code_soup = tutorial_soup.find_all('td', attrs={'class': 'odd'})
    tutorial_code = [i.getText() for i in tutorial_code_soup]
    code_blocks.append(tutorial_code)
    # go back to initial page
    driver.execute_script("window.history.go(-1)")
print(code_blocks)

driver.close()


for i, tutorial_code in enumerate(code_blocks):
    with open('code_blocks{}.txt'.format(i), 'w') as f:
        for code_block in tutorial_code:
            f.write(code_block+"\n")
