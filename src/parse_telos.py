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


def cleanIt(mystring):
    mystring = mystring.replace('\n', '')
    mystring = ' '.join(mystring.split())
    return mystring


def getSlug(mystring):
    mystring = mystring.replace('services/', '')
    mystring = mystring.replace('.html', '')
    return mystring


soup = getSoupFromHtmlPage('./sources/2.html')

sub_cat_blocks = soup.find_all(class_='service-item-wrap')

for sub in sub_cat_blocks:
    subtitle_tags = sub.find_all(class_='service-item-wrap__title')
    printy(cleanIt(subtitle_tags[0].a.text), 'm')

    product_tags = sub.findAll('li')
    for prod in product_tags:
        print(cleanIt(prod.a.text))
        printy(getSlug(prod.a.get('href')), 'g')

    print("\n")


# title_tags = sub_cat_blocks[0].find_all(class_='service-item-wrap__title')

# for title in title_tags:

#     print(title.a.text)
#     print("\n")
# print(soup)
