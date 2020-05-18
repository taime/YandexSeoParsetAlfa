import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent

from printy import printy, raw_format
from random import randint
import http.client

from "../const/const.py" import start_page, end_page, base_url, files_folder, domain, phrases, cookies, hdr
from "../const/func.py" import whiteHtmlFile, getSoupFromHtmlPage

url = 'http://free-proxy.cz/en/proxylist/country/all/https/date/all'
filename = './tmp/proxies.html'


def getProxiesPage(url):
    # Making Request
    response = requests.get(url, headers=hdr, cookies=cookies)
    # Write to file html that we got
    whiteHtmlFile(response.content, filename)
    # Read the Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    return (soup)


def getSoup():
    #soup = getProxiesPage(url)
    soup = getSoupFromHtmlPage(filename)
    # ip_tags = soup.find_all(class_='spy14')
    # for ip_addr in ip_tags:
    # print(ip_addr.text)
    # found = soup.findAll('table', {"id", "proxy_list"})[0]
    found = soup.findAll('table', {"id": "proxy_list"})[0].findAll("tbody")[0].findAll('tr')
    # found = soup.findAll('table')[0].findAll('tr')
    print(found)

    for row in found:
        # print(row)
        # first_column = row.findAll('td').text
        first_column = row.findAll('td')[0].text
        # first_column = row.findAll('td')[0]
        print(first_column)
        print("\n")


# # GET HTML PAGE WITH PROXY
# getProxiesPage(url)

# GET SERVERS ID AND PORT
getSoup()
