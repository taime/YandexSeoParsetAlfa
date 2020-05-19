import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent

from pycookiecheat import chrome_cookies

text = 'Преобразователи частоты цена'
text = urllib.parse.quote_plus(text)
url = "https://yandex.ru/search/?text="+text


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
ua = UserAgent()
hdr = {'User-Agent': ua.random,
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
cookies = chrome_cookies(url)

response = requests.get(url, headers=hdr, cookies=cookies)
doc = BeautifulSoup(response.text, 'html.parser')

with open('output.html', 'wb') as f:
    f.write(response.content)
webbrowser.open('output.html')

# with open("output.html") as fp:
# doc = BeautifulSoup(fp, 'html.parser')


# Grab all of the titles
title_tags = doc.find_all(class_='link_theme_outer')
# print(title_tags)
# title_tags = doc.find_all('a')
# title_tags = title_tags.find_all('b')


# title_tags = title_tags.find_all('b')

i = 21
for title in title_tags:
    if title.b != None:
        i = i+1

        print(i, title.b.text)


# for title in title_tags[:15]:
#     print(title.b)
#     # print(title.text.strip())
