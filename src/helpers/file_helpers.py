import json
from helpers.parsing_helpers import parseIpAddreses
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


def openHtmlPage(file):
    with open(file) as fp:
        return (fp)


def getSoupFromHtmlPage(file):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return (soup)


def readTextFile(filename):
    f = open(filename, "r")
    s = f.read()
    return (s)


def readDataFromTextFile(filename):
    txt = readDataFromTextFile('demofile.txt')
    ip_addreses = parseIpAddreses(txt)
    return (ip_addreses)


def saveDataToTextFile(data, filename):
    a_file = open(filename, "w")
    for row in data:
        np.savetxt(a_file, row)
    a_file.close()


def saveDataToJsonFile(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def readDataFromJsonFile(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return(data)


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


def addProxyToTxtFile(proxy, file='data.txt'):
    with open(file, 'a') as f:
        f.write(proxy["https"] + "\n")


def addProxyToJsonFile(proxy, file='data.json'):
    data = readDataFromJsonFile(filename)
    data.append(proxy["https"])
    saveDataToJsonFile(data, file)


def clearTxtFile(domain, text):
    writePositionsToTxtFile('', domain, text)
