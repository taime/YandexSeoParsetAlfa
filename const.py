from pycookiecheat import chrome_cookies


start_page = 0
end_page = 3
# max_position_check = 820
# res_on_page = 21
# max_page = max_position_check//res_on_page
files_folder = './tmp/'
# domain = 'gurmanit.ru'
domain = 'et-serv.ru'
base_url = "https://yandex.ru/search/?text="
cookies = chrome_cookies(base_url)


hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


phrases_g = [
    'томаты пилати что это',
    'паста трофи',
    'каперсы на веточке',
    'пекорино с трюфелем',
    'салями с трюфелем',
    'помидоры пилати',
    'сыр камамбер шввейцария',
    'сыр бри с трюфелями купить',
    'паста трофи',
    '90,5 % колбаса с трюфелем италия',
    'чернила каракатицы купить',
]

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

proxies_list_https = [
    "https://212.83.138.252:5836",
    "https://67.73.189.42:999",
    "https://50.251.229.185:80",
    "https://212.129.52.13:5836",
    "https://212.129.5.123:5836",
    "https://195.154.108.211:5836",
    "https://94.75.67.107:55443",
    "https://185.187.75.16:40484",
    "https://212.129.43.124:5836",
    "https://212.129.42.175:5836",
    "https://212.129.1.184:5836",
    "https://198.27.76.4:5007",
    "https://181.196.145.106:50899",
    "https://139.180.141.57:8118",
    "https://195.154.63.178:5836",
    "https://96.96.48.150:3128",
    "https://195.154.62.117:5836",
    "https://134.35.235.27:8080",
    "https://96.113.220.54:3128",
    "https://96.113.190.86:3128",
    "https://195.154.60.219:5836",
    "https://195.154.59.207:5836",
    "https://180.243.61.153:8080",
    "https://46.246.26.5:3128",
    "https://195.154.57.127:5836",
    "https://195.154.56.150:5836",
    "https://93.91.196.242:8080",
    "https://195.154.55.172:5836",
    "https://195.154.51.238:5836",
    "https://91.126.239.175:8080",
    "https://195.154.48.112:5836",
    "https://91.98.39.87:8080",
    "https://195.154.47.180:5836",
    "https://92.60.190.249:36987",
    "https://180.247.152.122:8080",
    "https://84.119.9.192:80",
    "https://195.154.36.151:5836",
    "https://83.151.225.191:8080",
    "https://195.154.35.206:5836",
    "https://195.154.33.119:5836",
    "https://94.74.166.97:808",
    "https://118.97.193.202:30442",
    "https://191.102.95.172:8080",
    "https://36.89.129.15:35270",
    "https://103.28.227.69:3128",
    "https://193.117.138.126:31859",
    "https://68.15.158.182:48678",
    "https://185.83.197.228:8080",
    "https://62.210.8.216:5836",
    "https://185.136.165.196:8080",
    "https://62.210.7.117:5836",
    "https://183.77.87.110:8080",
    "https://62.210.24.238:5836",
    "https://103.36.35.135:8080",
    "https://173.249.28.223:5836",
    "https://186.15.49.12:8080",
    "https://51.91.163.98:3128",
    "https://167.99.75.87:8080",
    "https://51.91.108.137:3128",
    "https://51.91.10.46:3128",
    "https://163.172.93.124:5836",
    "https://51.77.99.223:8080",
    "https://51.68.61.17:80",
    "https://163.172.226.74:5836",
    "https://14.207.79.207:8080",
    "https://51.159.66.140:5836",
    "https://36.92.216.162:8080",
    "https://51.159.52.158:5836",
    "https://51.158.30.241:5836",
    "https://45.81.168.43:8080",
    "https://51.158.154.43:5836",
    "https://51.15.188.14:5836",
    "https://51.15.182.240:5836",
    "https://51.15.187.125:5836",
    "https://163.172.117.20:5836",
    "https://51.15.178.33:5836",
    "https://163.172.11.22:5836",
    "https://37.229.122.18:8080",
    "https://160.119.125.25:8080",
    "https://144.76.24.153:3128",
    "https://134.119.179.196:5836",
    "https://142.44.148.56:8080",
    "https://183.88.17.45:8080",
    "https://89.28.53.42:8080",
    "https://134.119.190.194:5836",
    "https://134.119.179.194:5836",
    "https://74.59.132.126:49073",
    "https://128.199.184.216:8080",
    "https://212.83.190.118:5836",
    "https://212.83.189.137:5836",
    "https://212.83.188.253:5836",
    "https://212.83.185.168:5836",
    "https://212.83.179.105:5836",
    "https://167.86.66.178:3128",
    "https://212.83.166.175:5836",
    "https://212.129.62.202:5836",
    "https://212.129.58.162:5836",
    "https://212.129.57.222:5836",
    "https://212.129.38.35:5836",
    "https://212.129.28.152:5836",
    "https://212.129.27.246:5836",
    "https://118.99.95.117:8080",
    "https://163.172.229.128:5836",
    "https://194.8.146.167:50510",
    "https://171.6.147.25:8213",
    "https://102.176.160.107:8080",
    "https://195.154.58.65:5836",
    "https://96.113.176.102:3128",
    "https://44.232.52.177:8090",
    "https://103.102.138.158:8080",
    "https://187.85.151.234:8080",
    "https://185.194.25.77:8080",
    "https://185.191.172.178:8080",
    "https://212.83.178.56:5836",
    "https://110.74.219.3:8080",
    "https://87.251.238.156:37654",
    "https://163.172.96.25:5836",
    "https://139.255.160.177:8080",
    "https://163.172.63.172:5836",
    "https://110.78.138.30:8080",
    "https://177.128.121.50:3128",
    "https://42.115.25.110:8080",
    "https://118.163.83.21:3128",
    "https://162.252.144.229:8181",
    "https://58.162.229.173:45143",
    "https://155.138.131.25:8080",
    "https://50.197.38.230:60724",
    "https://178.219.118.156:8080",
    "https://5.59.145.129:8080",
    "https://136.243.204.148:8080",
    "https://129.226.77.75:10000",
    "https://202.142.155.86:8080",
    "https://213.92.182.235:8080",
    "https://71.168.222.78:3128",
    "https://45.77.110.95:80",
    "https://77.68.85.59:8080",
    "https://45.159.75.71:8080",
    "https://103.70.79.3:8080",
    "https://199.188.93.188:8000",
    "https://212.129.2.175:5836",
    "https://165.22.48.9:8080",
    "https://165.22.30.81:3128",
    "https://82.177.38.195:8080",
    "https://144.91.80.248:5836",
    "https://203.150.113.138:8080",
    "https://77.244.213.223:8080",
    "https://96.113.213.134:3128",
    "https://69.9.238.22:8080",
    "https://62.210.253.15:5836",
    "https://65.152.119.226:39408",
    "https://118.172.207.162:8080",
    "https://161.35.66.112:3128",
    "https://41.66.75.106:8080",
    "https://110.36.237.123:8080",
    "https://45.174.76.129:999",
    "https://34.92.94.5:8123",
    "https://27.72.56.206:54037",
    "https://212.205.214.216:49690",
    "https://41.72.199.6:8080",
    "https://199.188.89.254:8000",
    "https://125.25.165.97:39021",
    "https://198.255.114.82:3128",
    "https://36.66.137.181:31946",
    "https://134.209.165.18:3128",
    "https://202.5.36.131:8080",
    "https://184.180.90.226:8080",
    "https://103.114.10.250:8080",
    "https://104.41.29.74:8080",
    "https://167.71.198.204:8080",
    "https://173.82.74.58:5836",
    "https://173.82.115.174:5836",
    "https://162.246.18.77:3128",
    "https://181.198.97.241:30072",
    "https://124.121.2.94:8080",
    "https://190.242.99.162:8080",
    "https://167.71.33.239:3128",
    "https://103.101.104.223:8080",
    "https://81.16.10.141:38132",
    "https://165.227.221.151:3128",
    "https://163.172.204.39:5836",
    "https://161.35.68.137:3128",
    "https://185.158.248.106:5836",
    "https://103.75.27.74:8080",
    "https://85.175.99.136:8080",
    "https://14.207.24.23:8080",
    "https://163.53.185.22:8080",
    "https://36.85.56.26:8080",
    "https://134.209.238.181:3128",
    "https://5.252.179.8:3128",
    "https://124.41.213.201:31109",
    "https://180.183.101.165:8080",
    "https://200.89.174.4:3128",
    "https://116.204.142.62:8080",
    "https://45.70.196.140:999",
    "https://103.119.147.234:3128",
    "https://195.8.51.55:8080",
    "https://82.150.177.19:8080",
    "https://200.127.155.86:8081",
    "https://188.56.212.213:8080",
    "https://201.111.221.186:8080",
    "https://41.76.117.194:30878",
    "https://81.30.55.173:3128",
    "https://45.76.43.163:8080",
    "https://36.92.6.151:8181",
    "https://180.180.170.188:8080",
    "https://14.160.26.153:8080",
    "https://81.18.34.98:40934",
    "https://195.209.176.2:8080",
    "https://178.253.241.142:8080",
    "https://109.168.18.50:80",
    "https://94.182.48.146:8080",
    "https://87.255.13.217:8080",
    "https://36.89.228.201:52687",
    "https://149.129.240.8:8080",
    "https://121.122.96.91:8080",
    "https://180.253.79.228:8080",
    "https://183.89.154.88:8080",
    "https://102.164.203.237:38615",
    "https://91.202.240.208:51678",
    "https://103.76.19.246:8080",
    "https://89.34.208.223:49038",
    "https://36.91.188.18:3128",
    "https://42.228.3.158:8080",
    "https://115.74.201.137:42108",
    "https://167.172.161.25:3128",
    "https://185.158.249.76:5836",
    "https://203.128.72.146:8080",
    "https://188.255.252.249:54163",
    "https://36.68.254.215:8080",
    "https://103.102.13.52:3129",
    "https://212.98.143.138:8082",
    "https://103.129.192.218:41451",
    "https://91.207.238.193:8080",
    "https://212.83.168.18:5836",
    "https://125.164.13.20:8080",
    "https://88.255.182.170:8080",
    "https://181.102.207.247:7071",
    "https://110.39.169.66:8080",
    "https://212.83.189.222:5836",
    "https://103.4.145.237:8080",
    "https://103.53.76.82:8089",
    "https://212.129.54.183:5836",
    "https://95.71.126.66:8080",
    "https://81.161.61.88:55978",
    "https://200.73.130.105:8080",
    "https://85.196.183.162:8080",
    "https://151.235.164.121:8080",
    "https://41.60.232.67:8080",
    "https://212.83.180.168:5836",
    "https://36.89.8.235:8080",
    "https://36.77.71.85:8080",
    "https://51.91.158.22:3128",
    "https://110.138.192.178:8080",
    "https://171.7.78.204:8080",
    "https://36.92.219.206:30456",
    "https://45.82.138.121:3128",
    "https://45.236.104.85:8080",
    "https://134.249.141.148:8080",
    "https://197.216.2.14:8080",
    "https://169.239.45.37:8080",
    "https://103.78.213.226:57305",
    "https://37.255.235.195:80",
    "https://103.121.149.46:3128",
    "https://170.238.252.162:57101",
    "https://5.58.88.175:8080",
    "https://1.2.189.176:8080",
    "https://183.89.10.243:8080",
    "https://110.36.185.152:8080",
    "https://180.183.72.81:8080",
    "https://161.35.78.63:3128",
    "https://195.230.130.73:41068",
    "https://180.241.112.238:8080",
    "https://169.0.216.66:8080",
    "https://185.158.248.95:5836",
    "https://63.151.67.7:8080",
    "https://212.129.62.136:5836",
    "https://45.236.170.9:3282",
    "https://103.69.216.125:8080",
    "https://197.133.44.175:8080",
    "https://118.99.118.40:8080",
    "https://185.255.47.158:8080",
    "https://89.165.65.228:42019",
    "https://88.198.29.29:8080",
    "https://169.1.151.167:8080",
    "https://50.233.228.147:8080",
    "https://79.253.200.201:8080",
    "https://47.103.213.31:8080",
    "https://62.27.108.142:8080",
    "https://51.158.28.106:5836",
    "https://168.205.92.131:8080",
    "https://95.80.182.79:8080",
    "https://218.4.192.218:3128",
    "https://45.77.146.99:8118",
    "https://77.242.26.45:8080",
    "https://195.154.49.94:5836",
    "https://195.154.38.125:5836",
    "https://167.249.181.19:8080",
    "https://185.79.99.9:8080",
    "https://182.87.157.223:8080",
    "https://167.172.176.25:3128",
    "https://186.190.224.202:999",
    "https://131.196.87.117:3128",
    "https://193.68.200.85:52825",
    "https://154.118.52.242:38583",
    "https://212.129.6.45:5836",
    "https://122.50.5.146:10000",
    "https://103.248.248.165:37493",
    "https://103.86.50.186:8080",
    "https://201.18.88.150:8080",
    "https://61.163.32.88:3128",
    "https://195.24.53.195:80",
    "https://52.243.45.145:8080",
    "https://41.139.223.242:47842",
    "https://201.91.82.155:3128",
    "https://51.15.180.219:5836",
    "https://51.15.165.187:5836",
    "https://5.9.58.24:5836",
    "https://5.200.81.186:8080",
    "https://45.76.87.220:8080",
    "https://182.52.90.117:45535",
    "https://212.83.163.112:5836",
    "https://212.83.146.91:5836",
    "https://212.83.143.196:5836",
    "https://212.83.158.196:5836",
    "https://212.83.161.59:5836",
    "https://163.172.93.133:5836",
    "https://182.23.81.82:3128",
    "https://163.172.124.88:5836",
    "https://163.172.122.53:5836",
    "https://103.247.122.102:8080",
    "https://62.201.228.138:8080",
    "https://195.178.56.33:8080",
    "https://89.204.214.142:8080",
    "https://45.236.91.20:8880",
    "https://117.254.180.247:8080",
    "https://31.135.150.30:8080",
    "https://36.92.186.50:55443",
    "https://85.159.48.170:40014",
    "https://187.114.26.80:8080",
    "https://139.255.30.122:42647",
    "https://195.154.48.187:5836",
    "https://79.120.177.106:8080",
    "https://167.86.92.144:3128",
    "https://41.90.240.45:8080",
    "https://163.172.93.183:5836",
    "https://151.80.65.175:3128",
    "https://144.217.139.56:5007",
    "https://169.255.234.166:8080",
    "https://14.207.59.215:8080",
    "https://14.207.26.224:8080",
    "https://180.183.19.130:8080",
    "https://36.91.128.66:8080",
    "https://41.79.66.106:52050",
    "https://181.196.247.162:37107",
    "https://14.162.145.116:30762",
    "https://79.106.97.66:8080",
    "https://183.89.107.31:8080",
    "https://139.255.112.98:8080",
    "https://36.67.109.91:31186",
    "https://118.173.232.215:43186",
    "https://213.16.81.189:54040",
    "https://117.121.211.170:8080",
    "https://176.101.221.119:8080",
    "https://111.118.128.123:8080",
    "https://45.77.247.146:3128",
    "https://193.34.55.64:58099",
    "https://101.51.141.49:57977",
    "https://101.108.127.6:8080",
    "https://87.247.19.126:43983",
    "https://89.107.56.159:3128",
    "https://88.99.134.61:8080",
    "https://41.79.35.1:8080",
    "https://62.210.9.164:5836",
    "https://14.186.119.252:8080",
    "https://37.220.201.202:8080",
    "https://200.111.182.6:443",
    "https://18.138.91.14:3128",
    "https://51.79.38.73:9999",
    "https://176.235.80.102:9090",
    "https://51.158.153.74:5836",
    "https://38.21.34.224:8080",
    "https://41.164.199.133:8080",
    "https://105.27.116.46:37312",
    "https://118.174.233.40:45976",
    "https://129.205.98.54:8080",
    "https://201.193.180.14:42954",
    "https://36.93.70.118:8080",
    "https://36.80.124.184:8080",
    "https://81.217.151.218:56193",
    "https://190.211.81.212:80",
    "https://95.71.25.89:8080",
    "https://162.223.88.228:8080",
    "https://103.109.247.26:5758",
    "https://187.36.72.238:8080",
    "https://136.228.128.6:47025",
    "https://36.81.245.226:8080",
    "https://118.174.46.144:45330",
    "https://118.96.101.199:8080",
    "https://116.58.228.86:8080",
    "https://107.182.181.99:8080",
    "https://79.106.224.231:51254",
    "https://64.227.126.31:3128",
    "https://60.53.199.121:8080",
    "https://51.91.201.55:8585",
    "https://5.56.133.117:7080",
    "https://49.48.110.30:8080",
    "https://202.62.59.8:8080",
    "https://86.57.177.8:39217",
    "https://212.129.62.140:5836",
    "https://1.20.169.136:8080",
    "https://180.249.176.145:8080",
    "https://183.88.195.207:8080",
    "https://103.52.135.60:8080",
    "https://177.99.206.82:8080",
    "https://181.39.32.122:8080",
    "https://171.22.25.42:3128",
    "https://212.83.161.221:5836",
    "https://45.168.72.39:49638",
    "https://36.91.171.133:55443",
    "https://110.78.146.51:8080",
    "https://191.232.247.198:8080",
    "https://223.25.97.210:49941",
    "https://91.214.179.5:8080",
    "https://177.107.47.189:8080",
    "https://50.249.79.18:8080",
    "https://194.5.179.82:49015",
    "https://103.113.69.17:49491",
    "https://45.77.222.251:3128",
    "https://36.92.18.179:8080",
    "https://34.95.235.219:8080",
    "https://157.100.57.211:8080",
    "https://216.169.73.65:60204",
    "https://93.174.94.80:8080",
    "https://105.186.248.60:8080",
    "https://123.56.118.36:8080",
    "https://185.187.197.107:8080",
    "https://36.89.148.161:8080",
    "https://173.82.74.59:5836",
    "https://173.82.177.211:5836",
    "https://14.207.126.92:8080",
    "https://36.67.116.165:8080",
    "https://128.199.188.41:8000",
    "https://159.255.163.73:57708",
    "https://103.83.36.161:5836",
    "https://51.158.28.107:5836",
    "https://163.172.204.28:5836",
    "https://79.110.39.189:8080",
    "https://124.121.124.69:8080",
    "https://37.98.245.58:8080",
    "https://190.108.70.155:8080",
    "https://51.158.153.72:5836",
    "https://125.208.135.146:8080",
    "https://190.5.225.178:53570",
    "https://102.164.211.175:42346",
    "https://190.103.28.245:999",
    "https://223.204.9.14:8080",
    "https://91.212.64.229:8080",
    "https://95.71.124.147:8080",
    "https://103.206.246.214:8080",
    "https://118.172.181.147:34388",
    "https://125.167.49.71:8080",
    "https://160.119.45.111:8080",
    "https://46.246.45.208:3128",
    "https://178.134.155.82:48146",
    "https://62.210.178.191:5836",
    "https://185.69.28.213:8080",
    "https://197.159.23.174:39150",
    "https://95.65.73.200:60952",
    "https://101.109.63.69:8080",
    "https://2.139.189.242:8080",
    "https://181.112.228.6:9991",
    "https://177.22.25.244:3128",
    "https://223.204.54.100:8080",
    "https://36.94.61.194:8080",
    "https://202.75.97.82:47009",
    "https://36.90.93.234:8080",
    "https://212.129.6.232:5836",
    "https://177.131.121.103:3128",
    "https://103.81.195.2:8080",
    "https://179.95.232.131:3128",
    "https://82.117.245.190:31125",
    "https://74.85.156.94:8080",
    "https://5.133.29.19:8080",
    "https://202.166.211.143:49939",
    "https://187.95.114.125:3128",
    "https://62.210.8.166:5836",
    "https://134.119.192.210:5836",
    "https://116.197.134.222:8080",
    "https://182.253.115.66:57733",
    "https://189.112.150.241:3128",
    "https://186.46.120.230:48275",
    "https://180.183.192.164:8080",
    "https://183.89.150.10:8080",
    "https://202.169.38.198:30612",
    "https://102.67.19.132:8080",
    "https://190.57.143.66:50719",
    "https://200.63.34.193:31231",
    "https://85.128.16.61:56452",
    "https://159.192.152.232:8080",
    "https://103.216.48.83:8080"
]