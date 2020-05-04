import time
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent
from pycookiecheat import chrome_cookies
from printy import printy, raw_format
from random import randint


files_folder = './tmp/'
domain = 'et-serv.ru'
# phrases = [
#     'томаты пилати что это',
#     'паста трофи',
#     'каперсы на веточке',
#     'пекорино с трюфелем',
#     'салями с трюфелем',
#     'помидоры пилати',
#     'сыр камамбер шввейцария',
#     'сыр бри с трюфелями купить',
#     'паста трофи',
#     '90,5 % колбаса с трюфелем италия',
#     'чернила каракатицы купить',
# ]
phrases = [
    'частотный преобразователь danfoss',
    'частотный преобразователь данфосс',
    'частотный преобразователь danfoss vlt',
    'частотный преобразователь delta',
    'частотный преобразователь дельта',
    'частотный преобразователь delta  vfd',
    'частотный преобразователь vacon',
    'частотный преобразователь вакон',
    'частотный преобразователь веспер',
    'частотный преобразователь toshiba',
    'частотный преобразователь тошиба',
    'частотный преобразователь купить',
    'частотный преобразователь цена',
    'частотный преобразователь 380',
    'частотный преобразователь квт',
    'преобразователь частоты danfoss',
    'преобразователь частоты данфосс',
    'преобразователь частоты danfoss vlt',
    'преобразователь частоты delta',
    'преобразователь частоты дельта',
    'преобразователь частоты delta  vfd',
    'преобразователь частоты vacon',
    'преобразователь частоты вакон',
    'преобразователь частоты веспер',
    'преобразователь частоты toshiba',
    'преобразователь частоты тошиба',
    'преобразователь частоты купить',
    'преобразователь частоты цена',
    'преобразователь частоты 380',
    'преобразователь частоты квт',
    'частотник danfoss',
    'частотник данфосс',
    'частотник danfoss vlt',
    'частотник delta',
    'частотник дельта',
    'частотник delta  vfd',
    'частотник vacon',
    'частотник вакон',
    'частотник веспер',
    'частотник toshiba',
    'частотник тошиба',
    'частотник купить',
    'частотник цена',
    'частотник 380',
    'частотник квт',
    'частотный преобразователь купить в москве',
    'частотный преобразователь купить в спб',
    'частотный преобразователь купить цены',
    'частотный преобразователь для электродвигателя',
    'частотный преобразователь 380 купить'
]

start_page = 0
end_page = 5
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


def strP(pos):
    if pos < 10:
        return "  " + str(pos)
    elif pos < 100:
        return " " + str(pos)
    else:
        return str(pos)


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


def checkCapcha(soup):
    title_tags = soup.find_all(class_='captcha__image')
    return (len(title_tags) > 0)


def whiteHtmlFile(html, domain, text, url, p):
    filename = domain + '_' + text + '_' + str(p)+'.html'
    with open(files_folder+filename, 'wb') as f:
        f.write(html)


def addPositionsToTxtFile(positions, domain, text):
    filename = domain+'__'+text+'.txt'
    with open(files_folder+filename, 'a') as f:
        f.write(positions)


def writePositionsToTxtFile(positions, domain, text):
    filename = domain+'__'+text+'.txt'
    with open(files_folder+filename, 'w') as f:
        f.write(positions)


def clearTxtFile(domain, text):
    writePositionsToTxtFile('', domain, text)


def parseSearchPage(soup, domain, text, p,):
    # printy("[g]cтр. " + str(p))
    # time.sleep(randint(30, 120))
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
            raw_text = ""
            if title.b.text == domain:
                if pos < 11:
                    raw_text = raw_format(strP(pos), "y>B") + raw_format(" [g]| ") + raw_format(text, "y>")
                elif pos < 30:
                    raw_text = raw_format(strP(pos), "oB") + raw_format(" [g]| ") + raw_format(text, "o")
                else:
                    raw_text = raw_format(strP(pos), "mB") + raw_format(" [g]| ") + raw_format(text, "m")
                print(raw_text)
                return ({"didFind": True, "words": words})
    return ({"didFind": False, "words": words})


def checkPhrase(text):
    # printy("[g]Ищем фразу: " + text)
    page = start_page
    clearTxtFile(domain, text)
    while (page < end_page):
        soup = getPage(domain, text, url, page, hdr, cookies)
        # soup = openHtmlPage('./tmp/et-serv.ru_частотный преобразователь delta_1.html')
        if checkCapcha(soup):
            # print("Capcha :(")
            return('capcha')
        else:
            res = parseSearchPage(soup, domain, text, page)
            addPositionsToTxtFile(res['words'], domain, text)
            page += 1
            if res["didFind"]:
                return('found')
                break


# DOING THE JOB
# printy("[wB]   -------------------\n       " + domain + "\n   -------------------")
for txt in phrases:
    res = checkPhrase(txt)
    if res == 'capcha':
        break
