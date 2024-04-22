import selenium
# import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time # dėl sleep komandos


opcijos = Options()
opcijos.add_argument('--incognito')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

url = "https://www.kaunodiena.lt"

driver.get(url)
time.sleep(10)

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source,'htmp.parser')# analizuojame internetinipuslapi su BeautifulSoup, htm.parser reiskai turi analizuoti html kodus biblioteka, teoriskai isparsinama puslapio html

bs.find_all('a',{'class':':articles-list-title'}) # ieskome reikiamos vietos class: su ":articles-list-title
print(bs)

# print(source)

# driver.close()
