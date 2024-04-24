def sudetis(a, b):
    return a + b

print(sudetis(5, 10))

#Set-ExecutionPolicy RemoteSigned -Scope Process

def daugyba(a:int, b:int) -> int:
    """
    si funkcija sudaugina du pateiktus skaicius ir grazina sveikaji skaiciu
    """
    return a * b

def rask_didziausia(a:int,b:int) -> int:
    return a if a>b else b

def pasisveikinimas(vardas):
    return f'Labas, {vardas}'

def pirmas_sarase(sarasas:list):
    return sarasas[0] if sarasas else None # if sarasas- patikrina ar tikrau suvestas sarasas
    