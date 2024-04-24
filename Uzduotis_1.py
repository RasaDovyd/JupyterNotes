# 1 užduotis
# Parašykite funkciją, kuri kaip argumentą priima vieną kintamąjį (tekstą) ir grąžina jį apversta
# pavyzdžiui, pateikus žodį "labas", funkcija grąžintų atsakymą "sabal"
# pateikus žodį "alus", grąžintų "sula"
# parašykite keletą testų šiai funkcijai

def apverstas_tekstas(a):
    return a[::-1]


# 2 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina to sąrašo narių sumą
# parašykite keletą testų šiai funkcijai

def saraso_suma(sarasas:list):
    suma = sum(sarasas)
    return suma


# 3 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina jame esančius TEIGIAMUS skaičius
# parašykite keletą testų šiai funkcijai

def teigiami_skaiciai(sarasas:list):
    naujas_sarasas = []
    for skaicius in sarasas:
        if skaicius> 0:
            naujas_sarasas.append(skaicius)
    return naujas_sarasas


# 4 užduotis
# Parašykite funkciją, kuri priima dvi sąrašų rūšiavimo funkcijas: vieną didėjančiai rūšiavimui, kitą mažėjančiai rūšiavimui, ir sąrašą skaičių. 
# Funkcija turi grąžinti rūšiuotą sąrašą pagal pateiktas rūšiavimo funkcijas.
# parašykite keletą testų šiai funkcijai

# Ilgesnis variantas:
# def saraso_rikiavimas(f:str,sarasas:list)-> list: # f- funkcija
#     def rikiuoti_mazejanciai(sarasas):
#       return sorted(sarasas,reverse=False)  

#     def rikiuoti_didejanciai(sarasas):
#       return sorted(sarasas) 

#     if f == 'didejanciai':
#         return rikiuoti_didejanciai(sarasas)
#     else:
#         return rikiuoti_mazejanciai(sarasas)

# print(saraso_rikiavimas('didejanciai', [1,5,2]))


# funkcija pteikiam kaip argumenta

def rikiuoti(rikiavimo_funkcija, sarasas):
    return rikiavimo_funkcija(sarasas)

def rikiuoti_mazejanciai(sarasas):
    return sorted(sarasas, reverse=True)

def rikiuoti_didejanciai(sarasas):
    return sorted(sarasas)

print(rikiuoti(rikiuoti_mazejanciai, [5,3,4,1,6,9]))


# 1 Užduotis
# Sukurkite funkciją, kuri patikrintų ar skaičius dalinasi iš 3
# Parašykite keletą testų (naudojantis parametrize)

def skaiciaus_dalyba_is3(skaicius):
    if skaicius % 3 == 0:
        return 'dalinasi'
    else:
        return 'nesidalina'


# 2 užduotis 
# Parašykite funkciją rasti_pasikartojancias_raides, kuri priima sąrašą žodžių ir grąžina sąrašą tų žodžių
# kurie turi bent vieną pasikartojančią raidę.
# Parašykite keletą testų (naudojantis parametrize)

def pasikartojancios_raides(zodziai):
    pasikartojantys_z = []
    for zodis in zodziai:
        for raide in zodis:
            if zodis.count(raide) > 1:
                pasikartojantys_z.append(zodis)
                break
    return pasikartojantys_z

# kitas budas:
# def pasikartojancios_raides(zodziai):
    # pasikartojantys_z = []
    # for zodis in zodziai:
    #     if len(set(zodis)) < len(zodis):
    #         pasikartojantys_z.append(zodis)
    # return pasikartojantys_z


# 3 užduotis 
# Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis. 
# Grąžinkite True, jei skaičius yra pirminis, ir False, jei ne.
# Parašykite keletą testų (naudojantis parametrize)

def pirminis_skaicius(skaicius:int):
    if skaicius <= 2:
        return 'False'
    for sk in range(2,skaicius):
        if skaicius % sk == 0:
            return 'False'
        else:
            return 'True'