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


def parseIpAddreses(txt):
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', txt)
    # for i in range(len(ips)):
    #     print(ips[i])
    return (ips)


def checkHasCapcha(soup):
    title_tags = soup.find_all(class_='captcha__image')
    has_capcha = len(title_tags) > 0
    if has_capcha:
        printy("The Capcha :(", "m")

    return (has_capcha)
