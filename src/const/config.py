from pycookiecheat import chrome_cookies


start_page = 0
end_page = 10
# max_position_check = 820
# res_on_page = 21
# max_page = max_position_check//res_on_page
files_folder = 'tmp/'
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


phrases_k = [
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
