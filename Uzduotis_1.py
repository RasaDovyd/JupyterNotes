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