import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

puslapio_nr = [2,3,4,5,6,7,8,9,10,11]
opcijos = Options()
data = [] # data turi buti cia, pries for cikla, kitaip surinks visu psl info, bet i faila irasys tik vieno..

for puslapis in puslapio_nr:
    url = f'https://www.aruodas.lt/butai/puslapis/{puslapis}'
    driver = webdriver.Chrome(options=opcijos)
    driver.get(url)
    time.sleep(60)
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    ResultSet = bs.find_all('div', {'class':'advert-flex'})
    print(len(ResultSet))

    for skelbimas in ResultSet:
        try:
            price_element= skelbimas.find('div', {'class':'price'})
            tag = price_element.find('span')
            kaina = tag.contents[0]

            kvm_kaina_element= skelbimas.find('div', {'class':'price'})
            tag1 = kvm_kaina_element.find('span', {'class':'price-pm-v2'})
            kvm_kaina =tag1.contents[0]

            address_element = skelbimas.find('div', {'class':'list-adress-v2'})
            tag2 = address_element.find('h3').find('a', href=True)
            linkas = tag2['href']
            tekstas = tag2.contents

            plotas_element= skelbimas.find('div', {'class':'list-AreaOverall-v2 list-detail-v2'})
            plotas =plotas_element.contents[0]

            kambasiu_sk_element= skelbimas.find('div', {'class':'list-RoomNum-v2 list-detail-v2'})
            kambariu_sk =kambasiu_sk_element.contents[0]

            f = ''
            for i in kaina:
                f = f + str(i).strip()
            kaina = f.replace('€', '')

            f1 = ''
            for a in kvm_kaina:
                f1 = f1 + str(a).strip()
            kvm_kaina = f1[:-4]

            f2 = ''
            for i in tekstas:
                f2 = f2 + str(i).strip()
            tekstas = f2.replace('<br/>', ', ')

            f3 = ''
            for a in plotas:
                f3 = f3 + str(a).strip()
            plotas = f3

            f4 = ''
            for i in kambariu_sk:
                f4 = f4 + str(i).strip()
            kambariu_sk = f4

            d = {'buto _kaina':kaina, 'kvadrato_kaina': kvm_kaina, 'adresas':tekstas, 'plotas':plotas, 'kambariu_skaicius':kambariu_sk} # pasidarome zodyna su duomenimis
            data.append(d)
            print(d)

        except Exception as klaida:
            print(klaida)

    driver.close() 

df = pd.DataFrame(data=data)
df.to_csv('Aruodas 2024_04_22.csv', header=True, index=False, sep=';') # sukeliam sugeneruotus duomenis i sukuriama faila