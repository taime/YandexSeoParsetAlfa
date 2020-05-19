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


def readTextFile(filename):
    f = open(filename, "r")
    s = f.read()
    return (s)


def parseIpAddreses(string):
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', s)
    # for i in range(len(ips)):
    #     print(ips[i])
    return (ips)


def whiteHtmlFile(htmlBody, filename):
    with open(filename, 'wb') as f:
        f.write(htmlBody)


def getSoupFromHtmlPage(file):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return (soup)


def parseIpAddreses(txt):
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', txt)
    return (ips)


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


def saveArrayToJsonFile(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def readDataFromJsonFile(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return(data)
