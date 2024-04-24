import Uzduotis_1 as u1
import pytest

def test_apverstas_tekstas():
    assert Uzduotis_1.apverstas_tekstas('alus') == 'sula'
    assert Uzduotis_1.apverstas_tekstas('2563') == '3652'


def test_saraso_suma():
    sarasas = [2,5,7]
    assert Uzduotis_1.saraso_suma(sarasas) == 14

# def test_saraso_suma_raides():
#     sarasas = [1,'g']
#     assert Uzduotis_1.saraso_suma(sarasas) == 'klaida'


def test_teigiami_skaiciai():
    sarasas = [-5,5,2,-6,-8,4]
    assert Uzduotis_1.teigiami_skaiciai(sarasas) == [5,2,4]

# def test_teigiami_skaiciai_eror():
#     sarasas = [-5,5,'a',-6,-8,4]
#     assert Uzduotis_1.teigiami_skaiciai(sarasas) == 'klaida'  


def test_rikiuoti_mazejanciai():
    assert Uzduotis_1.rikiuoti(Uzduotis_1.rikiuoti_mazejanciai, [4,5,1,3]) == [5,4,3,1]

def test_rikiuoti_didejanciai():
    assert Uzduotis_1.rikiuoti(Uzduotis_1.rikiuoti_didejanciai, [4,5,1,3]) == [1,3,4,5]

# @pytest.mark.parametrize('a,b,c,turis',[
#     (1,1,1,1),
#     (2,2,2,8),
#     (4,4,4,64)
# ])
# def test_kubo_turis(a,b,c,turis):
#     assert u1.kubo_turis(a,b,c) == turis


# 1
@pytest.mark.parametrize('skaicius, tiketinas_rezultatas',[
    (2,'nesidalina'),
    (3,'dalinasi'),
    (15,'dalinasi'),
    (65,'nesidalina')
])
def test_skaiciaus_dalyba_is3(skaicius, tiketinas_rezultatas):
    assert u1.skaiciaus_dalyba_is3(skaicius) == tiketinas_rezultatas

#2
@pytest.mark.parametrize('zodziai, tiketinas_rezultatas',[
    (['labas','rytas'],['labas']),
    (['saltas','pavasaris'],['saltas','pavasaris']),
    (['maza', 'grazi', 'knyga'],['maza'])
])
def test_pasikartojancios_raides(zodziai, tiketinas_rezultatas):
    assert u1.pasikartojancios_raides(zodziai) == tiketinas_rezultatas


#3
@pytest.mark.parametrize('skaicius, tiketinas_rezultatas',[
    (55,'True'),
    (13,'True'),
    (47,'True'),
    (24,'False')
])
def test_pirminis_skaicius(skaicius, tiketinas_rezultatas):
    assert u1.pirminis_skaicius(skaicius) == tiketinas_rezultatas