from Pamoka_26_2024_04_24 import sudetis, daugyba, rask_didziausia, pasisveikinimas # galima importuoti kiekviena testa atskirai arba:
import Pamoka_26_2024_04_24 # importavuys visa faila, nereikia atskirai kiekvienos funkcijos importuoti
import pytest

def test_sudetis():
    assert sudetis(1,2) == 3

def test_sudetis_neigiami():
    assert sudetis(-1,-5) == -6

def test_daugyba():
    assert daugyba(2,5) == 10
    assert daugyba(5,5) > 0
    assert daugyba(-5,-5) > 0
    assert daugyba(-5,5) < 0

def test_sudetis_2():
    num1, num2 = 5, 3
    rezultatas = 8
    faktinis_rezultatas = sudetis(num1, num2)
    assert rezultatas == faktinis_rezultatas, f'sudeties testas nepavyko: {num1}+{num2} turetu buti {rezultatas}, bet gavome {faktinis_rezultatas}'

def test_rask_didziausia():
    num1,num2 = 10,20
    rezultatas = 20
    faktinis_rezultatas = rask_didziausia(num1, num2)
    assert faktinis_rezultatas == rezultatas

def test_rask_didziausia_2():
    assert rask_didziausia(10,5) == 10
    assert rask_didziausia(5,10) == 10
    assert rask_didziausia(10,10) == 10

def test_pasisveikinimas():
    assert pasisveikinimas('Tomas') == 'Labas, Tomas'

def test_pasisveikinimas_2():
    assert Pamoka_26_2024_04_24.pasisveikinimas('Romas') == 'Labas, Romas'

def test_pirmas_sarase():
    skaiciai = [1,2,3,4,5]
    assert Pamoka_26_2024_04_24.pirmas_sarase(skaiciai) == 1

def test_pirmas_sarase_tekstas():
    raides = ['a', 'b', 'c']
    assert Pamoka_26_2024_04_24.pirmas_sarase(raides) == 'a'

def test_pirmas_sarase_tuscia():
    raides = []
    assert Pamoka_26_2024_04_24.pirmas_sarase(raides) == None

def test_pirmas_sarase_neListas():
    neListas = 'labas'
    assert Pamoka_26_2024_04_24.pirmas_sarase(neListas) == 'l'


# parametrai pateikiami testui, veliau juos visus pateiks testui
@pytest.mark.parametrize('sarasas, tiketinas_rezultatas',[
    ([1,2,3,4], 1), # ([sarasas], tiketinas rezultatas)
    (['a', 'b', 'c'], 'a'),
    ([], None),
    ([[1,2],[3,4],[5,6]], [1,2])
])

def test_pirmas_sarase(sarasas, tiketinas_rezultatas):
    assert Pamoka_26_2024_04_24.pirmas_sarase(sarasas) == tiketinas_rezultatas


@pytest.mark.parametrize('a,b,c,turis',[
    (1,1,1,1),
    (2,2,2,8),
    (4,4,4,64)
])
def test_kubo_turis(a,b,c,turis):
    assert Pamoka_26_2024_04_24.kubo_turis(a,b,c) == turis