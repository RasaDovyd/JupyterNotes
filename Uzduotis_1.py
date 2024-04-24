# 1 užduotis
# Parašykite funkciją, kuri kaip argumentą priima vieną kintamąjį (tekstą) ir grąžina jį apversta
# pavyzdžiui, pateikus žodį "labas", funkcija grąžintų atsakymą "sabal"
# pateikus žodį "alus", grąžintų "sula"
# parašykite keletą testų šiai funkcijai


def apverstas_tekstas(a):
    return ' '.join(word[::-1] for word in a.split())

# 2 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina to sąrašo narių sumą
# parašykite keletą testų šiai funkcijai

def saraso_ilgis(sarasas:list):
    return sum(sarasas)

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

def saraso_rusiavimas(sarasas:list):
    return sarasas
    return sarasas.sort(reverse=False)
    return sarasas.sort(reverse=True)