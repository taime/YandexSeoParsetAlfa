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
from helpers.common_helpers import *
from helpers.file_helpers import *
from helpers.proxy_helpers import *
from helpers.parsing_helpers import *

url = "https://www.telosbeauty.ru/"


def getPage(url, hdr, cookies):
    # text_q = urllib.parse.quote_plus(text)
    # url = base_url + text_q + "&p=" + str(p)
    # Making Request
    response = requests.get(url, headers=hdr, cookies=cookies)

    # Write to file html that we got
    writeFile(response.content, 'telosbeauty_test.html')

    # soup = BeautifulSoup(response.text, 'html.parser')
    # return (soup)
    return (response)

getPage(url, hdr, cookies)
