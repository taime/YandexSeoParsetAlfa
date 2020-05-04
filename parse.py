import time
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent
from pycookiecheat import chrome_cookies

domain = 'gurmanit.ru'
phrases = [
    '90,5 % колбаса с трюфелем италия',
    # 'чернила каракатицы купить',
    # 'паста трофи',
    # 'каперсы на веточке',
    # 'пекорино с трюфелем',
    # 'салями с трюфелем',
]

start_page = 0
end_page = 20
# max_position_check = 820
# res_on_page = 21
# max_page = max_position_check//res_on_page
url = "https://yandex.ru/search/?text="


hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

cookies = chrome_cookies(url)


def openHtmlPage(file):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return (soup)


def getPage(domain, text, url, p, hdr, cookies):
    text_q = urllib.parse.quote_plus(text)
    url = url + text_q + "&p=" + str(p)
    # Making Request
    response = requests.get(url, headers=hdr, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Write to file html that we got
    whiteHtmlFile(response.content, domain, text, url, p)
    return (soup)


def whiteHtmlFile(html, domain, text, url, p):
    filename = domain + '_' + text + '_' + str(p)+'.html'
    with open(filename, 'wb') as f:
        f.write(html)


def writePositionsToTxtFile(positions, domain, text):
    filename = domain+'__'+text+'.txt'
    with open(filename, 'a') as f:
        f.write(positions)


def parseSearchPage(soup, domain, text, p,):
    print("cтр. " + str(p))

    # time.sleep(2)
    pos = 21 * p
    words = ''

    # Parse Links to find domain
    title_tags = soup.find_all(class_='link_theme_outer')
    for title in title_tags:
        if title.b != None:
            pos += 1
            word = str(pos) + '. ' + title.b.text + "\n"
            words += word
            # print(pos, title.b.text)
            writePositionsToTxtFile(word, domain, text)
            if title.b.text == domain:
                print("Позиция:" + str(pos))
                return (True)
    return (False)


def checkPhrase(text):
    print("-------------------")
    print("Фраза: " + text)
    # positions = ''
    page = start_page
    didFind = False
    while (page < end_page):
        # soup = getPage(domain, text, url, page, hdr, cookies)
        soup = openHtmlPage('test.html')
        didFind = parseSearchPage(soup, domain, text, page)
        # positions += res.words
        # writePositionsToTxtFile(positions, domain, text)
        page += 1
        if didFind:
            print('FIND!!!')
            # writePositionsToTxtFile(positions, domain, text)
            break


# DOING THE JOB
print("Домен: " + domain)
print("===================")
for txt in phrases:
    checkPhrase(txt)


# def checkDomain(title, domain, text, pos):
#     if title.b.text == domain:
#         print("Позиция:" + str(pos))
#         return True
#     else:
#         return False
