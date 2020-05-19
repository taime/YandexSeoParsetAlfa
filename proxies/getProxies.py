# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
# import pandas as pd
import re
import os
import json


def parseIpAddreses(txt):
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', txt)
    return (ips)


def readTextFile(filename):
    f = open(filename, "r")
    s = f.read()
    return (s)


def readDataFromTextFile(filename):
    txt = readDataFromTextFile('demofile.txt')
    ip_addreses = parseIpAddreses(txt)
    return (ip_addreses)


def saveDataToTextFile(data, filename):
    a_file = open(filename, "w")
    for row in data:
        np.savetxt(a_file, row)
    a_file.close()


def saveDataToJsonFile(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def readDataFromJsonFile(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return(data)


def getProxies():
    filename = '../const/proxies.json'
    url = 'https://free-proxy-list.net'
    firefox_path = r'/usr/local/bin/geckodriver'  # path from 'which chromedriver'

    driver = webdriver.Firefox(executable_path=firefox_path)
    driver.get(url)
    driver.implicitly_wait(100)

    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('proxylisttable_wrapper'))
    tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')
    tutorial_code_soup = tutorial_soup.find_all('textarea', attrs={'class': 'form-control'})
    txt = tutorial_code_soup[0].text

    # Parse the Ip addreses from text
    ip_addreses = parseIpAddreses(txt)

    # Saving The IP addreses to json file
    saveDataToJsonFile(ip_addreses, filename)

    # Select dropdown = new Select(driver.findElement(By.id("identifier")))
    # driver.save_screenshot("screenshot.png")
    driver.close()

    return(ip_addreses)


getProxies()
