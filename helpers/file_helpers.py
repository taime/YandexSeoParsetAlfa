import json
from helpers.parsing import parseIpAddreses


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
