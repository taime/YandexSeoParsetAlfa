from const.config import start_page, end_page, base_url, files_folder, domain, phrases, cookies, hdr
import time
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent

from printy import printy, raw_format
from random import randint

import http.client

from const.config import start_page, end_page, base_url, files_folder, domain, phrases, cookies, hdr
from const.proxy_lists import proxies_list_https
from helpers.file_helpers import *


def getHttpsProxy(n):
    proxies_list = readDataFromJsonFile('const/proxies_https.json')
    proxy = {"https": "https://"+proxies_list[n]}
    return proxy


def getRandomHttpsProxy():
    proxies_list = readDataFromJsonFile('const/proxies_https.json')
    random = randint(0, len(proxies_list)-1)
    proxy = {"https": "https://"+proxies_list[random]}
    return proxy


# def getRandomProxy():
#     # proxies_list = proxies_list_http
#     proxies_list = proxies_list_https
#     q_proxies = len(proxies_list)-1
#     random = randint(0, q_proxies)
#     proxies = {"https": proxies_list[random]}
#     return proxies


# def getProxies(n):
#     proxy = proxies_list_https[n]
#     proxies = {"https": proxy}
#     return proxies
