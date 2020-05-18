from selenium import webdriver

chrome_path = r'/usr/local/bin/chromedriver'  # path from 'which chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://free-proxy-list.net')


driver.close()
