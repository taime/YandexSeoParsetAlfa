import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent

from printy import printy, raw_format
from random import randint
import http.client
from const import start_page, end_page, base_url, files_folder, domain, phrases, cookies, hdr
from proxy_lists import proxies_list_https


def whiteHtmlFile(htmlBody, filename):
    with open(filename, 'wb') as f:
        f.write(htmlBody)


def getSoupFromHtmlPage(file):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return (soup)