from selenium import webdriver

chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://yandex.ru')
driver.save_screenshot("screenshot.png")

driver.close()




# public byte[] shootPage() throws IOException {
#     BufferedImage image = Shutterbug.shootPage(driver, ScrollStrategy.WHOLE_PAGE).getImage();
#     ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
#     ImageIO.write(image, "png", outputStream);
#     return outputStream.toByteArray();
# }