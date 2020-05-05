import time
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser
from fake_useragent import UserAgent
from pycookiecheat import chrome_cookies
from printy import printy, raw_format
from random import randint

import http.client

# proxies = {"http": "http://192.41.71.204:3128"}

proxies_list = ["http://192.41.71.204:3128",
                "http://159.65.255.142:3128",
                "http://96.234.124.154:80",
                "http://3.21.117.16:80",
                "http://24.172.82.94:53281",
                "http://173.192.128.238:25",
                "http://80.187.140.26:8080",
                "http://159.8.114.34:8123",
                "http://176.103.48.116:1182",
                "http://52.166.247.251:80",
                "http://92.79.65.240:8080",
                "http://79.137.123.252:3129",
                "http://200.52.141.162:53281",
                "http://167.86.96.193:80",
                "http://169.57.157.148:8123",
                "http://138.68.53.44:8118",
                "http://125.167.100.150:80",
                "http://51.77.149.1:3133",
                "http://79.137.123.155:3129",
                "http://54.37.14.65:3129",
                "http://91.150.189.122:43102",
                "http://198.50.152.64:23500",
                "http://138.36.2.186:45277",
                "http://144.217.101.242:3129",
                "http://191.100.128.158:21776",
                "http://91.210.169.241:80",
                "http://185.56.8.209:84",
                "http://181.118.167.104:80",
                "http://190.84.232.87:49907",
                "http://14.38.255.39:80",
                "http://189.57.62.146:80",
                "http://185.56.209.114:51386",
                "http://31.179.224.42:38263",
                "http://94.130.179.24:8045",
                ]


def getRandomProxy():
    q_proxies = len(proxies_list)-1
    random = randint(0, q_proxies)
    proxies = {"http": proxies_list[random]}
    return proxies

# proxies = ['167.114.167.143:']


files_folder = './tmp/'
# domain = 'gurmanit.ru'
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
end_page = 3
# max_position_check = 820
# res_on_page = 21
# max_page = max_position_check//res_on_page
url = "http://yandex.ru/search/?text="


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
        return (fp)


def getSoupFromHtmlPage(file):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return (soup)


def getPage(domain, text, url, p, hdr, cookies):
    text_q = urllib.parse.quote_plus(text)
    url = url + text_q + "&p=" + str(p)
    # Making Request
    response = requests.get(url, headers=hdr, cookies=cookies)

    # Write to file html that we got
    whiteHtmlFile(response.content, domain, text, url, p)

    # soup = BeautifulSoup(response.text, 'html.parser')
    # return (soup)
    return (response)


def continueGetIfNotTooManyTries(domain, text, url, p, hdr, cookies, tries):
    tries += 1
    if tries > 500:
        printy("Too much tires", "r")
        return(None)
    else:
        getPageWithProxy(domain, text, url, p, hdr, cookies, tries)


def getPageWithProxy(domain, text, url, p, hdr, cookies, tries=0):
    proxies = getRandomProxy()
    printy("proxy is:", "c")
    print(proxies)
    text_q = urllib.parse.quote_plus(text)
    url = url + text_q + "&p=" + str(p)
    # Making Request
    try:
        response = requests.get(url, headers=hdr, cookies=cookies, proxies=proxies, timeout=10)
        # response = requests.get(url, headers=hdr, cookies=cookies,  timeout=10)
        response.raise_for_status()
        addProxyToTxtFile(proxies)
        whiteHtmlFile(response.content, domain, text, url, p)
        return(response)
    except requests.exceptions.HTTPError as errh:
        printy("ERROR HTTP ", "rB")
        print("Http Error:", errh)
        continueGetIfNotTooManyTries(domain, text, url, p, hdr, cookies, tries)
    except requests.exceptions.ConnectionError as errc:
        printy("ERROR Connecting ", "rB")
        print("Error Connecting:", errc)
        continueGetIfNotTooManyTries(domain, text, url, p, hdr, cookies, tries)
    except requests.exceptions.Timeout as errt:
        printy("ERROR TIMEOUT", "rB")
        print("Timeout Error:", errt)
        continueGetIfNotTooManyTries(domain, text, url, p, hdr, cookies, tries)
    except requests.exceptions.RequestException as err:
        printy("ERROR OOps ", "rB")
        print("OOps: Something Else", err)
        continueGetIfNotTooManyTries(domain, text, url, p, hdr, cookies, tries)


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


def addProxyToTxtFile(proxy):
    with open('proxies.txt', 'a') as f:
        f.write(proxy["http"]+"\n")


def clearTxtFile(domain, text):
    writePositionsToTxtFile('', domain, text)


def parseSearchPage(soup, domain, text, p,):
    printy("[g]cтр. " + str(p))
    # time.sleep(randint(1, 4))
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
            if title.b.text == domain:
                printPosWithColor(pos, text)
                return ({"didFind": True, "words": words})
    return ({"didFind": False, "words": words})


def printPosWithColor(pos, text):
    if pos < 11:
        raw_text = raw_format(strP(pos), "y>B") + raw_format(" [g]| ") + raw_format(text, "y>")
    elif pos < 30:
        raw_text = raw_format(strP(pos), "oB") + raw_format(" [g]| ") + raw_format(text, "o")
    else:
        raw_text = raw_format(strP(pos), "mB") + raw_format(" [g]| ") + raw_format(text, "m")
    print(raw_text)


def checkPhrase(text):
    printy("[g]Ищем фразу: " + text)
    page = start_page
    clearTxtFile(domain, text)
    while (page < end_page):
        # response = getPage(domain, text, url, page, hdr, cookies)

        # response = getPageWithProxy(domain, text, url, page, hdr, cookies)
        # soup = BeautifulSoup(response.text, 'html.parser')

        soup = getSoupFromHtmlPage('./tmp/et-serv.ru_частотный преобразователь 380_0.html')

        if soup is None:
            printy("Soup is None", "m")
            return("STOP")
        elif checkCapcha(soup):
            printy("The Capcha :(", "m")
            return("STOP")
        else:
            print("We have Soup!")
            res = parseSearchPage(soup, domain, text, page)
            addPositionsToTxtFile(res['words'], domain, text)
            page += 1
            if res["didFind"]:
                printy("Great! We've found it!", "m")
                return(True)
                break
            else:
                return("Didn't found the word on this page, will try another")


def doTheJob():
    printy("[wB]   -------------------\n       " + domain + "\n   -------------------")

    for word in phrases:
        res = checkPhrase(word)
        # # TEMPORARY TAKE RANDOM NUMBER FO DICT
        # random_word = phrases[randint(0, len(phrases)-1)]
        # res = checkPhrase(random_word)
        if res == "STOP":
            print("Had to stop program!")
            break
        elif res:
            print("Great Job. Let's find another word!")
        else:
            printy("res is", "yB")
            print(res)


doTheJob()
