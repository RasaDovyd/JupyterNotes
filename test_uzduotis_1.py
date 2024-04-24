import Uzduotys_1

def test_apverstas_tekstas():
    # return ' '.join(word[::-1] for word in a.split())
    assert Uzduotys_1.apverstas_tekstas('alus') == 'sula'

# def test_saraso_ilgis(sarasas:list):
    # return sum(sarasas)

# def test_teigiami_skaiciai(sarasas:list):
    # naujas_sarasas = []
    # for skaicius in sarasas:
    #     if skaicius> 0:
    #         naujas_sarasas.append(skaicius)
    # return naujas_sarasas

# def test_saraso_rusiavimas(sarasas:list):
    # return sarasas
    # return sarasas.sort(reverse=False)
    # return sarasas.sort(reverse=True)