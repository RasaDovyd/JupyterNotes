import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


puslapio_nr = [2,3,4,5,6]
opcijos=Options()
driver=webdriver.Chrome(options=opcijos)
data=[]

for puslapis in puslapio_nr:
    url = f'https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr={puslapis}'
    driver.get(url)
    time.sleep(60)
    source=driver.page_source
    bs=BeautifulSoup(source,'html.parser')
    ResultSet=bs.find_all('div',{'class':'announcement-content'})
    print(len(ResultSet))
    if "human" in str(source).lower():
        print('mus pagavo')
        break

    if len(ResultSet) > 0:
        for skelbimas in ResultSet:
            try:
                gamintojas_element= skelbimas.find('div', {'class':'announcement-body-heading'})
                tag = gamintojas_element.find('div', {'class':'announcement-title'})
                gamintojas = tag.text.split()[0]

                modelis_element= skelbimas.find('div', {'class':'announcement-body-heading'})
                tag = modelis_element.find('div', {'class':'announcement-title'})
                modelis = ' '.join(tag.text.split()[1:])
                
                pagaminimoData_element= skelbimas.find('div', {'class':'announcement-title-parameters'}).find('div',{'class':'announcement-parameters'})
                tag1 = pagaminimoData_element.text
                pagaminimoData = (pagaminimoData_element.contents)[1].text

                kebulas_element= skelbimas.find('div', {'class':'announcement-title-parameters'}).find('div',{'class':'announcement-parameters'})
                tag2 = kebulas_element.text
                kebulas = (kebulas_element.contents)[3].text

                kaina_element= skelbimas.find('div', {'class':'announcement-body-heading'}).find('div',{'class':'pricing-container has-loan-price'}).find('div',{'class':'announcement-pricing-info'}).find('strong')
                kaina = kaina_element.text.strip()

                kuras_element= skelbimas.find('div',{'class':'announcement-parameters-block'}).find('div',{'class':'announcement-parameters'}).find('span')
                kuras = kuras_element.text.replace('\n','').strip()

                pavaru_deze_element= skelbimas.find('div',{'class':'announcement-parameters-block'}).find('div',{'class':'announcement-parameters'})
                pavaru_deze = pavaru_deze_element.text.split('\n')[3] # pasidariau sarasa, ji isslitinau per \n ir paemiau 4 elementa

                variklis_element= skelbimas.find('div',{'class':'announcement-parameters-block'}).find('div',{'class':'announcement-parameters'})
                variklis = variklis_element.text.split('\n')[5].split(',')[0].strip()

                kw_element= skelbimas.find('div',{'class':'announcement-parameters-block'}).find('div',{'class':'announcement-parameters'})
                kw = kw_element.text.split('\n')[5].split(',')[1].strip()

                rida_element= skelbimas.find('div',{'class':'announcement-parameters-block'}).find('div',{'class':'announcement-parameters'})
                rida = rida_element.text.split('\n')[6].strip()

                miestas_element= skelbimas.find('div',{'class':'announcement-parameters-block'}).find('div',{'class':'announcement-parameters'})
                miestas = miestas_element.text.split('\n')[7].strip()

                d = {'Gamintojas':gamintojas,'Modelis':modelis, 'Pagaminimo data':pagaminimoData, 'Kėbulo tipas':kebulas, 'Kaina':kaina, 'Kuros tipas':kuras, 'Pavarų dėžė':pavaru_deze, 'Variklio turis':variklis, 'Variklio galia':kw, 'Rida':rida, 'Miestas':miestas}
                data.append(d)
                print(d)

            except Exception as klaida:
                print(klaida)   
    else:
        print("skelbimu nerasta")

driver.close() 

df = pd.DataFrame(data=data)
df.to_csv('Auto_plius 2024_04_23.csv', header=True, index=False)