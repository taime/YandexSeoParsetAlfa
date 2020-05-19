
def parseIpAddreses(txt):
    ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', txt)
    # for i in range(len(ips)):
    #     print(ips[i])
    return (ips)
