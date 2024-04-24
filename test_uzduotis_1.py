import Uzduotis_1
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

