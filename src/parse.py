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


def continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries):
    printy("continueGetIfNotTooManyTries", 'mb')
    tries += 1
    if tries > 500:
        printy("Too much tires", "r")
        return(None)
    else:
        getPageWithProxy(domain, text, base_url, p, hdr, cookies, tries)


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


def getPageWithProxy(domain, text, base_url, p, hdr, cookies, tries=0):
    time.sleep(1)
    printy("[g]Try:" + str(tries) + ". " + str(base_url) + text + "&p=" + str(p))
    proxies = getRandomHttpsProxy()
    print("Proxies: "+str(proxies))
    text_q = urllib.parse.quote_plus(text)
    url = base_url + text_q + "&p=" + str(p)
    # Making Request
    try:
        # response = requests.get(url, headers=hdr, cookies=cookies, timeout=10)
        response = requests.get(url, headers=hdr, cookies=cookies, proxies=proxies, timeout=1)
        response.raise_for_status()
        whiteHtmlFile(response.content, domain, text, url, p)

        if response.text is None:
            print("reponse text is None. Let's try another proxy")
            continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
        else:
            addProxyToTxtFile(proxies)
            print("We've got the page. Let's make soup!")
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup is None:
                printy("Soup is None", "m")
                continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
                return (false)
            else:
                hasCapcha = checkHasCapcha(soup)
                if (hasCapcha):
                    continueGetIfNotTooManyTries(domain, text, base_url, p, hdr, cookies, tries)
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


def parseSearchPage(soup, domain, text, p,):
    printy("[g]cтр. " + str(p))
    # time.sleep(randint(1, 2))
    pos = 21 * p
    words = ''

    # Parse Links to find domain
    title_tags = soup.find_all(class_='link_theme_outer')
    res_len = len(title_tags)

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


def findWord(soup, text, page):
    res = parseSearchPage(soup, domain, text, page)
    addPositionsToTxtFile(res['words'], domain, text)
    page += 1
    if res["didFind"]:
        printy("Great! We've found it!", "m")
        return(True)
    else:
        print("Didn't found the word on this page, will try another")
        return(False)


def checkPhrase(text):
    printy("[g]Ищем фразу: " + text)
    page = start_page
    clearTxtFile(domain, text)
    while (page < end_page):
        # time.sleep(4)
        # soup = getPage(domain, text, base_url, page, hdr, cookies)
        soup = getPageWithProxy(domain, text, base_url, page, hdr, cookies)
        # soup = getSoupFromHtmlPage('./tmp/test.html')

        if findWord(soup, text, page):
            break
        else:
            print("didn't find it on page:" + str(page))
            page += 1

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

    wl = len(phrases) - 1

    for word in phrases:
        # res = checkPhrase(word)
        random_word = phrases[randint(0, wl)]
        res = checkPhrase(random_word)

        if res == "STOP":
            print("Had to stop program!")
            break


doTheJob()
