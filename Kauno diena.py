import selenium # importuojam selenium biblioteka
# import undetected_chromedriver as uc # kazka paslepia
from bs4 import BeautifulSoup # parsina kazka
from selenium import webdriver # webdriver artitinka interneto narsykle, irankis kuris atidarines narsykle
from selenium.webdriver.chrome.options import Options

import time # importuojamas del sleep komandos, kad tarp zingsniu butu tarpai ir web puslapis musu neisristu

opcijos= Options()
opcijos.add_argument('--incognito') # tekstas chrome narsyklei, kad atidarytu narsykle incognito rezimu

driver=webdriver.Chrome(options=opcijos) # susikurem driveri

url= "https://www.kauno.diena.lt" #url, kuri norime atidaryti

driver.get(url) # puslapio atidarymas
time.sleep(3) # nurodome kiek laiko pasnausti

source = driver.page_source # pasiimam puslapio html koda

bs = BeautifulSoup(source,'html.parser')# analizuojame internetinipuslapi su BeautifulSoup, htm.parser reiskai turi analizuoti html kodus biblioteka, teoriskai isparsinama puslapio html

ResultsSet = bs.find_all('a',{'class':'articles-list-title'}) # ieskome reikiamos vietos class: su ":articles-list-title
print(ResultsSet)

# print(source) # isspausdinam puslapio koda, kai isitikinam kad veikia, galim istrinti
# driver.close() # uzdarom
# rezultatas: gauname sarasa ir tada dirbame su juo

for elementas in ResultsSet: 
    print('::ELEMENTAS')
    print(elementas)    # Isspausdina sarasa atskirai kiekvienas jo elementas atsklirtas zodziu Elementas
    print(elementas['href']) # atrenka nuoroda i straipsni, nes prie href puslapio kode yra parasyta nuoroda i straipsni. 
    print(elementas.text) #isspausdina atskirai straipsnio pavadinima. Pasiekeme elemente esanti teksta, siuo atveju straipsnio pavadinima


# PABAIGTI
# Surinkite visus kauno dienos straipsnių pavadinimus į pandas dataframe.
# pridėkite naują stulpelį, kuriame būtų žodžių kiekis kiekviename pavadinime
# pridėkite naują stulpelį, kuriame būtų pavadinime esančių simbolių kiekis
# eksportuokite tai į CSV failą
# eksportuotą CSV failą nuskaitykite su pandas
# Koks vidutinis žodžių kiekis pavadinimuose?

# kas atliko šią užduotį: turit likus į kiekvieną straipsnį konkrečiai. 
# Surinkite tokią statistiką - kiek žodžių turi straipsniai? 
# Koks vidutinis žodžių kiekis? 
# Kiek yra straipsnių, kurių žodžių kiekis yra mažesnis, didesnis už vidurkį? 
# Kokia žodžių kiekio mediana?


