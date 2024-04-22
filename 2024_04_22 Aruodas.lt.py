#!/bin/python3

# web scrapinimui atsidarome python langa, ne Jupyter Notes, nes gali uzluzti Jupyter Notes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
# import undetected_chromedriver as uc # sita reikia isjungti ant musu kompo, ant kito gali tekti naudoti ir tada atkomentuoti 23 eilute, o uzkomentuoti 24
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


opcijos = Options()
# opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless') # Naudojant Headless yra rizika, kad atpazins puslapis, kad esi web scrapintojas, todel ne visada naudojam. Su headless kodas veikia vizualiai neatidarydamas narsykles lango.

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

url = "https://www.aruodas.lt/butai/puslapis/2/"

driver.get(url)

time.sleep(35)

source = driver.page_source

# print(source)

bs = BeautifulSoup(source, 'html.parser') # analizuojam source

ResultSet = bs.find_all('div', {'class':'advert-flex'})
# print(len(ResultSet)) # eilute naudojama patikrinimui, jeigu atsakymas bus ne nulis- reiskia kodas veikia iki cia, jeigu us 0- reiskai reikia taisyti. Paskaiciuoja kiek yra AdvertFlex konteineriu puslapyje( nebutinai skelbimu, konteineryje gali buti ir kita info)

for skelbimas in ResultSet:
    try:
        address_element = skelbimas.find('div', {'class':'list-adress-v2'})
        tag = address_element.find('h3').find('a', href=True)
        linkas = tag['href']
        tekstas = tag.contents # tekstą galima pasiekti ir per . contents atributa. Grazina sarasa visu elementu, kuris yra tekste  href elemente. .text grazina contents teksta kaip vientisa teksta- nepatogu.

        price_element= skelbimas.find('div', {'class':'price'})
        tag1 = price_element.find('span')
        kaina = tag1.contents[0]

        kvm_kaina_element= skelbimas.find('div', {'class':'price'})
        tag2 = kvm_kaina_element.find('span', {'class':'price-pm-v2'})
        kvm_kaina =tag2.contents[0]

        f = ''
        for i in tekstas:
            f = f + str(i).strip() # str- rasom, kad garantuotai gauti teksta
        adresas = f.replace('<br/>', ', ')

        # a = ''
        # for x in kaina:
        #     x = x + int(x).strip()
        # kaina = x.replace(' ', '')[:-1]

        # b = ''
        # for y in kvm_kaina:
        #     y = y + int(y).strip()
        # kvm_kaina = y.replace(' ', '')[:-4]

        # tekstas = tag.text.trim() # .strip() tai string metodas pasalina tarpus is prandzios ir is pabaigos
        print('====SKELBIMAS====')
        print(linkas, adresas, kaina, kvm_kaina, sep='\n') 
    except:
        pass # be try ir accept negavome norimo rezultato, nes href naudojamas ne tik skelbimo linkui. Su Try ir except mes tuos negerus atsakymus atmetame ir ju nespausdiname. tokiu budu turime tik skelbimus. 

driver.close() 



# Jūsų užduotis:
# Iš printinti linką, adresą, buto kainą, buto kainą už 1 kv metrą, vaizdas turi būti toks:
# ===SKELBIMAS===
# linkas,
# adresas
# kaina
# kaina už 1 kv metrą