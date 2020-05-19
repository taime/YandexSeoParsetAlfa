# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
# import pandas as pd
import re
import os
import json


def readTextFile(filename):
    f = open(filename, "r")
    s = f.read()
    return (s)


def parseIpAddreses(txt):
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', txt)
    # for i in range(len(ips)):
    #     print(ips[i])
    return (ips)


def saveArrayToTxtFile(an_array, filename):
    a_file = open(filename, "w")
    for row in an_array:
        np.savetxt(a_file, row)
    a_file.close()


firefox_path = r'/usr/local/bin/geckodriver'  # path from 'which chromedriver'
driver = webdriver.Firefox(executable_path=firefox_path)
driver.get('https://free-proxy-list.net')
driver.implicitly_wait(100)

element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('proxylisttable_wrapper'))
tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')
tutorial_code_soup = tutorial_soup.find_all('textarea', attrs={'class': 'form-control'})
txt = tutorial_code_soup[0].text
ip_addreses = parseIpAddreses(txt)

saveArrayToTxtFile(ip_addreses, 'proxies_list.txt')

print(ip_addreses)


# Select dropdown = new Select(driver.findElement(By.id("identifier")))
# driver.save_screenshot("screenshot.png")
driver.close()
