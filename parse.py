import time
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


def getRandomProxy():
    # proxies_list = proxies_list_http
    proxies_list = proxies_list_https
    q_proxies = len(proxies_list)-1
    random = randint(0, q_proxies)
    proxies = {"https": proxies_list[random]}
    return proxies


def getProxies(n):
    proxy = proxies_list_https[n]
    proxies = {"https": proxy}
    return proxies


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


def getPage(domain, text, base_url, p, hdr, cookies):
    text_q = urllib.parse.quote_plus(text)
    url = base_url + text_q + "&p=" + str(p)
    # Making Request
    response = requests.get(url, headers=hdr, cookies=cookies)

    # Write to file html that we got
    whiteHtmlFile(response.content, domain, text, url, p)

    soup = BeautifulSoup(response.text, 'html.parser')
    return (soup)
    # return (response)


def continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries):
    tries += 1
    if tries > 500:
        printy("Too much tires", "r")
        return(None)
    else:
        getPageWithProxy(domain, text, base_url, p, hdr, cookies, tries)


def getPageWithProxy(domain, text, base_url, p, hdr, cookies, tries=0):
    printy("[g]Try:" + str(tries) + ". " + str(base_url) + text + "&p=" + str(p))
    proxies = getRandomProxy()
    # proxies = getProxies(tries)
    print("Proxies: "+str(proxies))
    text_q = urllib.parse.quote_plus(text)
    url = base_url + text_q + "&p=" + str(p)
    # Making Request
    try:
        # response = requests.get(url, headers=hdr, cookies=cookies, timeout=10)
        # proxies = {"https": "https://127.0.0.1"}
        response = requests.get(url, headers=hdr, cookies=cookies, proxies=proxies, timeout=5)
        response.raise_for_status()
        whiteHtmlFile(response.content, domain, text, url, p)
        if response.text is None:
            print("reponse text is None. Let's try another proxy")
            continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
        else:
            addProxyToTxtFile(proxies)
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup is None:
                printy("Soup is None", "m")
                continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
                return (false)
            else:
                hasCapcha = checkHasCapcha(soup)
                if (hasCapcha):
                    continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
                    return (False)
                else:
                    addProxyToTxtFile(proxies, file='proxies_best.txt')
                    return(soup)

    except requests.exceptions.HTTPError as errh:
        printy("Http Error", "r")
        # print("Http Error:", errh)
        continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
    except requests.exceptions.ConnectionError as errc:
        printy("Error Connecting", "r")
        # print("Error Connecting:", errc)
        continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
    except requests.exceptions.Timeout as errt:
        printy("Timeout Error", "r")
        # print("Timeout Error:", errt)
        continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
    except requests.exceptions.RequestException as err:
        printy("OOps: Something Else", "r")
        # print("OOps: Something Else", err)
        continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)


def checkHasCapcha(soup):
    title_tags = soup.find_all(class_='captcha__image')
    has_capcha = len(title_tags) > 0
    if has_capcha:
        printy("The Capcha :(", "m")

    return (has_capcha)


def whiteHtmlFile(html, domain, text, url, p):
    filename = domain + '_' + text + '_' + str(p)+'.html'
    with open(files_folder+filename, 'wb') as f:
        f.write(html)


def addPositionsToTxtFile(positions, domain, text):
    filename = domain+'__'+text+'.txt'
    with open(files_folder+filename, 'a') as f:
        f.write(positions)


def addPosResults(pos, text, domain):
    with open(domain+'_positions.csv', 'a') as f:
        f.write(str(pos) + ';' + text+"\n")


def writePositionsToTxtFile(positions, domain, text):
    filename = domain+'__'+text+'.txt'
    with open(files_folder+filename, 'w') as f:
        f.write(positions)


def addProxyToTxtFile(proxy, file='proxies.txt'):
    with open(file, 'a') as f:
        f.write(proxy["https"]+"\n")


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
                addPosResults(pos, text, domain)
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


def findWord(soup, text, page):
    res = parseSearchPage(soup, domain, text, page)
    addPositionsToTxtFile(res['words'], domain, text)
    page += 1
    if res["didFind"]:
        printy("Great! We've found it!", "m")
        return(True)
    else:
        # print("Didn't found the word on this page, will try another")
        return(False)


def checkPhrase(text):
    printy("[g]Ищем фразу: " + text)
    page = start_page
    clearTxtFile(domain, text)
    while (page < end_page):
        time.sleep(1)
        # soup = getPage(domain, text, base_url, page, hdr, cookies)
        # soup = getPageWithProxy(domain, text, base_url, page, hdr, cookies)
        # soup = BeautifulSoup(response.text, 'html.parser')
        soup = getSoupFromHtmlPage('./tmp/test.html')

        # find = findWord(soup, text, page)

        if findWord(soup, text, page):
            break
        else:
            print("didn't find it on page:" + str(page))

        page+=1

        # if soup is None:
        #     printy("Soup is None", "m")
        #     # return("STOP")
        # # elif checkHasCapcha(soup):
        # #     printy("The Capcha :(", "m")
        # #     return("STOP")
        # else:
        #     res = parseSearchPage(soup, domain, text, page)
        #     addPositionsToTxtFile(res['words'], domain, text)
        #     page += 1
        #     if res["didFind"]:
        #         printy("Great! We've found it!", "m")
        #         # return(True)
        #         break
        #     # else:
        #     #     return("Didn't found the word on this page, will try another")


def doTheJob():
    printy("[wB]   -------------------\n       " + domain + "\n   -------------------")
    wl = len(phrases)-1

    for word in phrases:
        # res = checkPhrase(word)
        # TEMPORARY TAKE RANDOM NUMBER FO DICT
        random_word = phrases[randint(0, wl)]
        res = checkPhrase(random_word)
        if res == "STOP":
            print("Had to stop program!")
            break
        # elif res:
        #     print("Great Job. Let's find another word!")
        # else:
        #     printy("res is", "yB")
        #     print(res)


doTheJob()
