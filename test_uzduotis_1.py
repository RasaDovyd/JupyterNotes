import Uzduotis_1

def test_apverstas_tekstas():
    # return ' '.join(word[::-1] for word in a.split())
    assert Uzduotis_1.apverstas_tekstas('alus') == 'sula'
    assert Uzduotis_1.apverstas_tekstas('2563') == '3652'
    assert Uzduotis_1.apverstas_tekstas('s a l t a') == 'a t l a s' # cia net nezinau kokio rezultato tiketis

def test_saraso_suma(sarasas):
    sarasas = [2,5,7]
    assert Uzduotis_1.saraso_suma(sarasas) == 14

def test_saraso_suma_raides(sarasas):
    sarasas = ['s','g']
    assert Uzduotis_1.saraso_suma(sarasas) == Error # nezinau kaip ivardinti tiketina rezultata

def test_saraso_suma_raides(sarasas):
    sarasas = [5,'s',3] # nezinau ar reikia toki scenariju testtuoti
    assert Uzduotis_1.saraso_suma(sarasas) == Error 

def test_teigiami_skaiciai(sarasas:list):
    # naujas_sarasas = []
    # for skaicius in sarasas:
    #     if skaicius> 0:
    #         naujas_sarasas.append(skaicius)
    # return naujas_sarasas
    sarasas = [-5,5,2,-6,-8,4]
    assert Uzduotis_1.teigiami_skaiciai(sarasas) == [5,2,4]

def test_teigiami_skaiciai_eror(sarasas:list):
    sarasas = [-5,5,a,-6,-8,4]
    assert Uzduotis_1.teigiami_skaiciai(sarasas) == error  

# def test_saraso_rusiavimas(sarasas:list):
